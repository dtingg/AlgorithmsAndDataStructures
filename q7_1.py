"""
Quiz 7
Question 1
Given a 2d array representation of a Tic Tac Toe board, determine if
there is a winner. Recall that Tic Tac Toe is played on a 3x3 grid and
a winner is declared if there is any single row, column, or diagonal that
belongs to a single player. The grid entries will either contain an 'X'
or an 'O', indicating which player that cell belongs to.

The input is a 2d array:
[
  ['X', 'O', 'X'],
  ['X', 'X', 'O'],
  ['O', 'O', 'X']
]
In the above board, X is a winner (the diagonal from upper-left to lower-right).

You don't need to check if the input board would be impossible to get to given
the rules of the game — you only need to see if there's a winner given the rules above.
"""


def winner(board):
    three_x = ["X", "X", "X"]
    three_o = ["O", "O", "O"]

    # Three across
    if board[0] == three_x or board[1] == three_x or board[2] == three_x:
        return "X is the winner."
    elif board[0] == three_o or board[1] == three_o or board[2] == three_o:
        return "O is the winner."

    # Three up and down
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "X is the winner."
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return "O is the winner."

    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "X is the winner."
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return "O is the winner."

    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "X is the winner."
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return "O is the winner."

    # Three diagonal
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X is the winner."
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O is the winner."

    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X is the winner."
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O is the winner."

        # No winner
    else:
        return "No winner yet."


print(winner([
    ['X', 'O', 'X'],
    ['X', 'X', 'O'],
    ['O', 'O', 'X']
]))
