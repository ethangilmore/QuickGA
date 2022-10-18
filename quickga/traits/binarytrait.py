import random
from .basetrait import BaseTrait

class BinaryTrait(BaseTrait):
    def __init__(self, mutation_rate: float=0.05):
        self.mutation_rate = mutation_rate

    def random_value(self):
        return random.choice([0, 1])

    def crossover(self, a, b):
        return random.choice([a,b])

    def mutate(self, value):
        return self.random_value() if random.random()<self.mutation_rate else value
        