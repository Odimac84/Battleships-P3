"""
Markups on the board to show if we hit or missed.
"""
#Legend
# X for placing ship and hit battleship
# ' ' for empty plot
# '-' for missed shot


"""
Defining 2 boards, one for the player to have their guesses on and one with 
the correct solution on it. 
"""
ANSWER_BOARD = [[' '] * 10 for x in range(9)]
PLAYER_BOARD = [[' '] * 10 for x in range(9)]

"""
Converting to letters to use at the top of the board for easier overview of 
the gameboard.
"""
letters_convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
 'H': 7, 'I': 8}

"""
Loop to build the boards for both the PLAYER_BOARD and the ANSWER_BOARD.
"""
def print_board(board):
    print('   A B C D E F G H I')
    print('   +-+-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

"""
Loop to Put out the 5 battleships that we are gonna try and find.
"""
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,9), randint(0,9)
    while board[ship_row][ship_column] == 'X':
        ship_row, ship_column = randint(0,9), randint(0,9)
    board[ship_row][ship_column] = 'X'
  
"""
Function to add the input data on where to drop the bomb. built with loops to 
make sure correct data is entered. .upper is used to make sure that it will always be
an uppercase letter that is provided for the code to run.
"""
def get_ship_location():
    row = input('Please enter a ship row 1-9: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-9: ')
    column = input('Please enter a ship column A-I: ').upper()
    while column not in 'ABCDEFGHI':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-I: ').upper()
    return int(row) - 1, letters_convert[column]

"""
Counts the hits and tells us how many hits we have. 
"""
def count_hit_ships(board):
    pass

