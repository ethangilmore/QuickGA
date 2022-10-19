import random
import string
from .basetrait import BaseTrait

class CharTrait(BaseTrait):
    """A Trait whose value can be an ASCII character

    initialize:
        Value initializes to a random character from the included characters with equal chance

    crossover:
        Returns the value from a single parent with equal chance

    mutate:
        If mutated, value gets set randomly to any included character with equal chance
    """

    def __init__(self, include = ['lowercase', 'uppercase'], mutation_rate: float=0.05):
        """
        Args:
            include: list
                a list which may contain the values ['lowercase', 'uppercase', 'punctuation'] and decides the characters the value can have
            mutation_rate: float
                The chance of a value being mutated each generation
        """
        self.char_pool = []
        if 'lowercase' in include:
            self.char_pool += string.ascii_lowercase
        if 'uppercase' in include:
            self.char_pool += string.ascii_uppercase
        if 'punctuation' in include:
            self.char_pool += string.punctuation
        
    def random_value(self):
        return random.choice(self.char_pool)

    def crossover(self, a, b):
        return random.choice([a,b])

    def mutate(self, value):
        return self.random_value() if random.random()<self.mutation_rate else value
