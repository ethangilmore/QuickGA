import random
from .basetrait import BaseTrait

class IntTrait(BaseTrait):

    def __init__(self, min_value: int, max_value: int, mutation_rate: float=0.01):
        self.min_value = min_value
        self.max_value = max_value
        self.mutation_rate = mutation_rate

    def random_value(self) -> int:
        return random.randint(self.min_value, self.max_value)

    def crossover(self, a: int, b: int) -> int:
        return random.choice([a,b])

    def mutate(self, value: int) -> int:
        return self.random_value() if random.random()<self.mutation_rate else value