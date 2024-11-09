"""
Created on 08/11/2024

"""
import argparse

from classes.sudoku_ga import SudokuGA

if __name__ == '__main__':
    # Handle mandatory arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-ps', '--population-size', required=True, type=int,
                        help="Size of populations that will be generated")
    parser.add_argument('-sr', '--selection-rate', required=True, type=float,
                        help="Rate of the best elements to keep from one generation to be part of the next breeders")
    parser.add_argument('-rsr', '--random-selection-rate', required=True, type=float,
                        help="Rate of the population which is randomly selected to be part of the next breeders")
    parser.add_argument('-c', '--children', required=True, type=int,
                        help="How many children do we generate from 2 individuals")
    parser.add_argument('-mr', '--mutation-rate', required=True, type=float,
                        help="Part of the population that will go through mutation (avoid eugenics)")
    parser.add_argument('-g', '--max-generations', required=True, type=int,
                        help="Max number of generations to generate")
    parser.add_argument('-m', '--model', required=True,
                        help="Model to solve: name of the .txt file which should be under 'samples' directory")
    parser.add_argument('-r', '--restart-nb-generations', required=True, type=int,
                        help="Restart if there is no improvement on fitness value for best element after this number of"
                             " generations")
    args = parser.parse_args()

    population_size = vars(args)['population_size']
    selection_rate = vars(args)['selection_rate']
    random_selection_rate = vars(args)['random_selection_rate']
    nb_children = vars(args)['children']
    mutation_rate = vars(args)['mutation_rate']
    max_nb_generations = vars(args)['max_generations']
    model_to_solve = vars(args)['model']
    restart_after_n_generations_without_improvement = vars(args)['restart_nb_generations']

    sga = SudokuGA(population_size, selection_rate, random_selection_rate, nb_children, max_nb_generations,
                   mutation_rate, model_to_solve, restart_after_n_generations_without_improvement)
    sga.run()