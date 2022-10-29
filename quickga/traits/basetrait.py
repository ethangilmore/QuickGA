from typing import TypeVar

T = TypeVar("T")

class BaseTrait:
    """A class to represent an adaptable trait possessed by an Organism

    This class contains the information for how traits are Initialized, Combined, and Mutated

    The methods random_value, crossover, and mutate MUST be overwritten
    The method initial_value may be overwritten when necessary
    """

    def from_parent_values(self, a: T, b: T) -> T:
        """Takes two values and creates a new derived value
        
        Args:
            a:
                The value from the first parent
            b:
                The value from the second parent
        """
        new_value = self.crossover(a, b)
        new_value = self.mutate(new_value)
        return new_value

    def inital_value(self) -> T:
        """Creates the initial value for the trait
        
        Returns:
            The initial value for the trait
        """

        return self.random_value()

    def random_value(self) -> T:
        """This method is responsible for creating a random value the trait could posess

        THIS METHOD MUST BE OVERWRITTEN
        
        Returns:
            A random value the trait could posess
        """

        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'random_value' method")

    def crossover(self, a: T, b: T) -> T:
        """This method is responsible for creating a new value for the trait derived from two parent values
        
        THIS METHOD MUST BE OVERWRITTEN
        
        Args:
            a:
                The value from the first parent
            b:
                The value from the second parent
        """

        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'crossover' method")

    def mutate(self, value: T) -> T:
        """This method is responsible for creating a possibly mutated variation of a traits value

        Note that this method is called every time a trait is passed down
        It is this methods responsibility to calculate and implement mutation rates
        
        THIS METHOD MUST BE OVERWRITTEN
        
        Args:
            value:
                The value to be possibly mutated
        
        Returns:
            The possibly mutated variation of the value
        """

        raise Exception(f"The Class '{self.__class__.__name__}' has not implemented 'mutate' method")