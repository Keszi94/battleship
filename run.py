import random
import re
from tabulate import tabulate
from colorama import Fore, Back, Style, init

# Initialize colorama for colored text
init()

# The welcome message printed at the top of the console
def welcome_message():
    print(Fore.MAGENTA + 'WELCOME TO BATTLESHIP!\n' + Style.RESET_ALL)
    print('Rules:\n')
    print('1.: The boards are ' + Fore.MAGENTA + '5x5 ' + Style.RESET_ALL + ', they start from ' + Fore.MAGENTA + 'row 1, column 1.' + Style.RESET_ALL)
    print('2.: Each player has ' + Fore.MAGENTA + '4 ships' + Style.RESET_ALL + ' on their board.') 
    print('3.: Try to sink the computers ships before it sinks yours.\n')
    print(Fore.MAGENTA + 'Good luck!\n' + Style.RESET_ALL)   

welcome_message()
