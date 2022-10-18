import random
from .basetrait import BaseTrait

class FloatTrait(BaseTrait):

    def __init__(self, min_value: float, max_value: float, mutation_rate: float=0.01):
        self.min_value = min_value
        self.max_value = max_value
        self.mutation_rate = mutation_rate

    def random_value(self) -> float:
        return random.uniform(self.min_value, self.max_value)

    def crossover(self, a: float, b: float) -> float:
        return random.choice([a,b])

    def mutate(self, value: float) -> float:
        return self.random_value() if random.random()<self.mutation_rate else value