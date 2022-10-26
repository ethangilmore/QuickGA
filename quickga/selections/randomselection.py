import random
from .selectionfunctionfactory import SelectionFunctionFactory

class RandomSelection(SelectionFunctionFactory):
    def __init__(self, unique_parents: bool=False):
        self.enforces_unique_parents = unique_parents

    def selection_function(self, parent_pool, num_offspring):
        parent_pairs = []
        select_parent = lambda : random.choice(parent_pool)

        for i in range(num_offspring):
            new_parent_group = [select_parent(), select_parent()]
            # if we require unique parents but they are the same, keep replacing one parent until it is different
            while self.enforces_unique_parents and new_parent_group[0] == new_parent_group[1]:
                new_parent_group[1] = select_parent()
            parent_pairs.append(new_parent_group)

        return [pair[0] + pair[1] for pair in parent_pairs]