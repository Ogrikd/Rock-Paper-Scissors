import random

# 1. Define the possible choices
choices = ['rock', 'paper', 'scissors']

# 2. Get the user's choice
# A while loop is used to ensure the user enters a valid choice.
while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice in choices:
        break  # Exit the loop if the choice is valid
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

# 3. Generate a random choice for the computer
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}\n")

# 4. Determine the winner based on the rules
if user_choice == computer_choice:
    print("Draw")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'scissors' and computer_choice == 'paper') or \
     (user_choice == 'paper' and computer_choice == 'rock'):
    print("You win!")
else:
    print("You lose!")