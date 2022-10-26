from .selectionfunctionfactory import SelectionFunctionFactory
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

    def selection_function(self, parent_pool, num_offspring):
        parent_pairs = []
        # cache the fitnesses and total_fitness so that we don't need to recalculate every time a parent is selected
        fitnesses = [organism.fitness for organism in parent_pool]
        total_fitness = sum(fitnesses)
        # basically creates new function 'select_parent' using the 'select_parent_index' method and the two values cached above
        select_parent = lambda: parent_pool[self.select_parent_index(fitnesses, total_fitness)]

        for i in range(num_offspring):
            new_parent_group = [select_parent(), select_parent()]
            # if we require unique parents but they are the same, keep replacing one parent until it is different
            while self.enforces_unique_parents and new_parent_group[0] == new_parent_group[1]:
                new_parent_group[1] = select_parent()
            parent_pairs.append(new_parent_group)

        return [pair[0] + pair[1] for pair in parent_pairs]

