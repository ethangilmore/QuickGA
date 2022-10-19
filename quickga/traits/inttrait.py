import random
from .basetrait import BaseTrait

class IntTrait(BaseTrait):
    """A Trait whose value can be an integer number

    initialize:
        Value initializes to a random integer number from the provided range

    crossover:
        Returns the value from a single parent with equal chance

    mutate:
        If mutated, value gets set randomly to a random integer number from the provided range
    """

    def __init__(self, min_value: int, max_value: int, mutation_rate: float=0.01):
        """
        Args:
            min_value: int
                The minimum the value could be
            max_value: int
                The maximum the value could be
            mutation_rate: float
                The chance of a value being mutated each generation        
        """
        self.min_value = min_value
        self.max_value = max_value
        self.mutation_rate = mutation_rate

    def random_value(self) -> int:
        return random.randint(self.min_value, self.max_value)

    def crossover(self, a: int, b: int) -> int:
        return random.choice([a,b])

    def mutate(self, value: int) -> int:
        return self.random_value() if random.random()<self.mutation_rate else value