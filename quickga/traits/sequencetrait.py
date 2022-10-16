import random
from .basetrait import BaseTrait

class SequenceTrait(BaseTrait):

    def uniform_crossover(self, a, b):
        return [a[i] if random.random()<.5 else b[i] for i in range(len(a))]

    def one_point_crossover(self, a, b):
        self.n = 1
        return self.n_point_crossover(a, b)

    def two_point_crossover(self, a, b):
        self.n = 2
        return self.n_point_crossover(a, b)

    def n_point_crossover(self, a, b):
        if not self.n:
            raise Exception("No n defined for n-point crossover")
        
        indices = [i for i in range(len(a))]
        cross_indices = [indices.pop(random.randint(0,len(indices)-1)) for i in range(self.n)]
        
        new_sequence = []
        pick_from_a = random.random()<.5
        for i in range(len(a)):
            new_sequence += a[i] if pick_from_a else b[i]
            if i in cross_indices:
                pick_from_a = not pick_from_a

        return new_sequence


    def random_reset_mutation(self, value):
        pass

    def swap_mutation(self, value):
        pass

    def insertion_mutation(self, value):
        pass

    def scramble_mutation(self, value):
        pass

    def inversion_mutation(self, value):
        pass


    def __init__(self, trait, length: int, crossover_type: str, mutation_type: str, mutation_rate: float, n: int=None):
        self.trait = trait
        self.length = length
        self.crossover_type = crossover_type
        self.mutation_type = mutation_type
        self.mutation_rate = mutation_rate
        self.n = n

        self.crossover_functions = {
            'uniform': self.uniform_crossover,
            '1-point': self.one_point_crossover,
            '2-point': self.two_point_crossover,
            'n-point': self.n_point_crossover
        }

        self.mutation_functions = {
            'random-reset': self.random_reset_mutation,
            'swap': self.swap_mutation,
            'insertion': self.insertion_mutation,
            'scramble': self.scramble_mutation,
            'inversion': self.inversion_mutation
        }

        if crossover_type not in self.crossover_functions:
            raise Exception("Invalid crossover_type provided")
        if mutation_type not in self.mutation_functions:
            raise Exception("Invalid mutation_type provided")

    def initial_value(self):
        return [self.trait.initial_value() for i in range(self.length)]

    def random_value(self):
        return [self.trait.random_value() for i in range(self.length)]

    def crossover(self, a, b):
        return self.crossover_functions[self.crossover_type](a, b)

    def mutate(self, value):
        if random.random() < self.mutation_rate:
            return self.mutation_functions[self.mutation_type](value)
        return random
