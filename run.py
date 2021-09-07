"""
Markups on the board to show if we hit or missed. 
"""
#Legend
# X for placing ship and hit battleship
# ' ' for empty plot
# '-' for missed shot


"""
Defining 2 boards, one for the player to have their guesses on and one with the correct solution on it. 
"""
ANSWER_BOARD = [[' '] * 11 for x in range(10)]
PLAYER_BOARD = [[' '] * 11 for x in range(10)]

"""
Converting to letters to use at the top of the board for easier overview of the gameboard.
"""
letters_convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,}

"""
Loop to build the boards for both the PLAYER_BOARD and the ANSWER_BOARD.
"""
def print_board(board):
    pass

"""
Loop to Put out the 5 battleships that we are gonna try and find.
"""
def create_ships(board):
    pass
  
"""
Function to add the input data on where to drop the bomb. built with loops to make sure correct data is entered.
"""
def get_ship_location():
    pass

"""
Counts the hits and tells us how many hits we have. 
"""
def count_hit_ships(board):
    pass

