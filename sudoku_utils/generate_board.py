import os
import math
import random

def generate_filled_board(size):
    """Generate a filled Sudoku board of the given size."""
    def is_valid(board, row, col, num):
        for x in range(size):
            if board[row][x] == num or board[x][col] == num:
                return False
        start_row, start_col = row - row % grid_size, col - col % grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(board):
        for row in range(size):
            for col in range(size):
                if board[row][col] == 0:
                    for num in range(1, size + 1):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    grid_size = int(math.sqrt(size))
    board = [[0 for _ in range(size)] for _ in range(size)]
    solve(board)
    return board

def remove_numbers(board, size, num_holes):
    """Remove numbers from the filled board to create a puzzle."""
    for _ in range(num_holes):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        while board[row][col] == 0:
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        board[row][col] = 0
    return board

def save_board_to_file(board, filename):
    """Save the Sudoku board to a file."""
    with open(filename, 'w') as f:
        size = len(board)
        grid_size = int(math.sqrt(size))
        for i, row in enumerate(board):
            f.write(' '.join(map(str, row[:grid_size])) + ' | ' + ' '.join(map(str, row[grid_size:2*grid_size])) + ' | ' + ' '.join(map(str, row[2*grid_size:])) + '\n')
            if (i + 1) % grid_size == 0 and i + 1 != size:
                f.write('------|-------|------\n')
        # delete the last redundant line 
        f.seek(f.tell() - 1)
        f.truncate()
            
def is_valid_size(size):
    """Check if the size is a perfect square."""
    return size > 0 and math.isqrt(size) ** 2 == size

def main():
    size = int(input("Enter the size of the Sudoku board (e.g., 9 for 9x9): "))
    if not is_valid_size(size):
        print("Invalid size. The size must be a perfect square (e.g., 4, 9, 16).")
        return

    num_holes = int(input("Enter the number of holes(the lower the holes, the easier the puzzle) to create in the puzzle: "))
    board = generate_filled_board(size)
    board = remove_numbers(board, size, num_holes)
    filename = f"samples/{size}x{size}-created_puzzle.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    save_board_to_file(board, filename)
    print(f"Sudoku puzzle saved to {filename}")

if __name__ == "__main__":
    main()