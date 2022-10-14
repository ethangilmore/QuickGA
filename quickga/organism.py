from typing import Dict
from quickga.traits.basetrait import BaseTrait

class Organism:
    """A class to represent an Organism with Traits capable of simulated evolution

    Derived classes should use the add_trait or set_trait method to add traits capable of optimization
    The traits name should be the same as the class attribute

    All derived classes must implement the 'evaluate' method
    This method recieves no arguments and returns a numeric value representing a fitness score (higher value means more fit)

    Attributes:
        fitness:
            A number assigned to the organism representing its fitness levelt (higher means more fit)
        parents:
            The Organisms which were bred to produce this Organism
    """

    def __init__(self):
        self._traits = {}
        self.fitness = 0
        self.parents = []

    def __add__(self, other):
        """Creates a new object of the same class whose traits are generated from the parents"""
        return self.breed(other)

    def breed(self, other: 'Organism') -> 'Organism':
        """Creates a new object of the same class whose traits are generated from the parents
        
        Args:
            other:
                Another Organism whose traits should be combined to create the childs traits

        Returns:
            An Organism whose traits are derived from the parents traits
        """
        if type(other) is not type(self):
            raise Exception(f"Addition operation not supported for types {self.__class__.__name__} and {other.__class__.__name__}")
        # create new object of the same type as self
        child = self.__class__()
        # cache a reference to the parents and childrens class attributes
        child_vars = vars(child)
        parent1_vars = vars(self)
        parent2_vars = vars(other)
        # create the traits for the child organism
        for trait_name in self._traits:
            # we need the trait object because it contains the logic for creating a new value from the parents values
            trait_obj = self._traits[trait_name]
            # sets the child objects actual class attribute to the value derived from both the parents
            child_vars[trait_name] = trait_obj.from_parent_values(parent1_vars[trait_name], parent2_vars[trait_name])

        child.parents = [self, other]
        return child

    def add_trait(self, variable_name: str, trait: BaseTrait) -> None:
        """Adds a new trait capable of optimization to the organism
        
        A new class attribute will be created with the name provided in the 'variable_name'
        and the inital value will be set using the logic from the corresponding trait

        Example:
            self.add_trait('height', IntTrait(0, 10))
            
            print(self.height)
            # outputs some number from 0 to 10

        Args:
            variable_name:
                The name of the trait and class attribute
            trait:
                An object of a class derived from BaseTrait containing the logic for how the trait should be passed down
        """
        self._traits[variable_name] = trait
        vars(self)[variable_name] = trait.inital_value()

    def set_traits(self, traits: Dict[str, BaseTrait]) -> None:
        """Sets all of the traits capable of optimization in the organism
        
        New class attributes will be created with the names provided in the keys of the traits Dict
        and the inital values will be set using the logic from mapped corresponding trait

        Example:
            self.add_trait('height', IntTrait(0, 10))
            
            print(self.height)
            # outputs some number from 0 to 10

        Args:
            traits:
                A Dict of form {string: Trait} where Trait derives from BaseTrait
        """
        self._traits.clear()
        for trait_name, trait in traits.items:
            self.add_trait(trait_name, trait)

    @staticmethod
    def evolve(population_size: int, generations: int, selection_function) -> Dict:
        """The magic method responsible for optimizing the traits using a Genetic Algorithm
        
        Args:
            population_size:
                The number of Organisms in each generations
            generations:
                How many generations of evolution should take place
            selection_function:
                A function discribing the way of selecting parents from the population
        """
        raise NotImplementedError()

    def evaluate(self) -> float:
        """The function which determines the fitness of each Organism

        THIS METHOD MUST BE OVERWRITTEN BY ALL DERIVED CLASSES

        Args:
            None

        Returns:
            A numeric value representing a fitnes score (higher means more fit)
        """
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'evaluate' method")