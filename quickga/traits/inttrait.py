import random
from traits import BaseTrait

class IntTrait(BaseTrait):

    def __init__(self, min_value: int, max_value: int, mutation_rate: float=0.01):
        self.min_value = min_value
        self.max_value = max_value
        self.mutation_rate = mutation_rate

    def random_value(self) -> int:
        return random.randint(self.min_value, self.max_value)

    def crossover(self, a: int, b: int) -> int:
        return a if random.random() < .5 else b

    def mutate(self, value: int) -> int:
        if random.random() < self.mutation_rate:
            return self.random_value()
        return value