class Organism:

    def __init__(self):
        self.fitness = 0
        self._traits = {}

    def __add__(self, other):
        raise NotImplementedError()

    @staticmethod
    def evolve(population_size, generations, selection_function):
        raise NotImplementedError()