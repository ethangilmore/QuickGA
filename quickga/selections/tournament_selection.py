import random
from select import select
from .selection_function_factory import SelectionFunctionFactory

class TournamentSelection(SelectionFunctionFactory):

    def __init__(self, sample_size: int, unique_parents: bool=False):
        self.sample_size = sample_size
        self.enforces_unique_parents = unique_parents

    def select_parent(self, population, exclude):
        tournament = []

        # the number of organisms in the tournament should be equal to the sample size
        while len(tournament) < self.sample_size:
            chosen_for_tournament = random.choice(population)
            # checks that the chosen organism is not already in the tournament
            while chosen_for_tournament in tournament:
                chosen_for_tournament = random.choice(population)
            tournament.append(chosen_for_tournament)
        # return the most fit of those randomly chosen for the tournament

        return max(tournament, key=lambda x: x.fitness)

    def selection_function(self, population):
        if len(population) < self.sample_size:
            raise Exception("Population size cannot be less than sample size for Tournament Selection")

        parent_pairs = []
        # because each parent group creates one child, the number of parent groups should be equal to the population
        while len(parent_pairs) < len(population):
            new_parent_pair = [self.select_parent(population), self.select_parent(population)]
            # if we require unique parents but they are the same, keep replacing one parent until it is different
            while self.enforces_unique_parents and new_parent_pair[0] == new_parent_pair[1]:
                new_parent_pair = self.select_parent(population)
            parent_pairs.append(new_parent_pair)

        return parent_pairs
            
