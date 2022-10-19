import random
from .basetrait import BaseTrait

class FloatTrait(BaseTrait):
    """A Trait whose value can be an floating point number

    initialize:
        Value initializes to a random floating point number from the provided range

    crossover:
        Returns the value from a single parent with equal chance

    mutate:
        If mutated, value gets set randomly to a random floating point number from the provided range
    """

    def __init__(self, min_value: float, max_value: float, mutation_rate: float=0.01):
        """
        Args:
            min_value: float
                The minimum the value could be
            max_value: float
                The maximum the value could be
            mutation_rate: float
                The chance of a value being mutated each generation        
        """
        self.min_value = min_value
        self.max_value = max_value
        self.mutation_rate = mutation_rate

    def random_value(self) -> float:
        return random.uniform(self.min_value, self.max_value)

    def crossover(self, a: float, b: float) -> float:
        return random.choice([a,b])

    def mutate(self, value: float) -> float:
        return self.random_value() if random.random()<self.mutation_rate else value