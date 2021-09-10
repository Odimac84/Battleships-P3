from random import randint

# Markups on the board to show if we hit or missed.

# X for placing ship and hit battleship
# ' ' for empty plot
# '*' for missed shot


"""
Defining 2 boards, one for the player to have their guesses on and one with
the correct solution on it. ANSWER_BOARD is hidden and used to check locations
against only.
"""

ANSWER_BOARD = [[' '] * 9 for x in range(9)]
PLAYER_BOARD = [[' '] * 9 for x in range(9)]

# Loop to build the boards for both the PLAYER_BOARD and the ANSWER_BOARD.


def print_board(board):
    print('  A B C D E F G H I')
    print('  +-+-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

"""
Converting to letters to use at the top of the board for easier overview of
the gameboard.
"""

letters_convert = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8
}
# Loop to Put out the 5 battleships that we are gonna try and find.


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = 'X'

"""
Function to add the input data on where to drop the bomb. built with loops to
make sure correct data is entered. .upper is used to make sure that it will
always be an uppercase letter that is provided for the code to run.
"""


def get_ship_location():
    row = input('Please enter a ship row 1-9: \n')
    while row not in '123456789':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-9: \n')
    column = input('Please enter a ship column A-I: \n').upper()
    while column not in 'ABCDEFGHI':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-I: \n').upper()
    return int(row) - 1, letters_convert[column]


# Counts the hits and tells us how many hits we have.

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

create_ships(ANSWER_BOARD)
turns = 25

# if statement only activates when you start the game to print out short rules

if turns == 25:
    print('LETS PLAY BATTLESHIPS')
    print('Find the enemies on the map in 25 turns by choosing locations.')
    print('5 ships are hiding on the map, all must be found to win the game')

""""
function to check if the input data is a hit or a miss, also checks
if your winning. 25 turns to find the ships or you lose.
"""

while turns > 0:
    print_board(PLAYER_BOARD)
    row, column = get_ship_location()
    if PLAYER_BOARD[row][column] == 'X' or PLAYER_BOARD[row][column] == '*':
        print('You already guessed that')
    elif ANSWER_BOARD[row][column] == 'X':
        print(' HIT, you have sunk a ship.')
        PLAYER_BOARD[row][column] = 'X'
        turns -= 1
        print('You have ' + str(turns) + ' turns remaining')
    else:
        print('MISS, try again')
        PLAYER_BOARD[row][column] = '*'
        turns -= 1
        print('You have ' + str(turns) + ' turns remaining')
    if count_hit_ships(PLAYER_BOARD) == 5:
        print('Congratulations, you won no more ships present')
        break
    if turns == 0:
        print('No more bombs left you got captured')
        print_board(ANSWER_BOARD)
        break
