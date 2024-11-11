"""
Created on 11/11/2024

"""

import matplotlib.pyplot as plt

def plot_graph(best_fitness_score, worst_fitness_score, time_to_solve):
    """
    Plot the graph of the best and worst fitness score
    :param best_fitness_score: (array) the best fitness score for each generation
    :param worst_fitness_score: (array) the worst fitness score for each generation
    """
    plt.figure(figsize=(8, 6), dpi=80)
    plt.plot(best_fitness_score, label='Best fitness score', color='pink', linewidth=2, linestyle='dashed')
    plt.plot(worst_fitness_score, label='Worst fitness score', color='blue', linewidth=2, linestyle='dashed')
    plt.xlabel('Number of generations')
    plt.ylabel('Fitness score')
    plt.ylim(0, worst_fitness_score[0])
    plt.xlim(0, len(best_fitness_score))
    # Time it took to solve the problem
    plt.title(f"Time it took to solve the problem: {time_to_solve} seconds")
    plt.legend()
    plt.show()