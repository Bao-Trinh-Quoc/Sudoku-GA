# Sudoku Solver using Genetic Algorithm

This project implements a Sudoku solver using a Genetic Algorithm (GA). The GA is an optimization technique inspired by the process of natural selection, and it is used here to find solutions to Sudoku puzzles.


## Usage

To run the Sudoku solver, use the following command:

```sh
python3 main.py --population-size 10000 --selection-rate 0.2 --random-selection-rate 0.2 --children 5 --mutation-rate 0.3 --max-generations 500 --model 9x9-easy-03 --restart-nb-generations 40
```
Adapt the parameters to your needs. 

To generate a new Sudoku puzzle, use the following command:

```sh
python3 sudoku_utils/generate_board.py
```
The generated board will be saved in the samples directory.
## Directory and File Structure

```
project
    │_ classes (contains the classes used in the project)
    |_ samples (contains the Sudoku puzzles)
    |_ sudoku_utils (contains ultility functions for sudoku, GA and board generation)
    |_ general_utils (contains general utility functions used for the project)
    main.py (main script to run the program)
    README.md
    requirements.txt    (list of dependencies)
```
## Dependencies
To install the dependencies, run the following command:

```sh
pip install -r requirements.txt
```


## Acknowledgements
https://nidragedd.github.io/sudoku-genetics/ <br>
https://github.com/nidragedd/genetics <br>
https://www.researchgate.net/publication/337488121_An_Empirical_Analysis_of_Genetic_Algorithm_with_Different_Mutation_and_Crossover_Operators_for_Solving_Sudoku <br>
