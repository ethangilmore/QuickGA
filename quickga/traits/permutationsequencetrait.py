import random
from .sequencetrait import SequenceTrait

class PermutationSequenceTrait(SequenceTrait):
    def __init__(self, elements, crossover_type: str='partially-mapped', mutation_type: str='scramble', mutation_rate: float=0.05):
        self.elements = [e for e in elements]
        self.crossover_type = crossover_type
        self.mutation_type = mutation_type
        self.mutation_rate = mutation_rate

        self.crossover_functions = {
            'partially-mapped': self.partially_mapped_crossover,
        }

        self.mutation_functions = {
            'swap': self.swap_mutation,
            'insertion': self.insertion_mutation,
            'scramble': self.scramble_mutation,
            'inversion': self.inversion_mutation
        }

        if crossover_type not in self.crossover_functions:
            raise Exception("Invalid crossover type provided")
        if mutation_type not in self.mutation_functions:
            raise Exception("Invalid mutation type provided")

    def map_index(self, index: int, a: list, b: list, region_start: int, region_end: int) -> int:
        map_index = lambda index : a.index(b[index])
        i = index
        while region_start <= i and i < region_end:
            i = map_index(i)
        return i

    def partially_mapped_crossover(self, a: list, b: list) -> list:
        c = [None for i in range(len(a))]
        i1, i2 = self.random_unique_index_pair(a)
        start_index = min(i1, i2)
        end_index = max(i1, i2)
        
        # copy down segment from first parent
        c[start_index:end_index] = a[start_index:end_index]
        # map values from second parent
        for i, value in enumerate(b[start_index:end_index]):
            if value in c[start_index:end_index]:
                continue
            mapped_index = self.map_index(i+start_index, b, a, start_index, end_index)
            c[mapped_index] = value
        # copy all other values from second parent
        for i, value in enumerate(c):
            if value is None:
                c[i] = b[i]

        return c


    def random_value(self) -> list:
        random.shuffle(self.elements)
        return self.elements