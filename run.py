import random
import re
from tabulate import tabulate
from colorama import Fore, Back, Style, init

# Initialize colorama for colored text
init()

# The welcome message and game rules printed at the top of the console
def welcome_message():

    """ 
    The game will start after the correct name is typed in and the player hits enter.
    """
    print()
    print(Fore.MAGENTA + 'WELCOME TO BATTLESHIPS!\n' + Style.RESET_ALL)
    print('Rules:\n')
    print('1.: The boards are ' + Fore.MAGENTA + '5x5 ' + Style.RESET_ALL + ', they start from ' + Fore.MAGENTA + 'row 1, column 1.' + Style.RESET_ALL)
    print('2.: Each player has ' + Fore.MAGENTA + '4 ships' + Style.RESET_ALL + ' on their board.') 
    print("3.: Try to sink the computer's ships before it sinks yours.")
    print("4.: Hits are marked with " + Fore.MAGENTA + "'X'" + Style.RESET_ALL + ", misses will display with an " + Fore.MAGENTA + "'O'" + Style.RESET_ALL + ".")
    print("5.: You can see your ships on your board marked " + Fore.MAGENTA + "'S'" + Style.RESET_ALL + ".")
    print("6.: You will have to choose a row(1-5) and a column(1-5) in each round.\n")
    print(Fore.MAGENTA + 'Good luck!\n' + Style.RESET_ALL)   

def player_name_input():
    """
    An inmput field for the player to type in their name.
    After the name is given and the player pressed enter the game starts.
    Using isalpha() so that the input field only takes letters. 
    """
    
    name = input('Please input your name (no numbers, 10 characters max): ')
    if len(name) <= 10 and name.isalpha():
        return name
    else :
            print(Back.RED + 'Invalid input! Please try again! (no numbers, 10 characters max)' + Style.RESET_ALL + '\n')
            input('Please input your name (no numbers, 10 characters max): ')

class Boards:
    """
    Creating the dimensions for the playing boards 
    Placing the ships on the boards in random positions
    """
    
    def __init__(self, size=5, num_ships=4):
        self.size = size #default is 5
        self.num_ships = num_ships #default is 4
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.place_ships() #this will call the function that puts the ships into random cells on the board

def place_ships(self):
    """
    Randomly place the 4 ships on the boards 
    """
    ships_placed = 0
    while ships_placed < self.num_ships:
        """
        Generating two random numbers between 0 and 4 for row(x) and column(y) 
        """
        x = random.randint(0, self.size -1)
        y = random.randint(0, self.size -1)
        if self.board[x][y] == ' ': #checks if the selected position is empty
            self.board[x][y] = 'S' #if the position is empty an 'S' is placed for 'Ship'
            ships_placed += 1           

def display_boards(self, board_title, show_ships_pos=False):
    """
    This function will display the boards
    On the player's board the position of the ships will be visible 
    """ 
    display = [row[:] for row in self.board]
    if not show_ships_pos:
        display = [[' ' if cell == 'S' else cell for cell in row] for row in display]
    
    print(f"\n{board_title}") #prints whose board it is above the board (player's board, computer's board)
    print(tabulate(display, tablfmt="fancy_grid", stralign="center")) #prints the boards

def play_game():
    """ 
    Runs all the program functions

    """
    welcome_message()
    player_name_input()


play_game()

