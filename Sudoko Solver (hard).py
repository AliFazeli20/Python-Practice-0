# Sudoku Solver using backtracking algorithm

# Utility function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Check if a number can be placed at grid[row][col]
def is_safe(grid, row, col, num):
    # Check if 'num' is not in the current row and current column
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    
    # Check if 'num' is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

# Function to solve the Sudoku puzzle
def solve_sudoku(grid):
    # Find an empty cell
    empty = find_empty_location(grid)
    if not empty:
        return True  # No empty cell means the puzzle is solved
    
    row, col = empty
    
    for num in range(1, 10):
        # Check if it is safe to place the number
        if is_safe(grid, row, col, num):
            grid[row][col] = num  # Place the number
            if solve_sudoku(grid):  # Recur to solve the rest of the grid
                return True
            grid[row][col] = 0  # If placing the number doesn't lead to a solution, reset the cell
    
    return False  # Trigger backtracking

# Function to find an empty location in the grid
def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle and print the result
if solve_sudoku(sudoku_grid):
    print("Solved Sudoku grid:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
