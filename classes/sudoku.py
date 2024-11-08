"""
Created on: 08/11/2024

"""

from random import randint
from math import sqrt
import numpy as np

from sudoku_utils import positions, board_utils
from general_utils import tools

# class Sudoku:
#     _grid_size      = 0
#     _size           = 0
#     _fixed_values   = None
#     _rows           = None
#     _columns        = None
#     _grids          = None
#     _fitness_score  = None

#     def __init__(self, values):
#         """
#         Constructor of the Sudoku class

#         :param values: (array) the values of the board. if Unknown, put 0 otherwise put fixed-number-value
#         rows, columns and grids are initialized based on the values and a dictionary of fixed values is created
#         """
#         nb_rows = int(sqrt(len(values))) # 9x9 -> 9
#         self._size = nb_rows
#         self._grid_size = int(sqrt(nb_rows)) # 9x9 -> 3
#         self._rows = {}
#         self._columns = {}
#         self._grids = {}
#         self._fixed_values = {}

#         if nb_rows != self._grid_size ** 2:
#             raise ValueError("The number of values is not a perfect square")

#         self._init_values = []
#         self.set_initial_values(values)
    
#     def set_initial_values(self, values):
#         """
#         Set rows, columns, and grids based on an array of values
#         :param values: (array) the values of the board. if Unknown, put 0 otherwise put fixed-number-value
#         """
#         self._init_values = values
#         expected_len = pow(self._size, 2)
#         if len(values) != expected_len:
#             raise ValueError("The number of values is not correct")
        
#         # Initialize rows, columns, and grids
#         for i in range(self._size):
#             self._rows[i] = []
#             self._columns[i] = []
#             self._grids[i] = []
        
#         pos = 0
#         for char in values:
#             val = int(char)
#             row_id = positions.retrieve_row_id_from_pos_and_size(pos, self._size)
#             col_id = positions.retrieve_col_id_from_pos_and_size(pos, self._size)
#             grid_id = positions.retrieve_grid_id_from_row_and_col(row_id, col_id, self._grid_size)
#             pos += 1
#             # Append the value to the corresponding row, column, and grid dictionaries
#             self._rows[row_id].append(val)
#             self._columns[col_id].append(val)
#             self._grids[grid_id].append(val)
#             # If the value is fixed, add it to the fixed values dictionary        
#             if val != 0:
#                 self._fixed_values[board_utils.build_fixed_val_key(row_id, col_id)] = val
        
#         return self
    
#     def fill_random(self):
#         """
#         Randomly fill the board with values. Result is valid in term of grids
#         :return: an objects with grids all filled with available values and no duplicates. 
#         But still can have duplicates in rows and columns
#         """
#         for grid_id, grid_values in self._grids.items():
#             available_vals = positions.fill_valid_values(grid_values, self._size)

#             for pos, new_val in enumerate(available_vals):
#                 row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, pos, self._grid_size)
#                 col_id = positions.retrieve_col_id_from_grid_id_and_position(grid_id, pos, self._grid_size)
#                 self._rows[row_id][col_id] = new_val
#                 self._columns[col_id][row_id] = new_val

#             self._grids[grid_id] = available_vals

#         return self
    
#     def fill_with_grids(self, grids):
#         """
#         Fill the board with the given grids
#         :param grids: (list) the grids to fill the board with
#         :return: Changed the object with the new grids
#         """
#         for grid_id, grid_values in enumerate(grids):
#             for pos, new_val in enumerate(grid_values):
#                 row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, pos, self._grid_size)
#                 col_id = positions.retrieve_col_id_from_grid_id_and_position(grid_id, pos, self._grid_size)
#                 self._rows[row_id][col_id] = new_val
#                 self._columns[col_id][row_id] = new_val
#             self._grids[grid_id] = grid_values
        
#         return self
    
#     def display(self):
#         """
#         Iterate over rows to print values and display the objects
#         """
#         for i in range(self._size):
#             if i > 1 and i % self._grid_size == 0:
#                 print(board_utils.build_seperator_line(self._grid_size))

