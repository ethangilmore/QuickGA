import random
from .selectionfunctionfactory import SelectionFunctionFactory

class RankSelection(SelectionFunctionFactory):
    def __init__(self, unique_parents: bool = False):
        self.enforces_unique_parents = unique_parents

    def select_parent_index(self, ranks: list, rank_sum: int) -> int:
        current_sum = 0
        stop = random.uniform(0,rank_sum)
        for i in range(len(ranks)):
            current_sum += ranks[i]
            if current_sum >= stop:
                return i

    def selection_function(self, parent_pool: list, num_offspring: int) -> int:
        parent_pairs = []

        parent_pool.sort(key=lambda x: x.fitness)
        ranks = [i+1 for i in range(len(parent_pool))]
        rank_sum = (ranks[-1]-ranks[0]+1)*(ranks[0]+ranks[-1])/2

        select_parent = lambda: parent_pool[self.select_parent_index(ranks, rank_sum)]

        for i in range(num_offspring):
            new_parent_group = [select_parent(), select_parent()]
            # if we require unique parents but they are the same, keep replacing one parent until it is different
            while self.enforces_unique_parents and new_parent_group[0] == new_parent_group[1]:
                new_parent_group[1] = select_parent()
            parent_pairs.append(new_parent_group)

        return [pair[0] + pair[1] for pair in parent_pairs]
        
