import random
from select import select
from .selectionfunctionfactory import SelectionFunctionFactory

class TournamentSelection(SelectionFunctionFactory):

    def __init__(self, sample_size: int, unique_parents: bool=False):
        self.sample_size = sample_size
        self.enforces_unique_parents = unique_parents

    def select_parent(self, parent_pool: list):
        tournament = []

        # the number of organisms in the tournament should be equal to the sample size
        while len(tournament) < self.sample_size:
            chosen_for_tournament = random.choice(parent_pool)
            # checks that the chosen organism is not already in the tournament
            while chosen_for_tournament in tournament:
                chosen_for_tournament = random.choice(parent_pool)
            tournament.append(chosen_for_tournament)
        # return the most fit of those randomly chosen for the tournament

        return max(tournament, key=lambda x: x.fitness)

    def selection_function(self, parent_pool: list, num_offspring: int):
        if len(parent_pool) < self.sample_size:
            raise Exception("Population size cannot be less than sample size for Tournament Selection")

        parent_pairs = []
        for i in range(num_offspring):
            new_parent_pair = [self.select_parent(parent_pool), self.select_parent(parent_pool)]
            # if we require unique parents but they are the same, keep replacing one parent until it is different
            while self.enforces_unique_parents and new_parent_pair[0] == new_parent_pair[1]:
                new_parent_pair = self.select_parent(parent_pool)
            parent_pairs.append(new_parent_pair)

        return [pair[0] + pair[1] for pair in parent_pairs]
            
