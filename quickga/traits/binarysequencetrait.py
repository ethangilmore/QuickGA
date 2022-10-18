from .sequencetrait import SequenceTrait
from .binarytrait import BinaryTrait

class BinarySequenceTrait(SequenceTrait):
    def __init__(self, length: int, crossover_type: str, mutation_type: str, mutation_rate: float=0.05, n: int=None):
        super().__init__(BinaryTrait(mutation_rate=0), length, crossover_type, mutation_type, mutation_rate, n) 