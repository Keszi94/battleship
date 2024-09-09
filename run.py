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
    """
    
    def __init__(self, size=5, num_ships=4):
        self.size = size
        self.num_ships = num_ships
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.place_ships()

#def place_ships(self):


def play_game():
    """ 
    Runs all the program functions

    """
    welcome_message()
    player_name_input()

play_game()
