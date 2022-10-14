from typing import TypeVar

T = TypeVar("T")

class BaseTrait:

    def from_parent_values(self, a: T, b: T) -> T:
        new_value = self.crossover(a, b)
        new_value = self.mutate(new_value)
        return new_value

    def inital_value(self) -> T:
        return self.random_value()

    def random_value(self) -> T:
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'random_value' method")

    def crossover(self, a: T, b: T) -> T:
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'crossover' method")

    def mutate(self, value: T) -> T:
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'mutate' method")