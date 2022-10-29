import random
from .basetrait import BaseTrait

class BinaryTrait(BaseTrait):
    """A Trait whose value can be either 0 or 1

    initialize:
        Value initializes to a 0 or 1 randomly with equal chance

    crossover:
        Returns the value from a single parent with equal chance

    mutation:
        If mutated, value gets set to 0 or 1 randomly with equal chance
    """

    def __init__(self, mutation_rate: float=0.05):
        """
        Args:
            mutation_rate: float
                The chance of a value being mutated each generation
        """
        self.mutation_rate = mutation_rate

    def random_value(self) -> int:
        return random.choice([0, 1])

    def crossover(self, a: int, b: int) -> int:
        return random.choice([a,b])

    def mutate(self, value: int) -> int:
        return self.random_value() if random.random()<self.mutation_rate else value
        