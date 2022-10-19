from .sequencetrait import SequenceTrait
from .inttrait import IntTrait

class IntSequenceTrait(SequenceTrait):
    """A Trait whose value is a List (or "Sequence") of the integer numbers

    initialize:
        Value initializes to a list of integer numbers

    crossover:
        Currently implemented crossover methods include
            - 1-point crossover
            - 2-point crossover
            - n-point crossover
            - uniform crossover

    mutate:
        Currently implemented mutation methods include
            - random-reset mutation
            - insertion mutation
            - swap mutation
            - scramble mutation
            - inversion mutation

        If mutated, value gets set mutated according to the method specified in the constructor
    """

    def __init__(self, length: int, min_value: int, max_value: int, crossover_type: str='2-point', 
            mutation_type: str='random-reset', mutation_rate: float=0.05, n: int=None):
        """
        Args:
            length: int
                How long the sequence should be
            min_value: int
                The minimum a value in the sequence could be
            max_value: int
                The maximum a value in the sequence could be
            crossover_type: str
                One of ['uniform', '1-point', '2-point', 'n-point']
            mutation_type: str
                One of ['random-reset', 'swap', 'inseriton', 'scramble', 'inversion']
            mutaion_type: float
                The chance of a value being mutated each generation
            n: int
                If the user selects the crossover type 'n-point' the n should be specified with this argument
        """
        super().__init__(IntTrait(min_value, max_value, mutation_rate=0), length, crossover_type, mutation_type, mutation_rate, n) 