#             line = self._rows[i]
#             for j in range(self._size):
#                 val = line[j]
#                 if self.size() > 9: # for a larger grid, we need to display 2 digits
#                     val = str(val).zfill(2)
#                 if j > 0 and j % self._grid_size == 0:
#                     print(' | {}'.format(val), end='')
#                 elif j == (self._size - 1):
#                     print(' {}'.format(val))
#                 else:
#                     print(' {}'.format(val), end='')
#         print("")

#     def fitness(self):
#         """
#         Compute the fitness score of the board. The fitness score is the number of duplicates in rows and columns
#         :return: (int) the fitness score. Lower is better
#         """
#         if self._fitness_score is None:
#             duplicates = 0
#             for i in range(self.size()):
#                 duplicates += tools.count_duplicates(self._rows[i]) + tools.count_duplicates(self._columns[i])
#             self._fitness_score = duplicates

#         return self._fitness_score

#     def _is_fixed(self, row_id, col_id):
#         """
#         Check if the value at the given position is fixed
#         :param row_id: (int) the row index
#         :param col_id: (int) the column index
#         :return: (bool) True if the value is fixed, False otherwise
#         """
#         return board_utils.build_fixed_val_key(row_id, col_id) in self._fixed_values

#     def _get_random_non_fixed(self, grid_id, forbidden_pos):
#         """
#         Randomly pick one value in the given grid id. The value must not be in the forbidden values or fixed value
#         :param grid_id: (int) the grid id
#         :param forbidden_pos: (int) the position that cannot be picked even if it is not fixed
#         :return: (tuple of ints) picked position in grid, row_id, col_id
#         """
#         rand_pos    = -1
#         row_id      = -1
#         col_id      = -1
#         is_fixed    = True
#         while is_fixed or rand_pos == forbidden_pos:
#             rand_pos = randint(0, self._size - 1)
#             row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, rand_pos, self._grid_size)
#             col_id = positions.retrieve_col_id_from_grid_id_and_position(grid_id, rand_pos, self._grid_size)
#             is_fixed = self._is_fixed(row_id, col_id)
        
#         return rand_pos, row_id, col_id

#     def swap_2_values(self):
#         """
#         Swap 2 values in the grid which are not fixed
#         :return: the object with 2 values swapped
#         """
#         grid_id = np.random.randint(0, self._size - 1)  # self._size or self._size - 1
        
#         rand_pos1, row_id1, col_id1 = self._get_random_non_fixed(grid_id, -1)
#         rand_pos2, row_id2, col_id2 = self._get_random_non_fixed(grid_id, rand_pos1)

#         grid_values = self._grids[grid_id]
#         val1 = grid_values[rand_pos1]
#         val2 = grid_values[rand_pos2]

#         # Swap the values in the grid
#         grid_values[rand_pos1] = val2
#         grid_values[rand_pos2] = val1
#         # Swap the values in the rows and columns
#         self._rows[row_id1][col_id1] = val2
#         self._rows[row_id2][col_id2] = val1
#         self._columns[col_id1][row_id1] = val2
#         self._columns[col_id2][row_id2] = val1

#         return self
    

#     def grids(self):
#         """
#         :return: (dict) grids of objects as dict where key is the 'grid id' and value an array of values
#         """
#         return self._grids

#     def rows(self):
#         """
#         :return: (dict) rows of objects as dict where key is the 'row id' and value an array of values
#         """
#         return self._rows

#     def columns(self):
#         """
#         :return: (dict) columns of objects as dict where key is the 'column id' and value an array of values
#         """
#         return self._columns

#     def size(self):
#         """
#         :return: (int) size of the objects, i.e number of elements per row/column/grid
#         """
#         return self._size

#     def grid_size(self):
#         """
#         :return: (int) size of a grid of the objects (i.e the square root of the size). For a 9x9 size, this method
#         returns 3
#         """
#         return self._grid_size

#     def get_initial_values(self):
#         """
#         :return: (array) the values used to build the objects at first time
#         """
#         return self._init_values

