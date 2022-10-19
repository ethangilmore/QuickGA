from .sequencetrait import SequenceTrait
from .chartrait import CharTrait

class CharSequenceTrait(SequenceTrait):
    """A Trait whose value is a List (or "Sequence") of the ASCII characters

    initialize:
        Value initializes to a list of ASCII characters

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

    def __init__(self, length: int, include = ['lowercase', 'uppercase'], crossover_type: str='2-point',
            mutation_type: str='random-reset', mutation_rate: float=0.05, n: int=None):
        """
        Args:
            length: int
                How long the sequence should be
            include: list
                a list which may contain the values ['lowercase', 'uppercase', 'punctuation'] and decides the characters the value can have
            crossover_type: str
                One of ['uniform', '1-point', '2-point', 'n-point']
            mutation_type: str
                One of ['random-reset', 'swap', 'inseriton', 'scramble', 'inversion']
            mutaion_type: float
                The chance of a value being mutated each generation
            n: int
                If the user selects the crossover type 'n-point' the n should be specified with this argument
        """

        super().__init__(CharTrait(include, mutation_rate=0), length, crossover_type, mutation_type, mutation_rate, n) 