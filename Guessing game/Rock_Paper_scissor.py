import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
    
        user_choice = input("\nEnter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
            
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")

# Start the game
print("Welcome to Rock-Paper-Scissors!")
play_game()
