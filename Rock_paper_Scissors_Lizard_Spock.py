# Task: Rock Paper Scissors Lizard Spock
# The rules are as follows:
# - Scissors cut Paper.
# - Paper covers Rock.
# - Rock crushes Lizard.
# - Lizard poisons Spock.
# - Spock smashes Scissors.
# - Scissors beat Lizard.
# - Lizard eats Paper.
# - Paper disproves Spock.
# - Spock vaporizes Rock.
# - Rock breaks Scissors.

# Code:
import random 
print("==================") 
print("Hi! Do you know a simple game of Rock Paper Scissors? Let's add a little twist!")
print("This game is Rock Paper Scissors Lizard Spock! \n To remind you, here are the rules: \n")
print(" Scissors cut Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors beat Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock \n Rock breaks Scissors")
print(" 1) ✊ \n 2) ✋ \n 3) ✌ \n 4) 🦎 \n 5) 🖖")
computer = int(random.randint(1, 5))
player = int(input("Pick a number: "))
if player == 1 and computer == 1:
  print("You chose: ✊ \n Computer chose: ✊ \n It's a tie!")
elif player == 1 and computer == 2:
  print("You chose: ✊ \n Computer chose: ✋ \n Computer wins!")
elif player == 1 and computer == 3:
  print("You chose: ✊ \n Computer chose: ✌ \n You win!")
elif player == 1 and computer == 4:
  print("You chose: ✊ \n Computer chose: 🦎  \n You win!")
elif player == 1 and computer == 5:
  print("You chose: ✊ \n Computer chose: 🖖  \n Spock wins!")
elif player == 2 and computer == 1:
  print("You chose: ✋ \n Computer chose: ✊ \n You win!")
elif player == 2 and computer == 2:
  print("You chose: ✋ \n Computer chose: ✋ \n It's a tie!")
elif player == 2 and computer == 3:
  print("You chose: ✋ \n Computer chose: ✌ \n Computer wins!")
elif player == 2 and computer == 4:
  print("You chose: ✋ \n Computer chose: 🦎  \n Computer wins!")
elif player == 2 and computer == 5: 
  print("You chose: ✋ \n Computer chose: 🖖  \n You win!")
elif player == 3 and computer == 1:
  print("You chose: ✌ \n Computer chose: ✊ \n Computer wins!")
elif player == 3 and computer == 2: 
  print("You chose: ✌ \n Computer chose: ✋ \n You win!")
elif player == 3 and computer == 3: 
  print("You chose: ✌ \n Computer chose: ✌ \n It's a tie!")
elif player == 3 and computer == 4:
  print("You chose: ✌ \n Computer chose: 🦎  \n You win!")
elif player == 3 and computer == 5: 
  print("You chose: ✌ \n Computer chose: 🖖  \n Spock wins!")
elif player == 4 and computer == 1: 
  print("You chose: 🦎 \n Computer chose: ✊  \n Computer wins!")
elif player == 4 and computer == 2: 
  print("You chose: 🦎 \n Computer chose: ✋  \n You win!")
elif player == 4 and computer == 3:
  print("You chose: 🦎 \n Computer chose: ✌  \n Computer wins!")
elif player == 4 and computer == 4:
  print("You chose: 🦎 \n Computer chose: 🦎 \n It's a tie!")
elif player == 4 and computer == 5:
  print("You chose: 🦎 \n Computer chose: 🖖 \n You win!")
elif player == 5 and computer == 1: 
  print("You chose: 🖖 \n Computer chose: ✊ \n Spock wins!") 
elif player == 5 and computer == 2: 
  print("You chose: 🖖 \n Computer chose: ✋ \n Computer wins!")
elif player == 5 and computer == 3:
  print("You chose: 🖖 \n Computer chose: ✌ \n Spock wins!")
elif player == 5 and computer == 4: 
  print("You chose: 🖖 \n Computer chose: 🦎 \n Computer wins!")
elif player == 5 and computer == 5: 
  print("You chose: 🖖 \n Computer chose: 🖖 \n It's a tie!")
