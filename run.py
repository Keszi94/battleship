import random
import re
from colorama import Fore, Back, Style, init

# Initialize colorama for colored text
init(autoreset=True)

# Declaring the player and computer scores globally
player_score = 0
computer_score = 0


def welcome_message():
    """
    The game will start after the correct name is
    typed in and the player hits enter.
    """
    print()
    print(Style.BRIGHT + Fore.MAGENTA + 'WELCOME TO BATTLESHIPS!\n')
    print('Rules:\n')
    print('1.: The boards are ' + Style.BRIGHT + Fore.MAGENTA + '5x5' +
          Style.RESET_ALL + ', they start from ' + Style.BRIGHT +
          Fore.MAGENTA + 'row 1, column 1.')
    print('2.: Each player has ' + Style.BRIGHT + Fore.MAGENTA + '4 ships' +
          Style.RESET_ALL + ' on their board.')
    print("3.: Try to sink the computer's ships before it sinks yours.")
    print("4.: Hits are marked with " + Style.BRIGHT + Fore.MAGENTA + "'X'" +
          Style.RESET_ALL + ", misses will display with an " + Style.BRIGHT +
          Fore.MAGENTA + "'O'.")
    print("5.: You can see your ships on your board marked " + Style.BRIGHT +
          Fore.MAGENTA + "'S'.")
    print("6.: You will have to choose a row(1-5) and a column(1-5) in" +
          " each round.\n")
    print(Style.BRIGHT + Fore.MAGENTA + 'Good luck!\n')


def player_name_input():
    """
    An inmput field for the player to type in their name.
    After the name is given and the player pressed enter the game starts.
    Using isalpha() so that the input field only takes letters.
    """

    name = input('Please input your name (no numbers, 10 characters max): ')
    if len(name) <= 10 and name.isalpha():
        return name
    else:
        print(Back.RED + 'Invalid input! Please try again! (no numbers, 10' +
              'characters max)' + Style.RESET_ALL + '\n')
        input('Please input your name (no numbers, 10 characters max): ')


class Boards:
    """
    Creating the dimensions for the playing boards
    Placing the ships on the boards in random positions
    """
    def __init__(self, size=5, num_ships=4):
        self.size = size  # default is 5
        self.num_ships = num_ships  # default is 4
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        """
        This will call the function that puts the ships into
        random cells on the board
        """
        self.place_ships()

    def place_ships(self):
        """
        Randomly place the 4 ships on the boards
        """
        ships_placed = 0
        while ships_placed < self.num_ships:
            """
            Generating two random numbers between
            0 and 4 for row(x) and column(y)
            """
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            """Checks if the selected position is empty"""
            if self.board[x][y] == ' ':
                """If the position is empty an 'S' is placed for 'Ship'"""
                self.board[x][y] = 'S'
                ships_placed += 1

    def display_boards(self, board_title, show_ships_pos=False):
        """
        This function will display the boards
        On the player's board the position of the ships will be visible
        """
        display = [row[:] for row in self.board]
        if not show_ships_pos:
            display = [[' ' if cell == 'S' else cell for cell in row] for
                       row in display]

        """Prints whose board it is above the board (player's board,
            computer's board)"""
        print(f"\n{board_title}")

        """Top border of the boards"""
        print("  " + "  ".join(["--" for _ in range(self.size)]))

        """Rows of the boards"""
        for row in display:
            print("| " + " | ".join(row) + " |")
            print("  " + "  ".join(["--" for _ in range(self.size)]))


def player_guess(player_board, computer_board, player_guesses):
    """
     Print out the inputs asking for the player's guesses
     Print out if the player had a hit/miss at the end of the round
     Print out what the player's choice was
    """
    global player_score
    while True:
        try:
            row = int(input("Choose a row (1-5): ")) - 1
            col = int(input("Choose a column (1-5): ")) - 1
            if row not in range(5) or col not in range(5):
                raise ValueError("You must choose a number between 1 and 5!")

            # Check if coordinates have already been guessed
            if (row, col) in player_guesses:
                print(Back.YELLOW + Fore.BLACK + f"You already guessed " +
                      f"row {row+1}, column {col+1}! Guess again!")
                continue

            # Add guess to previous guesses
            player_guesses.add((row, col))
            break
        except ValueError as e:
            print(f"Invalid input! {e}")

    print(f"Your guess was: " + Style.BRIGHT + Fore.MAGENTA +
          f"row {row + 1} column {col + 1}.\n")

    if computer_board.board[row][col] == 'S':
        print(Fore.GREEN + "You hit a ship on the computer's board!\n")
        player_score += 1
        computer_board.board[row][col] = 'X'
    else:
        print(Fore.YELLOW + "You missed!\n")
        computer_board.board[row][col] = 'O'


def computer_guess(player_board, computer_guesses):
    """
    Creates random computer gueasses
    Prints out the computer's guess
    Prints out the computer's outcome for the round
    """

    global computer_score
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if (row, col) not in computer_guesses:
            computer_guesses.add((row, col))
            break

    print(f"the computer's guess was " + Fore.CYAN +
          f"row {row + 1}, column {col + 1}.'\n")

    if player_board.board[row][col] == 'S':
        print(Fore.RED + "The computer hit one of your ships!\n")
        computer_score += 1
        player_board.board[row][col] = 'X'
    else:
        print(Fore.YELLOW + "The computer missed!\n")
        player_board.board[row][col] = 'O'


def check_winner(player_name, player_score, computer_score):
    """
    Check who the final winner is
    Prints the game outcome
    """

    if player_score == 4:
        print(Fore.GREEN + f"Congratulations {player_name}! You sank all" +
              " the ships!\n")
    elif computer_score == 4:
        print(Fore.RED + f"Sorry, {player_name}! The computer" +
              " sank all your ships! Better luck next time!\n")


def play_again():
    """
    The play_again function makes it easy to start a new game
    by typing in 'y'
    If the player chooses'no' a goodbye message prints and the game
    exists
    If the player enters the wrong input an error message prints
    """
    while True:
        play_again_input = input("Would you like to start a" +
                                 " new game? (y/n): ").strip().lower()

        if play_again_input == 'y':
            return True
        elif play_again_input == 'n':
            print(Style.BRIGHT + Fore.MAGENTA +
                  "Thanks for playing! Bye for now!")
            return False
        else:
            print(Back.RED + "Invalid input! Please enter 'y' for" +
                  "yes or 'n' for no.")


def play_game():
    """
    Runs all the program functions

    """
    welcome_message()
    player_name = player_name_input()

    while True:

        # Display the player's and computer's board
        player_board = Boards()
        computer_board = Boards()

        # Initialize guesses
        player_guesses = set()
        computer_guesses = set()

        global player_score, computer_score
        player_score = 0
        computer_score = 0

        # Put the titles above the boards
        while player_score < 4 and computer_score < 4:
            player_board.display_boards(board_title=f"{player_name}'s Board:",
                                        show_ships_pos=True)
            computer_board.display_boards(board_title="Computer's Board:",
                                          show_ships_pos=False)

            player_guess(player_board, computer_board, player_guesses)
            computer_guess(player_board, computer_guesses)

        # Checks for a tie
        if player_score == 4 and computer_score == 4:
            print(Style.BRIGHT + Fore.YELLOW + "The game is a tie!")

        else:
            # Checks for the winner
            check_winner(player_name, player_score, computer_score)

        if not play_again():
            break


if __name__ == "__main__":
    play_game()
