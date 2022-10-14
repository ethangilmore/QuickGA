from typing import Dict
from quickga.traits.basetrait import BaseTrait


class Organism:

    def __init__(self):
        self._traits = {}
        self.fitness = 0

    def __add__(self, other):
        return self.breed(other)

    def breed(self, other):
        if type(other) is not type(self):
            raise Exception(f"Addition operation not supported for types {self.__class__.__name__} and {other.__class__.__name__}")
        
        child = self.__class__()

        child_vars = vars(child)
        parent1_vars = vars(self)
        parent2_vars = vars(other)

        for trait_name in self._traits:
            trait_obj = self._traits[trait_name]
            child_vars[trait_name] = trait_obj.from_parent_values(parent1_vars[trait_name], parent2_vars[trait_name])

        return child

    def add_trait(self, variable_name: str, trait: BaseTrait) -> None:
        self._traits[variable_name] = trait
        vars(self)[variable_name] = trait.inital_value()

    def remove_trait(self, variable_name: str) -> None:
        self._traits.pop(variable_name)
        vars(self).pop(variable_name)

    def set_traits(self, traits: Dict[str, BaseTrait]) -> None:
        self._traits.clear()
        for trait_name, trait in traits.items:
            self.add_trait(trait_name, trait)

    @staticmethod
    def evolve(population_size: int, generations: int, selection_function) -> Dict:
        raise NotImplementedError()

    def evaluate(self) -> float:
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'evaluate' method")