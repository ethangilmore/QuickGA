import random
from typing import Tuple
from .basetrait import BaseTrait

class SequenceTrait(BaseTrait):

    def __init__(self, trait, length: int, crossover_type: str, mutation_type: str, mutation_rate: float=0.05, n: int=None):
        """
        Args:
            trait: Trait
                The trait which defines the values in the sequence
            length: int
                How long the sequence should be
            crossover_type: str
                One of ['uniform', '1-point', '2-point', 'n-point']
            mutation_type: str
                One of ['random-reset', 'swap', 'inseriton', 'scramble', 'inversion']
            mutaion_type: float
                The chance of a value being mutated each generation
            n: int
                If the user selects the crossover type 'n-point' the n should be specified with this argument
        """

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
            raise Exception("Invalid crossover type provided")
        if mutation_type not in self.mutation_functions:
            raise Exception("Invalid mutation type provided")

    """A Trait whose value is a List (or "Sequence") of the values of another Trait

    initialize:
        Value initializes to a list of values defined by the provided Trait's initial value

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

    def random_unique_index_pair(self, items: list) -> Tuple[int, int]:
        """Returns two unique indices for a list"""
        index_a = random.randint(0,len(items)-1)
        index_b = random.randint(0,len(items)-2)
        index_b += 1 if index_b >= index_a else 0
        return index_a, index_b

    def uniform_crossover(self, a: list, b: list) -> list:
        """For each value in the child sequence, it is chosen from one of the parents at random
        
        example:
            a = [0,0,0,0,0,0,0,0,0,0]
            b = [1,1,1,1,1,1,1,1,1,1]
            c = [0,1,1,0,0,1,0,0,1,1]

        Args:
            a: list
                Sequence from one parent
            b: list
                Sequence form other parent

        Returns:
            A new list made from the crossover of the two parent lists
        """
        return [a[i] if random.random()<.5 else b[i] for i in range(len(a))]

    def one_point_crossover(self, a: list, b: list) -> list:
        """Chooses one point in the childs sequence, values before will be inherited from one parent, values after from the other parent
        
        example:
            a = [0,0,0,0,0,0,0,0,0,0]
            b = [1,1,1,1,1,1,1,1,1,1]
            c = [0,0,0,0,1,1,1,1,1,1]

        Args:
            a: list
                Sequence from one parent
            b: list
                Sequence form other parent

        Returns:
            A new list made from the crossover of the two parent lists
        """
        self.n = 1
        return self.n_point_crossover(a, b)

    def two_point_crossover(self, a: list, b: list) -> list:
        """Chooses two points in the childs sequence, values between points will be inherited from one parent, other values from the other parent
        
        example:
            a = [0,0,0,0,0,0,0,0,0,0]
            b = [1,1,1,1,1,1,1,1,1,1]
            c = [0,0,0,0,1,1,1,1,0,0]

        Args:
            a: list
                Sequence from one parent
            b: list
                Sequence form other parent

        Returns:
            A new list made from the crossover of the two parent lists
        """
        self.n = 2
        return self.n_point_crossover(a, b)

    def n_point_crossover(self, a: list, b: list) -> list:
        """N-point crossover for however many points specified
        
        example: n = 3
            a = [0,0,0,0,0,0,0,0,0,0]
            b = [1,1,1,1,1,1,1,1,1,1]
            c = [0,0,1,1,1,0,0,0,1,1]

        Args:
            a: list
                Sequence from one parent
            b: list
                Sequence form other parent

        Returns:
            A new list made from the crossover of the two parent lists
        """
        if not self.n:
            raise Exception("No n defined for n-point crossover")
        
        indices = [i for i in range(1, len(a)-1)]
        cross_indices = [indices.pop(random.randint(0,len(indices)-1)) for i in range(self.n)]
        
        new_sequence = []
        pick_from_a = random.random()<.5
        for i in range(len(a)):
            new_sequence.append(a[i] if pick_from_a else b[i])
            if i in cross_indices:
                pick_from_a = not pick_from_a

        return new_sequence


    def random_reset_mutation(self, value: list) -> list:
        """Randomly resets a value in the sequence

        Example:
            value = [0,1,2,3,4,5,6,7,8,9]
            value = [0,1,2,9,4,5,6,7,8,9]
                           ^
        Args:
            value: list
                The sequence to be mutated

        Returns:
            The mutated sequence
        """

        random_index = random.randint(0,len(value)-1)
        value[random_index] = self.trait.random_value()

        return value

    def insertion_mutation(self, value: list) -> list:
        """Randomly moves one value to another index in the array, shifts all other values

        Example:
            value = [0,1,2,3,4,5,6,7,8,9]
            value = [0,1,2,9,3,4,5,6,7,8]
                           ^ ^ ^ ^ ^ ^ ^ 
        Args:
            value: list
                The sequence to be mutated

        Returns:
            The mutated sequence
        """

        remove_index, insert_index = self.random_unique_index_pair(value)
        temp = value.pop(remove_index)
        value.insert(insert_index, temp)

        return value

    def swap_mutation(self, value: list) -> list:
        """Randomly swaps two values in the sequence

        Example:
            value = [0,1,2,3,4,5,6,7,8,9]
            value = [0,1,2,9,4,5,6,7,8,3]
                           ^           ^
        Args:
            value: list
                The sequence to be mutated

        Returns:
            The mutated sequence
        """

        index_a, index_b = self.random_unique_index_pair(value)

        temp = value[index_a]
        value[index_a] = value[index_b]
        value[index_b] = temp

        return value

    def scramble_mutation(self, value: list) -> list:
        """Randomly scrambles a section in the sequence

        Example:
            value = [0,1,2,3,4,5,6,7,8,9]
            value = [0,1,2,5,7,3,9,6,8,9]
                           ^ ^ ^ ^ ^
        Args:
            value: list
                The sequence to be mutated

        Returns:
            The mutated sequence
        """

        index_a, index_b = self.random_unique_index_pair(value)
        scramble_section = value[index_a:index_b]
        random.shuffle(scramble_section)
        value[index_a:index_b] = scramble_section

        return value

    def inversion_mutation(self, value: list) -> list:
        """Randomly reverses a section in the sequence

        Example:
            value = [0,1,2,3,4,5,6,7,8,9]
            value = [0,1,2,7,6,5,4,3,8,9]
                           ^ ^ ^ ^ ^

        Args:
            value: list
                The sequence to be mutated

        Returns:
            The mutated sequence
        """

        index_a, index_b = self.random_unique_index_pair(value)
        invert_section = value[index_a:index_b]
        invert_section.reverse()
        value[index_a:index_b] = invert_section

        return value

    def initial_value(self) -> list:
        return [self.trait.initial_value() for i in range(self.length)]

    def random_value(self) -> list:
        return [self.trait.random_value() for i in range(self.length)]

    def crossover(self, a: list, b: list) -> list:
        return self.crossover_functions[self.crossover_type](a, b)

    def mutate(self, value: list) -> list:
        if random.random() < self.mutation_rate:
            return self.mutation_functions[self.mutation_type](value)
        return value
