import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

##Write your code below this line 👇

# User makes a guess
user_guess_num = int(input("Which do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:"))

# Convert guess to actual text
if user_guess_num == 0:
    print("You chose rock: " + rock)
elif user_guess_num == 1:
    print("You chose paper: " + paper)
else:
    print("You chose scissors: " + scissors)
# add invalid number check

# Program make a guess
prog_guess_num = random.randint(0,2)

# Convert guess to actual text
if prog_guess_num == 0:
    print("The computer chose rock: " + rock)
elif prog_guess_num == 1:
    print("The computer chose paper: " + paper)
else:
    print("The computer chose scissors: " + scissors)
# add invalid number check

# Evaulate guesses

# Same guesses are a push
if user_guess_num == prog_guess_num:
    print("You both guessed the same, no one wins.  It is a push.")

# You guessed rock
if user_guess_num == 0 and prog_guess_num == 1:
    print("Paper covers rock, you lose!")
elif user_guess_num == 0 and prog_guess_num == 2:
    print("Rock breaks scissors, you win!")
# You guessed paper
elif user_guess_num == 1 and prog_guess_num == 0:
    print("Paper covers rock, you win!")
elif user_guess_num == 1 and prog_guess_num == 2:
    print("Scissors cut paper, you lose!")
# You guessed scissors
elif user_guess_num == 2 and prog_guess_num == 0:
    print("Rock breaks scissors, you lose!")
elif user_guess_num == 2 and prog_guess_num == 1:
    print("Scissors cut paper, you win!")



