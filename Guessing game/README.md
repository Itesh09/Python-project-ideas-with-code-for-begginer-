Guessing Game using python-project for beginner.
This project is a simple guessing game implemented in Python, suitable for beginners to practice their programming skills. The game generates a random number, and the player has to guess the number within a limited number of chances.
We are going to use-:if else
				:while loop
				:Random function
					 
About the Code
The Python Guessing Game project consists of a single Python script (guessing_game.py) that contains the entire game logic.
Features
* Generates a random number for the player to guess.
* Allows the player to input their guess and provides feedback on whether the guess is too high, too low, or correct.
* Limits the number of guesses the player can make.
* Simple and easy-to-understand code, suitable for beginners.
Code explanation

I have imported random in build function in python which generate random number between 1 to 100 and store it in variable n . 


Here I have created function def play_game() inside the whole code is there. The main  reason for creating function is after the game it will ask you if you play again or not. NO necessary for running code again and again
Main logic:
Logic is that code will generate random variable and store in n and ask user to enter number and store it in variable num:
 We are comparing  if : n and num are equal or not if equal You won
If not we are checking which one is greater and printing user input is small or greater that will give hint to   player.
One wrong  guess-print message and reducing chance.
if n!=num:
        
                    if num<n:
                        print("You guess is small try again")
                    elif num>n:
                        print("your  guess is greater try again")
                    else:
                     print("YOUR WON Correct guess")
                     return True

                    chance-=1
                    print("remaining chances  are\n ",chance)
                    if chance==0:
                     print("YOU LOSE  try again the corect number was",n)
                     return False
		
