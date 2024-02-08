 # Import the random module for generating computer's choice
import random 
def get_user_choice():
    """
    Prompt the user to choose rock, paper, or scissors.
    """
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """
    Generate a random choice (rock, paper, or scissors) for the computer.
    """
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's choice and the computer's choice.
    Rock beats scissors, scissors beat paper, and paper beats rock.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    """
    Show the user's choice, the computer's choice, and the result.
    """
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    print(result)

def play_again():
    """
    Ask the user if they want to play another round.
    """
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

# Initialize scores
user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)

    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Score - You: {user_score}  Computer: {computer_score}")

    if not play_again():
        break     