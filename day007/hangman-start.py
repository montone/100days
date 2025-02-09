#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

word = word_list[random.randint(0,2)]
print(word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# Using .lower() function after input, interesting.
guess = input("Guess a letter: ").lower()
#print("Your guess is: " + guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

number = 0
good_guess = 0
for letter in range(0, len(word)):
    if word[letter] == guess:
        print("Hit! : " + word[letter])
        good_guess += 1
    number += number

if good_guess >= 1:
    print("Good guess!")
else:
    print("Bad guess")