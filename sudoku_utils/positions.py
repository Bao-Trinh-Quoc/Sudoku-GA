"""
This module is used to compute the positions of the elements in grids depending on the grid size

Created on: 06/01/2024
"""

from random import shuffle

# def retrieve_row_id_from_pos_and_size(pos, size):
#     """
#     Given a position in the row/col/grid and the size of the row/col/grid, determine the row index (from 0)
#     :param pos: (int), the position in the rol/col/grid (from 0)
#     :param size : (int), the size of the row/col/grid
#     :return (int) id of the row (from 0)
#     """
#     return pos // size

# def retrieve_col_id_from_pos_and_size(pos, size):
#     """
#     Like retrieve_row_id_from_pos_and_size, but for the column index
#     :param pos: (int), the position in the row/col/grid (from 0)
#     :param size : (int), the size of the row/col/grid
#     :return (int) id of the column (from 0)
#     """
#     return pos % size

# def retrieve_grid_id_from_row_and_col(row_id, col_id, grid_size):
#     """
#     Given the row and column indexes, determine the grid index (from 0)
#     Suppose 9x9 board with gid_size = 3, the grid indexes are as follows:
#     row_id = 1, col_id = 2 -> grid_id = (1 // 3) * 3 + (2 // 3) = 0

#     :param row_id: (int), the row index (from 0)
#     :param col_id: (int), the column index (from 0)
#     :param grid_size: (int), the size of the grid
#     :return (int) id of the grid (from 0)
#     """
#     return int(((row_id // grid_size) * grid_size) + (col_id // grid_size))

# def retrieve_row_id_from_grid_id_and_position(gird_id, grid_position, grid_size):
#     """
#     Given the grid index and the position in the grid, determine the row index (from 0)
#     :param grid_id: (int), the grid index (from 0)
#     :param grid_position: (int), the position in the grid (from 0)
#     :param grid_size: (int), the size of the grid
#     :return (int) id of the row (from 0)
#     """
#     row_in_grid = retrieve_row_id_from_pos_and_size(grid_position, grid_size)
#     row_offset = grid_size * (retrieve_row_id_from_pos_and_size(gird_id, grid_size))
#     return row_offset + row_in_grid

# def retrieve_col_id_from_grid_id_and_position(gird_id, grid_position, grid_size):
#     """
#     Like retrieve_row_id_from_grid_id_and_position, but for the column index
#     :param grid_id: (int), the grid index (from 0)
#     :param grid_position: (int), the position in the grid (from 0)
#     :param grid_size: (int), the size of the grid
#     :return (int) id of the column (from 0)
#     """
#     col_in_grid = retrieve_col_id_from_pos_and_size(grid_position, grid_size)
#     col_offset = grid_size * (retrieve_col_id_from_pos_and_size(gird_id, grid_size))
#     return col_offset + col_in_grid

# def fill_valid_values(array_to_fill, length):
#     """
#     Fill the array where there were '0' with randomly values
#     :param array_to_fill: (array), represent a row, col or grid, containing '0' as empty cells
#     :param length: (int), the length of the array
#     :return (array) the filled array
#     """
#     # Get fixed values i.e non-zero values
#     fixed_values = [val for val in array_to_fill if val > 0]
#     # Get fixed values and their index
#     fixed_index_values = [(pos, value) for pos, value in enumerate(array_to_fill) if value > 0]
#     # Determine what are the available values based on fixed values
#     available_values = [x for x in range(1, length + 1) if x not in fixed_values]
#     shuffle(available_values)
#     # Add fixed values in the shuffled array
#     for index, val in fixed_index_values:
#         available_values.insert(index, val)
#     return available_values

def retrieve_row_id_from_position_and_size(position, size):
    """
    Given a position in the objects values, determine the id of the row (starting at 0)
    :param position: (int) position in the objects values (starting at 0)
    :param size: (int) the size of the objects (i.e number of elements per row/column/grid)
    :return: (int) id of the row (starting at 0)
    """
    return position // size


