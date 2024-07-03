# Task: Rock Paper Scissors 
# The rules are as follows:
# - Rock beats Scissors.
# - Scissors beat Paper.
# - Paper beats Rock.

# Code:
import random 
print("==================") 
print("Hi! Should we play a simple game of Rock Paper Scissors? \n To remind you, here are the rules: \n")
print(" Rock beats Scissors \n Scissors beat Paper \n Paper beats Rock \n")
print(" 1) ✊ \n 2) ✋ \n 3) ✌")
computer = int(random.randint(1, 3))
player = int(input("Pick a number: "))
if player == 1 and computer == 1:
  print("You chose: ✊ \n Computer chose: ✊ \n It's a tie!")
elif player == 1 and computer == 2:
  print("You chose: ✊ \n Computer chose: ✋ \n Computer wins!")
elif player == 1 and computer == 3:
  print("You chose: ✊ \n Computer chose: ✌ \n You win!")
elif player == 2 and computer == 1:
  print("You chose: ✋ \n Computer chose: ✊ \n You win!")
elif player == 2 and computer == 2:
  print("You chose: ✋ \n Computer chose: ✋ \n It's a tie!")
elif player == 2 and computer == 3:
  print("You chose: ✋ \n Computer chose: ✌ \n Computer wins!")
elif player == 3 and computer == 1:
  print("You chose: ✌ \n Computer chose: ✊ \n Computer wins!")
elif player == 3 and computer == 2: 
  print("You chose: ✌ \n Computer chose: ✋ \n You win!")
elif player == 3 and computer == 3: 
  print("You chose: ✌ \n Computer chose: ✌ \n It's a tie!")
