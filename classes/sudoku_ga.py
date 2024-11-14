"""
Created on: 08/11/2024

"""

from time import time

from classes.sudoku import Sudoku
from sudoku_utils import ga_utils
from general_utils import file_loader, tools, graph

class SudokuGA(object):
    _population_size = None
    _selection_rate = None
    _random_selection_rate = None
    _nb_children = None
    _max_nb_generations = None
    _mutation_rate = None
    _model_to_solve = None
    _presolving = None
    _restart_after_n_generations_without_improvement = None
    _start_time = None

    def __init__(self, population_size, selection_rate, random_selection_rate, nb_children, max_nb_generations,
                 mutation_rate, model_to_solve, restart_after_n_generations_without_improvement):
        """
        :param population_size: (int) the whole population size to generate for each generation
        :param selection_rate: (float) elitism parameter: rate of the best elements to keep from one generation to be
        part of the next breeders
        :param random_selection_rate: (float) part of the population which is randomly selected to be part of the next
        breeders
        :param nb_children: (int) how many children do we generate from 2 individuals
        :param max_nb_generations: (int) maximum number of generations to generate. If a solution is found before, it is
        displayed, otherwise the best solution (but not THE solution) is displayed
        :param mutation_rate: (float) part of the population that will go through mutation (avoid eugenics)
        :param model_to_solve: (string) name of the .txt file which should be under 'samples' directory and contains the
        objects problem to solve
        :param restart_after_n_generations_without_improvement: (int) if > 0, the program will automatically restart if
        there is no improvement on fitness value for best element after this number of generations
        """
        self._population_size = population_size
        self._selection_rate = selection_rate
        self._random_selection_rate = random_selection_rate
        self._nb_children = nb_children
        self._max_nb_generations = max_nb_generations
        self._mutation_rate = mutation_rate
        self._model_to_solve = model_to_solve
        self._restart_after_n_generations_without_improvement = restart_after_n_generations_without_improvement

    def run(self):
        """
        Start the GA to solve the objects
        """
        values_to_set = self._load().get_initial_values()

        best_data = []
        worst_data = []
        found = False
        overall_nb_generations_done = 0
        restart_counter = 0

        while overall_nb_generations_done < self._max_nb_generations and not found:
            new_population = ga_utils.create_population(self._population_size, values_to_set)

            nb_generations_done = 0
            remember_the_best = 0
            nb_generations_without_improvement = 0

            # Loop until max allowed generations is reached or a solution is found
            while nb_generations_done < self._max_nb_generations and not found:
                # Rank the solutions
                ranked_population = ga_utils.rank_population(new_population)
                best_solution = ranked_population[0]
                best_score = best_solution.fitness()
                worst_score = ranked_population[-1].fitness()
                best_data.append(best_score)
                worst_data.append(worst_score)

                # Manage best value and improvements among new generations over time
                if remember_the_best == best_score:
                    nb_generations_without_improvement += 1
                else:
                    remember_the_best = best_score
                if 0 < self._restart_after_n_generations_without_improvement < nb_generations_without_improvement:
                    print("No improvement since {} generations, restarting the program".
                          format(self._restart_after_n_generations_without_improvement))
                    restart_counter += 1
                    break

                # Check if Sudoku is solved and print best and worst results
                if best_score > 0:
                    print("Sudoku not solved on generation {} (restarted {} times). Best fitness score is {} and "
                          "worst is {}".format(nb_generations_done, restart_counter, best_score, worst_score))
                    # Not solved => select a new generation among this ranked population
                    # Retain only the percentage specified by selection rate
                    next_breeders = ga_utils.pick_from_population(ranked_population, self._selection_rate,
                                                                  self._random_selection_rate)

                    children = ga_utils.create_children_random_parents(next_breeders, self._nb_children)
                    new_population = ga_utils.mutate_population(children, self._mutation_rate)

                    nb_generations_done += 1
                    overall_nb_generations_done += 1
                else:
                    print("Sudoku solved after {} generations ({} overall generations)!!! Solution found is:".
                          format(nb_generations_done, overall_nb_generations_done))
                    best_solution.display()
                    found = True
                    print("It took {} to solve it".format(tools.get_readable_time(self._start_time, time())))

        if not found:
            print("Sudoku not solved after {} generations. Printing best and worst results below".
                  format(overall_nb_generations_done))
            ranked_population = ga_utils.rank_population(new_population)
            best_solution = ranked_population[0]
            worst_solution = ranked_population[-1]
            print("Best is:")
            best_solution.display()
            print("Worst is:")
            worst_solution.display()
        
        graph.plot_graph(best_data, worst_data, tools.get_readable_time(self._start_time, time()))


    def _load(self):
        """
        Load the file, performs some sanity checks
        :return: (object) the sudoku puzzle to use
        """
        if ((self._selection_rate + self._random_selection_rate) / 2) * self._nb_children != 1:
            raise Exception("Either the selection rate, random selection rate or the number of children is not "
                            "well adapted to fit the population")

        values_to_set = file_loader.load_file_as_values(self._model_to_solve)
        zeros_to_count = '0' if len(values_to_set) < 82 else '00'   # In case when cells has a number with 2 digits
        print("The given {}x{} sudoku board is: (# of values to find = {})".format(int(len(values_to_set) ** 0.5), int(len(values_to_set) ** 0.5),values_to_set.count(zeros_to_count)))
        
        self._start_time = time()
        s = Sudoku(values_to_set)
        s.display()

        return s