"""
This module is used to compute the positions of the elements in grids depending on the grid size

Created on: 06/01/2024
"""

from random import shuffle

def retrieve_row_id_from_position_and_size(position, size):
    """
    Given a position in the row/col/grid and the size of the row/col/grid, determine the row index (from 0)
    :param pos: (int), the position in the rol/col/grid (from 0)
    :param size : (int), the size of the row/col/grid
    :return (int) id of the row (from 0)
    """
    return position // size


def retrieve_column_id_from_position_and_size(position, size):
    """
    Like retrieve_row_id_from_pos_and_size, but for the column index
    :param pos: (int), the position in the row/col/grid (from 0)
    :param size : (int), the size of the row/col/grid
    :return (int) id of the column (from 0)
    """
    return position % size


def retrieve_grid_id_from_row_and_col(row_id, col_id, grid_size):
    """
    Given the row and column indexes, determine the grid index (from 0)
    Suppose 9x9 board with gid_size = 3, the grid indexes are as follows:
    row_id = 1, col_id = 2 -> grid_id = (1 // 3) * 3 + (2 // 3) = 0

    :param row_id: (int), the row index (from 0)
    :param col_id: (int), the column index (from 0)
    :param grid_size: (int), the size of the grid
    :return (int) id of the grid (from 0)
    """
    return int(col_id // grid_size + ((row_id // grid_size) * grid_size))

def retrieve_row_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Given the grid index and the position in the grid, determine the row index (from 0)
    :param grid_id: (int), the grid index (from 0)
    :param grid_position: (int), the position in the grid (from 0)
    :param grid_size: (int), the size of the grid
    :return (int) id of the row (from 0)
    """
    row_in_grid = retrieve_row_id_from_position_and_size(grid_position, grid_size)
    delta_row = grid_size * (retrieve_row_id_from_position_and_size(grid_id, grid_size))
    return delta_row + row_in_grid


def retrieve_column_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Like retrieve_row_id_from_grid_id_and_position, but for the column index
    :param grid_id: (int), the grid index (from 0)
    :param grid_position: (int), the position in the grid (from 0)
    :param grid_size: (int), the size of the grid
    :return (int) id of the column (from 0)
    """
    col_in_grid = retrieve_column_id_from_position_and_size(grid_position, grid_size)
    delta_col = grid_size * (retrieve_column_id_from_position_and_size(grid_id, grid_size))
    return delta_col + col_in_grid


def fill_with_some_valid_values(array_to_fill, length):
    """
    Fill the array where there were '0' with randomly values
    :param array_to_fill: (array), represent a row, col or grid, containing '0' as empty cells
    :param length: (int), the length of the array
    :return (array) the filled array
    """
    # Get fixed values
    fixed_values = [value for value in array_to_fill if value > 0]
    # Get fixed values and their index
    fixed_index_values = [(pos, value) for pos, value in enumerate(array_to_fill) if value > 0]
    # Determine what are the available values based on fixed values
    available_values = [x for x in range(1, length + 1) if x not in fixed_values]
    shuffle(available_values)
    # Add fixed values in the shuffled array
    for index, val in fixed_index_values:
        available_values.insert(index, val)
    return available_values