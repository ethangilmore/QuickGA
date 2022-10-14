class BaseTrait:

    def __add__(self, other):
        raise NotImplementedError()

    def random_value(self):
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'random_value' method")

    def crossover(self, a, b):
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'crossover' method")

    def mutate(self, value):
        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'mutate' method")