def retrieve_column_id_from_position_and_size(position, size):
    """
    Given a position in the objects values, determine the id of the row (starting at 0)
    :param position: (int) position in the objects values (starting at 0)
    :param size: (int) the size of the objects (i.e number of elements per row/column/grid)
    :return: (int) id of the column (starting at 0)
    """
    return position % size


def retrieve_grid_id_from_row_and_col(row_id, col_id, grid_size):
    """
    Given a position by it row and column id (starting at 0), determine the id of the grid (also starting at 0)
    :param row_id: (int) self-explained, the row id (starting at 0)
    :param col_id: (int) self-explained, the column id (starting at 0)
    :param grid_size: (int) self-explained, the size of one objects grid (which equals to the square root of the
    objects size, which is the number of elements per row/column/grid)
    :return: (int) id of the grid (starting at 0)
    """
    return int(col_id // grid_size + ((row_id // grid_size) * grid_size))


def retrieve_range_rows_from_grid_id(grid_id, grid_size):
    """
    Retrieve range of rows (indexes) linked to the given grid id (starting at 0) for a given grid size
    Be careful, this method returns the upper row index included because it is a 'range' in the Python sense and
    the range (start, end) does not include the 'end' element while looping with 'for' or 'enumerate'. For example,
    for a grid size=3 and grid_id=0 (the first one), the range returned will be (0, 3) so that the loop will take row 0,
    1 and 2
    :param grid_id: (int) the grid id (starting at 0) for which we want to get the range of rows
    :param grid_size: (int) size of one grid (not the objects size, its square root)
    :return: a range of rows indexes
    """
    start = int(grid_id / grid_size) * grid_size
    return range(start, start + grid_size)


def retrieve_range_columns_from_grid_id(grid_id, grid_size):
    """
    Retrieve range of columns (indexes) linked to the given grid id (starting at 0) for a given grid size.
    Be careful, this method returns the upper column index included because it is a 'range' in the Python sense and
    the range (start, end) does not include the 'end' element while looping with 'for' or 'enumerate'. For example,
    for a grid size=3 and grid_id=0 (the first one), the range returned will be (0, 3) so that the loop will take column
    0, 1 and 2
    :param grid_id: (int) the grid id (starting at 0) for which we want to get the range of columns
    :param grid_size: (int) size of one grid (not the objects size, its square root)
    :return: a range of columns indexes
    """
    start = int(grid_id % grid_size) * grid_size
    return range(start, start + grid_size)


def retrieve_row_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Given a position by it grid id and position in the grid (both starting at 0), determine the id of row (also
    starting at 0)
    :param grid_id: (int) self-explained, the grid id (starting at 0)
    :param grid_position: (int) the position of the element in this grid (starting at 0)
    :param grid_size: (int) self-explained, the size of one objects grid (which equals to the square root of the
    objects size, which is the number of elements per row/column/grid)
    :return: (int) id of the row (starting at 0)
    """
    row_in_grid = retrieve_row_id_from_position_and_size(grid_position, grid_size)
    delta_row = grid_size * (retrieve_row_id_from_position_and_size(grid_id, grid_size))
    return delta_row + row_in_grid


def retrieve_column_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Given a position by it grid id and position in the grid (both starting at 0), determine the id of column (also
    starting at 0)
    :param grid_id: (int) self-explained, the grid id (starting at 0)
    :param grid_position: (int) the position of the element in this grid (starting at 0)
    :param grid_size: (int) self-explained, the size of one objects grid (which equals to the square root of the
    objects size, which is the number of elements per row/column/grid)
    :return: (int) id of the column (starting at 0)
    """
    col_in_grid = retrieve_column_id_from_position_and_size(grid_position, grid_size)
    delta_col = grid_size * (retrieve_column_id_from_position_and_size(grid_id, grid_size))
    return delta_col + col_in_grid


def fill_with_some_valid_values(array_to_fill, length):
    """
    Based on a given array containing '0' and non-zero values, return a new array filled with distinct and authorized
    values randomly placed where there were '0'.
    :param array_to_fill: (array) represents a grid, column or row and contains non-zero values if they are known or
    zero otherwise
    :param length: (int) size of the objects
    :return: (array) new array filled with distinct and authorized values randomly placed where there were '0'.
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