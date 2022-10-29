import math
import random

from quickga import BaseTrait, ProportionalSelection

class Organism:
    """A class to represent an Organism with Traits capable of simulated evolution

    Derived classes should use the add_trait or set_trait method to add traits capable of optimization
    The traits name should be the same as the instance attribute

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

    def __add__(self, other) -> 'Organism':
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
        # cache a reference to the parents and childrens instance attributes
        child_vars = vars(child)
        parent1_vars = vars(self)
        parent2_vars = vars(other)
        # create the traits for the child organism
        for trait_name in self._traits:
            # we need the trait object because it contains the logic for creating a new value from the parents values
            trait_obj = self._traits[trait_name]
            # sets the child objects actual instance attribute to the value derived from both the parents
            child_vars[trait_name] = trait_obj.from_parent_values(parent1_vars[trait_name], parent2_vars[trait_name])

        child.parents = [self, other]
        return child

    def add_trait(self, variable_name: str, trait: BaseTrait):
        """Adds a new trait capable of optimization to the organism
        
        A new instance attribute will be created with the name provided in the 'variable_name'
        and the inital value will be set using the logic from the corresponding trait

        Example:
            self.add_trait('height', IntTrait(0, 10))
            
            print(self.height)
            # outputs some number from 0 to 10

        Args:
            variable_name:
                The name of the trait and instance attribute
            trait:
                An object of a class derived from BaseTrait containing the logic for how the trait should be passed down
        """
        self._traits[variable_name] = trait
        vars(self)[variable_name] = trait.inital_value()

    def set_traits(self, traits: dict):
        """Sets all of the traits capable of optimization in the organism
        
        New instance attributes will be created with the names provided in the keys of the traits Dict
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
    def __generate_population_info(population: list) -> dict:
        """Creates a dictionary of stats and info for a population"""
        most_fit = max(population, key=lambda x: x.fitness)
        least_fit = min(population, key=lambda x: x.fitness)
        return {
            'population': population,
            'most_fit': most_fit,
            'least_fit': least_fit,
            'max_fitness': most_fit.fitness,
            'avg_fitness': sum([organism.fitness for organism in population])/len(population),
            'min_fitness': least_fit.fitness
        }

    @classmethod
    def evolve(cls, population_size: int, generations: int, selection_function=ProportionalSelection(),
            crossover_rate: float=0.85, elite_rate: float=0, incel_rate: float=0, migration_rate: float=0,
            generational_callback=None) -> dict:
        """The magic method responsible for optimizing the traits using a Genetic Algorithm
        
        Args:
            population_size:
                The number of Organisms in each generations
            generations:
                How many generations of evolution should take place
            selection_function:
                A function discribing the way of selecting and breeding parents from the population
            crossover_rate: [0,1]
                The chance that two parents will crossover and add an offspring to the next generation
                (as opposed to being directly carried down to the next generation)
            elite_rate: [0,1]
                The top X percent of the population that will be directly carried down to the next generation
            incel_rate: [0,1]
                The lowest X percent of the population that will be removed from the parent pool
            migration_rate: [0,]
                Adds X percent of the population as random organisms to the parent pool
        """
        # the current collection of organisms
        population = []
        # data regarding each generation
        evolution_info = []

        for i in range(generations):
            # if the population is empty, populate it!
            if not population:
                population = [cls() for j in range(population_size)]
            else:
                # sort the population from highest to lowest fitness
                population.sort(key=lambda x: x.fitness, reverse=True)
                # the first 'elite_rate' percent of the list are elites (carried down to next generation)
                elites_end_index = math.floor(elite_rate*len(population))
                # the last 'incel_rate' percent of the list are incels (removed from the breeding pool lol)
                incel_start_index = math.floor((1-incel_rate)*len(population))
                # between the elites and the incels have a random chance of being carried down without crossover (dependent on crossover_rate)
                # this mask is false for each organism that does not undergo crossover
                crossover_mask = [random.random() < crossover_rate for i in range(incel_start_index-elites_end_index)]
                # migrated organisms are random organisms added to the parent pool to create diversity
                num_migrated_organisms = math.floor(migration_rate*len(population))

                elites = population[:elites_end_index]
                not_crossed_over = [population[i+elites_end_index] for i in range(incel_start_index-elites_end_index) if not crossover_mask[i]]
                migrated = [cls() for j in range(num_migrated_organisms)]
                # we need to evaluate the fitness for the migrated organisms so that they are properly chosen by selection_functions
                for organism in migrated:
                    organism.fitness = organism.evaluate()
                
                # elites and others chosen by crossover_rate are carried down directly to next generation
                new_population = elites + not_crossed_over

                # fill the rest of the population with new offspring
                parent_pool = population[:incel_start_index] + migrated
                num_offspring = len(population) - len(new_population)
                offspring = selection_function(parent_pool, num_offspring)

                new_population += offspring

                population = new_population

            # have each organsim cache it's fitness score to avoid inefficient redundant calls
            for organism in population:
                organism.fitness = organism.evaluate()

            info = cls.__generate_population_info(population)

            evolution_info.append(info)
            if generational_callback:
                generational_callback(info)
        
        return evolution_info
        

    def evaluate(self) -> float:
        """The function which determines the fitness of each Organism

        THIS METHOD MUST BE OVERWRITTEN BY ALL DERIVED CLASSES

        Args:
            None

        Returns:
            A numeric value representing a fitnes score (higher means more fit)
        """
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'evaluate' method")