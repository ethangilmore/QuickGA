from .selection_function_factory import SelectionFunctionFactory
import random

class ProportionalSelection(SelectionFunctionFactory):

    def __init__(self, unique_parents: bool=False):
        self.enforces_unique_parents = unique_parents

    def select_parent_index(self, fitnesses, total_fitness):
        current_sum = 0
        stop = random.uniform(0,total_fitness)
        for i in range(len(fitnesses)):
            current_sum += fitnesses[i]
            if current_sum >= stop:
                return i

    def selection_function(self, population):
        parent_groups = []
        # cache the fitnesses and total_fitness so that we don't need to recalculate every time a parent is selected
        fitnesses = [organism.fitness for organism in population]
        total_fitness = sum(fitnesses)
        # basically creates new function 'select_parent' using the 'select_parent_index' method and the two values cached above
        select_parent = lambda: population[self.select_parent_index(fitnesses, total_fitness)]

        # because each parent group creates one child, the number of parent groups should be equal to the population
        while len(parent_groups) < len(population):
            new_parent_group = [select_parent(), select_parent()]
            # if we require unique parents but they are the same, keep replacing one parent until it is different
            while self.enforces_unique_parents and new_parent_group[0] == new_parent_group[1]:
                new_parent_group[1] = select_parent()
            parent_groups.append(new_parent_group)

        return parent_groups

