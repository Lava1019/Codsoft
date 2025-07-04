import random

# Prompt the user
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Computer randomly chooses
options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)

# Display choices
print("You chose:", user_choice)
print("Computer chose:", computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'scissors' and computer_choice == 'paper') or \
     (user_choice == 'paper' and computer_choice == 'rock'):
    print("You win!")
else:
    print("Computer wins!")