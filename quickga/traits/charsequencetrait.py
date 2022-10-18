from .sequencetrait import SequenceTrait
from .chartrait import CharTrait

class CharSequenceTrait(SequenceTrait):
    def __init__(self, include, length: int, crossover_type: str, mutation_type: str, mutation_rate: float=0.05, n: int=None):
        super().__init__(CharTrait(include, mutation_rate=0), length, crossover_type, mutation_type, mutation_rate, n) 