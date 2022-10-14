from typing import TypeVar

T = TypeVar("T")

class BaseTrait:

    def random_value(self) -> T:
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'random_value' method")

    def crossover(self, a: T, b: T) -> T:
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'crossover' method")

    def mutate(self, value: T) -> T:
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'mutate' method")