class Sudoku(object):
    """
    A sudoku grid has a size and contains some fixed values (either given at the beginning, either guessed after runs of
    computation). This class handles also some dicts for rows, columns and grids
    """
    _grid_size = 0
    _size = 0
    _fixed_values = None
    _rows = None
    _columns = None
    _grids = None
    _fitness_score = None

    def __init__(self, values):
        """
        Constructor

        :param values: (array) numbers needed to fill the objects. If one value is unknown, put a '0' character,
        otherwise provide the fixed-numbered-value.
        Then, rows, columns and grids are computed based on those values and a dict of fixed values is created
        """
        nb_rows = int(sqrt(len(values)))
        self._size = nb_rows
        self._grid_size = int(sqrt(nb_rows))
        self._rows = {}
        self._columns = {}
        self._grids = {}
        self._fixed_values = {}

        if nb_rows/self._grid_size != self._grid_size:
            raise Exception("You must provide a power number value")

        self._init_values = []
        self.set_initial_values(values)

    def set_initial_values(self, values):
        """
        Compute rows, columns and grids dicts based on an array of values
        :param values: (array) numbers needed to fill the objects. If one value is unknown, put a '0' character,
        otherwise provide the fixed-numbered-value.
        """
        self._init_values = values
        expected_len = pow(self._size, 2)
        if len(values) != expected_len:
            raise Exception("You must provide a number of values matching the size of the objects. Got {} whereas {} "
                            "was expected".format(len(values), expected_len))

        # Init the dicts
        for i in range(self._size):
            self._rows[i] = []
            self._columns[i] = []
            self._grids[i] = []

        # In the above section we determine, according to the position in the given values, in which
        # column, row and grid the value belongs to
        position = 0
        for character in values:
            val = int(character)
            row_id = positions.retrieve_row_id_from_position_and_size(position, self._size)
            col_id = positions.retrieve_column_id_from_position_and_size(position, self._size)
            grid_id = positions.retrieve_grid_id_from_row_and_col(row_id, col_id, self._grid_size)

            position += 1

            # Add this value to all dicts we maintain
            self._rows[row_id].append(val)
            self._columns[col_id].append(val)
            self._grids[grid_id].append(val)

            # Keep knowledge of fixed values where key is their position (key= row_id|col_id)
            if val != 0:
                self._fixed_values[board_utils.build_fixed_val_key(row_id, col_id)] = val
        return self

    def fill_random(self):
        """
        Randomly fill empty cells. Result is valid in terms of grids
        :return: a objects with grids all filled with available values and no duplicates. But there might (for sure
        there will) be some duplicates in rows/columns.
        """
        # Ensure that at least grids are 'correct' so we fill each one with available values to avoid duplicates
        for grid_id, grid_values in self._grids.items():
            available_values = positions.fill_with_some_valid_values(grid_values, self._size)

            # Get row and col from grid_id and position in grid and substitute the value
            for position, new_value in enumerate(available_values):
                row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, position, self._grid_size)
                col_id = positions.retrieve_column_id_from_grid_id_and_position(grid_id, position, self._grid_size)
                self._columns[col_id][row_id] = new_value
                self._rows[row_id][col_id] = new_value

            # Substitute value with new one in grids arrays
            self._grids[grid_id] = available_values
        return self

    def fill_with_grids(self, grids):
        """
        Fill the sudoku with given grids
        :param grids: (list) dicts used to fill this instance (used when building a new object from others)
        :return: (sudoku) changed sudoku
        """
        for grid_id, grid_values in enumerate(grids):
            # Get row and col from grid_id and position in grid and substitute the value
            for position, value in enumerate(grid_values):
                row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, position, self._grid_size)
                col_id = positions.retrieve_column_id_from_grid_id_and_position(grid_id, position, self._grid_size)
                self._columns[col_id][row_id] = value
                self._rows[row_id][col_id] = value
                '''
                Copy/paste value per value to avoid references issue (i.e 's.grids()[grid_id] = grid_values' will work 
                but it will generate further issues with mutation (as parent will also mutate and there are more than 1
                child per couple)
                '''
                self._grids[grid_id][position] = value
        return self

    def display(self):
        """
        Iterate over rows to print values and display the objects. We need to take care about new lines and subgrids
        separations (horizontal and vertical)
        """
        for i in range(self._size):
            if i > 1 and i % self._grid_size == 0:
                print(board_utils.build_separator_line(self._grid_size))

            line = self._rows[i]
            for j in range(self._size):
                val = line[j]
                if self.size() > 9:
                    val = str(val).zfill(2)
                if j > 0 and j % self._grid_size == 0:
                    print(' | {}'.format(val), end='')
                elif j == (self._size - 1):
                    print(' {}'.format(val))
                else:
                    print(' {}'.format(val), end='')
        print("")

    def grids(self):
        """
        :return: (dict) grids of objects as dict where key is the 'grid id' and value an array of values
        """
        return self._grids

    def rows(self):
        """
        :return: (dict) rows of objects as dict where key is the 'row id' and value an array of values
        """
        return self._rows

    def columns(self):
        """
        :return: (dict) columns of objects as dict where key is the 'column id' and value an array of values
        """
        return self._columns

    def size(self):
        """
        :return: (int) size of the objects, i.e number of elements per row/column/grid
        """
        return self._size

    def grid_size(self):
        """
        :return: (int) size of a grid of the objects (i.e the square root of the size). For a 9x9 size, this method
        returns 3
        """
        return self._grid_size

    def get_initial_values(self):
        """
        :return: (array) the values used to build the objects at first time
        """
        return self._init_values

    def fitness(self):
        """
        The most important function of the program. Here we give a note to the candidate according to the values
        Basically it is: how many figures are at the right place among the number of figures to find
        'Right place' = the number of duplicate symbols in rows or columns. Fewer duplicates presumably means a better
        solution
        :return: (int) a score for this candidate, lower it is, better is the candidate
        """
        # Evaluate once per individual
        if self._fitness_score is None:
            duplicates_counter = 0
            for i in range(self.size()):
                duplicates_counter += tools.count_duplicates(self._rows[i]) + tools.count_duplicates(self._columns[i])
            self._fitness_score = duplicates_counter
        return self._fitness_score

    def swap_2_values(self):
        """
        Pick randomly 2 elements to swap if they are not fixed values
        Once this is done, change the value in the objects arrays (rows, columns and grids)
        :return: (object) changed object
        """
        # Pick a random grid
        grid_id = np.random.randint(0, self._size - 1)

        rand_pos_1, row_id_1, col_id_1 = self._get_random_not_fixed(grid_id, -1)
        rand_pos_2, row_id_2, col_id_2 = self._get_random_not_fixed(grid_id, rand_pos_1)

        grid_values = self._grids[grid_id]
        val_1 = grid_values[rand_pos_1]
        val_2 = grid_values[rand_pos_2]

        grid_values[rand_pos_1] = val_2
        grid_values[rand_pos_2] = val_1
        self._rows[row_id_1][col_id_1] = val_2
        self._rows[row_id_2][col_id_2] = val_1
        self._columns[col_id_1][row_id_1] = val_2
        self._columns[col_id_2][row_id_2] = val_1

        return self

    def _is_fixed(self, row_id, col_id):
        """
        Given a row id and a column id, returns True if the value is fixed at the beginning
        :param row_id: (int) the row id
        :param col_id: (int) the column id
        :return: (boolean) True if value is fixed (i.e it is a given value), False otherwise
        """
        return board_utils.build_fixed_val_key(row_id, col_id) in self._fixed_values

    def _get_random_not_fixed(self, grid_id, forbidden_pos):
        """
        Randomly pick one value in the given grid id for the individual. The picked value cannot be a fixed one or a
        forbidden one
        :param grid_id: (int) id of the grid
        :param forbidden_pos: (int) in addition to the fixed value, specify a position that cannot be picked neither,
        even if not a fixed one
        :return: (tuple of 3 int) the picked position in the grid, the row id and the column id
        """
        rand_pos = -1
        row_id = -1
        col_id = -1
        is_fixed = True
        while is_fixed or rand_pos == forbidden_pos:
            rand_pos = randint(0, self._size - 1)
            # We need to find their position (row and column) in the whole table to check whether it is fixed or not
            row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, rand_pos, self._grid_size)
            col_id = positions.retrieve_column_id_from_grid_id_and_position(grid_id, rand_pos, self._grid_size)
            is_fixed = self._is_fixed(row_id, col_id)
        return rand_pos, row_id, col_id
