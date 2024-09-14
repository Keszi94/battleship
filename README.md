# Battleship

Welcome to my Python terminal battleship game! This game runs in the Code Institute mock terminal on [Heroku](https://id.heroku.com/login).

The users main goal is to sink all the computer's ships before the computer sinks theirs. There are 4 ships on both boards each taking up one cell.

[Here is the live version of my project](https://battleship-by-keszi-7455bc4bf0ea.herokuapp.com/)

[View Battleship on Github pages](https://github.com/Keszi94/battleship)

![Am i responsive](readme_images/amiresponsive.png)

### How to play

This game is based on the classic paper/board game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

* The player enters their name and two boards are randpmly generated with 4 ships on each.

* The computer's ships are hidden, while the player's ships are visible throughout the game.

* The guesses are indicated with an 'O' while hits display with an 'X'.

* In each turn the player and the computer makes a guess and try to sink the other player's ships.

* The winner is declared after one of the players lost all their ships.

I hope you will enjoy playing Battleship as much as I enjoyed creating it! Happy gaming!

- - - 

## CONTENTS
 
* [Features](#features)
   
* [Data Model](#data-model)   

* [Testing](#testing)
   * [Manual Testing](#manual-testing)
   * [Bugs](#bugs)
   * [Validator Testing](#validator-testing)

* [Deployment](#deployment) 

* [Credits](#credits)
   * [Code Used](#code-used)
   * [Content](#content)
   * [Design Tools](#design-tools)
   * [Acknowledgments](#acknowledgments)




## Features    

* Taking player's name input

*  Input validation
      
   * player can not enter numbers only letters
   * can not enter anything over 10 characters

 ![name input](readme_images/nameinput.png)

* Random board generation
  * ships are randomly placed on both the player and computer boards
  * the player can not see where the computer's ships are
  * the player's ships are always visible

 ![boards](readme_images/boards.png)

* play against the computer
* accepts user input

 ![row input](readme_images/rowinput.png)

* keeps scores
   
    * To see these statements the player has to scroll up in the terminal, which can be a minor inconvenience to people who find it easier to process information by reading a string rather than seeing the visual cues on the board.  

 ![row guess](readme_images/rowguess.png)

* Input validation and error-checking in guess input
  * player can not enter coordinates outside the size of the grid
  * player must only enter numbers
  * can not enter the same guess twice 

 ![invalid guesses](readme_images/invalidguesses.png)

* data maintained in class instances

- - - 

## Data Model

![Flowchart](readme_images/flowchart.png)

1. __Game Boards__ _(Class Boards)_

 * I used a class to represent the boards which helps manage the placement of the ships and the grid's structure. It ensures that ships are placed randomly on the boards at the start of the game and provides a method to also display said boards.
 * The boards for both the player and the computer are represented as 2D grids with the default size of 5x5. The grids store the ship, hits and misses locations.
 * Each cell in the grid can contain:
     * Ship: A ship is placed in th cell, displays as __'S'__
     * Hit : Result of a player/computer guess that hits a cell with a ship, displays as __'X'__
     * Miss : Result of a player/computer guess that hits an empty cell, diplays as __'O'__
     * Empty space: Means no ship or guess is present in the cell

2. __Ship Placement__ _(place_ships)_

 * Both the player and the computer have 4 ships that are placed randomly on their boards.
 * The board class handles the placement of the ships, ensuring that the ships are placed randomly, that they are all placed within the boundaries of the grid and that there are now two ships overlapping each other.

3. __Tracking Guesses__ _(player_guess, computer_guess)_

 * All guess coordinates are tracked to ensure that no location is checked more than once.
 * The guesses are stored in sets to make it easy to check if a guess has already been played or not.
 * After each guess, the board is updated to show if the guess was a miss or a hit, and then the information is displayed to the player.

4. __Managing Scores__ _(player_guess, computer_guess, check_winner)_

 * The game keeps separate scores for the player and the computer. These show the number of successful hits.
 * The score is updated after each round if a hit was made. The game continues on until one player sinks all of the other opponent's ships or if both hit 4 ships at the same time. 

5. __Restarting the Game__ _(play_again)_
 
 * At the end of each game, the player is given the option to restart. If they choose not to play, the game displays a goodbye message. If they decide to play again, the game resets the boards, ships and the scores.

6. __Complete Game Flow__ _(play_game)_
 
 * At the start, the game prints a welcome message with the rules and asks the player to input their name _(welcome_message)_. 
 * Two boards are created, both the same structure, one for the player, the other for the computer. Both boards get 4 randomly placed ships but only the player's ships are visible.
 * The gameplay consists of the player and the computer taking turns to guess a grid location on the other's board. After each guess:
    * The result of the turn is displayed on both boards and recorded (rows/columns guessed, any hits or misses). 
    * Results of each turn are also printed above the boards.  
 * The loop continues on until one player sinks all of their opponent's ships. If they do, they are declared as the winner. If both players hit the last ship on the other's board in the last round, the game is declared a tie.
 * After the outcome of the game is determined the player is given the option to play again or exit the game.  

- - - 

## Testing

I have manually tested this project by doing the following:
 * Checked my code for problems using [PEP8](https://pep8ci.herokuapp.com/).
 * Given invalid inputs: strings when numbers are expected, out of bounds inputs, repeat inputs
 * Tested in my local terminal and the Code Institute Heroku terminal
 * I used [Online python](https://www.online-python.com/) to test my code and logic, allowing me to avoid making major changes on Gitpod and and making comparisons easier.

### Manual Testing


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Player name input | Game starts, after valid input it should appear above the player's board | typed valid name within the character limit | The game started, input appeared as expected | Pass |
| Invalid player name input | Error message should display when input includes special characters, numbers or if it is too long | typed in special characters, numbers and more than 10 characters | Error message displayed | Pass |
| Guess row/column input | If valid number (1-5) is typed in the input is accepted, the guess is processed | Entered valid number, 1-5 | Input is accepted, the guess is registered in the game | Pass |
| Invalid guess row/column input | Error message should display if letter or out of range value is entered | Typed in a letter and numbers out of range | Error message displayed | Pass |
| Player hit detection | hit should display on computer's board in the guessed cell with an 'X', round outcome message should display | played rounds until I hit a ship on the computer's board | 'X' displayed on the board in the right cell, round outcome message displayed | Pass |
| Player miss detection | miss should display on computer's board in the guessed cell with an 'O', round outcome message should display | played rounds until I hit an empty cell on the computer's board | 'O' displayed on the board in the right cell, round outcome message displayed | Pass |
| Computer hit detection | hit should display on player's board in the guessed cell with an 'X', round outcome message should display | played rounds until the computer hit a ship on the player's board | 'X' displayed on the board in the right cell, round outcome message displayed | Pass |
| Computer miss detection |  miss should display on player's board in the guessed cell with an 'O', round outcome message should display | played rounds until the computer hit an empty cell on the player's board | 'O' displayed on the board in the right cell, round outcome message displayed | Pass |
| Tie scenario | Game should be declared a tie in the game outcome message when both players get 4 points in the same round | Played game until both me and the computer sank the 4th ship in the last round | "Game is a tie" message displayed | Pass |
| Player win | Player is declared winner in the game outcome message after reaching 4 points before opponent | Played game until I sunk all the computer's ships | "You win" message displayed | Pass |
| Computer win | Computer is declared winner in the game outcome message after reaching 4 points before opponent | Played game until computer sunk all the player's ships | "Sorry, computer wins" message displayed | Pass |
| Play again input - 'y' (yes) | A new game should start after player enters 'y' | Entered 'y' in input field | A new game started. New boards printed, scores were reset | Pass |
| Play again input - 'n' (no) | A goodbye message should print before the game ends | Entered 'n' in input field | Goodbye message displayed and the game ended | Pass |
| Invalid play again input | Error message should display when invalid input is entered | Typed in numbers, special characters and words | Error message displayed | Pass |

### Bugs

#### Solved Bugs

1. When trying to test how the boards would display after creating the Boards Class, the terminal gave me an IndentationError; all the functions meant to be inside the Boards Class were outside of it. 

2. Originally, I used tabulate to design my boards, but the two boards displayed with a significant size difference. I tried several methods to fix this issue, but none gave me the desired result. I decided to abandon using tabulate and created my own board styles manually instead 

3. During one of my test runs, after I entered my guesses, my results were printed, but instead of the expected computer's guess below mine, I received an error message in the terminal. This issue occurred because I mistakenly used the player_guesses parameter in the computer_guess function definition instead of computer_guesses. 

4. During testing, I realized that whenever both boards had 4 hits on the last turn, the player was incorrectly declared the winner. This occurred because there was no logic to determine a tie outcome. Additionally, the check_winner function contained an if/else statement that checked if the player_score was equal to 4 but did not consider the computer_score. I resolved this by replacing the if/else with an if/elif statement and added logic in the play_game function to check for a tie before evaluating the scores.

5. While testing the play_again input in my terminal, I noticed that it accepted the 'y' character correctly and restarted the game as intended. However, any character other than 'n' also caused the game to exit. This issue occured because the if/else statement in the play_again function only checked if the input was 'y' or not 'y'. I resolved this by creating a new play_again function outside of play_game, using a while loop to check for both 'y' and 'n' inputs with if/elif, and using else to print an invalid input error message. 

6. During my latest testing of the name input function, I noticed that while the error message displayed correctly for invalid input, repeating the invalid input immediately would still trigger the error message but allow the game to start anyway. I fixed this by placing the if/else statement inside a while loop. Now, the game won't start until the player provides the correct input.

### Validator Testing

* Testing done using PEP8, no errors detected:

![PEP8 test](readme_images/pythonlinter.png)

- - - 

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

* Steps for deployment:
  * Fork or clone this repository
  * Create a new [Heroku](https://id.heroku.com/login) app
  * Set the buildbacks to _Python_ and _NodeJs_ in that order
  * Link the Heroku app to the repository
  * Click on __Deploy__

- - -

## Credits

### Code Used

* I used [this Youtube tutorial](https://www.youtube.com/watch?v=Ej7I8BPw7Gk&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i&ab_channel=DrCodie) to help me with creating the game logic.
* I used [colorama](https://pypi.org/project/colorama/) to enhance the game's visual appeal and user experience by adding color to some of the text.

I have used the following websites to gather relevant information during my research:
* [Stackoverflow](https://stackoverflow.com/)
* [Reddit](https://www.reddit.com/)
* [Thecodingforums](https://www.thecodingforums.com/)
* [W3Schools](https://www.w3schools.com/)
* [Python.org](https://www.python.org/)

### Content

* I created my Readme file based on [Kera Cudmore's](https://github.com/kera-cudmore) [Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club) and [TheQuizArms](https://github.com/kera-cudmore/TheQuizArms) Readme files.

### Design Tools

I used [Lucidchart](https://lucidchart.com/) to create the flowchart that visualizes the game's structure and logic.

### Acknowledgments

I would like to acknowledge the following people who helped me along the way in completing my third milestone project:

* [Graeme Taylor](https://github.com/G-Taylor), my Code Institute Mentor.
- - -
