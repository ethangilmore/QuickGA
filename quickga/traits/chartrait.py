import random
import string
from .basetrait import BaseTrait

class CharTrait(BaseTrait):
    def __init__(self, include = ['lowercase', 'uppercase'], mutation_rate: float=0.05):
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
