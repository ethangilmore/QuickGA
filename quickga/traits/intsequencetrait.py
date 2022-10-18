from .sequencetrait import SequenceTrait
from .inttrait import IntTrait

class IntSequenceTrait(SequenceTrait):
    def __init__(self, min_value: int, max_value: int, length: int, 
            crossover_type: str, mutation_type: str, mutation_rate: float=0.05, n: int=None):
        super().__init__(IntTrait(min_value, max_value, mutation_rate=0), length, crossover_type, mutation_type, mutation_rate, n) 