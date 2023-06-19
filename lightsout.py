import random

# Function to create a new Lights Out puzzle board
def create_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.choice([True, False]))  # True represents a lit cell, False represents an unlit cell
        board.append(row)
    return board

# Function to print the current state of the board
def print_board(board):
    size = len(board)
    for row in board:
        for cell in row:
            print("X" if cell else " ", end=" ")
        print()

# Function to toggle the state of a cell and its neighboring cells
def toggle_cell(board, row, col):
    size = len(board)
    board[row][col] = not board[row][col]  # Toggle the selected cell

    # Toggle the neighboring cells (up, down, left, right)
    if row > 0:
        board[row - 1][col] = not board[row - 1][col]
    if row < size - 1:
        board[row + 1][col] = not board[row + 1][col]
    if col > 0:
        board[row][col - 1] = not board[row][col - 1]
    if col < size - 1:
        board[row][col + 1] = not board[row][col + 1]

# Function to check if the board is solved (all cells are unlit)
def is_solved(board):
    for row in board:
        if True in row:
            return False
    return True

# Main function to run the Lights Out puzzle game
def main():
    size = int(input("Enter the size of the board: "))
    board = create_board(size)

    print("Lights Out - Puzzle Game")
    print("Instructions:")
    print("Toggle the state of a cell and its neighboring cells.")
    print("The goal is to turn off all the lights.")

    while True:
        print("\nCurrent board:")
        print_board(board)

        row = int(input("Enter the row number (0 to {}): ".format(size - 1)))
        col = int(input("Enter the column number (0 to {}): ".format(size - 1)))

        toggle_cell(board, row, col)

        if is_solved(board):
            print("\nCongratulations! You solved the puzzle!")
            break

# Run the main function
if __name__ == "__main__":
    main()

