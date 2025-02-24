############################################################################
# Name: BlackJack.py
# Purpose: Simulate the game of blackjack.
# Lesson: 100 Days of Code: Day 10.
#
# Author: Mike Montone
# Date: 02/21/2025
#
############################################################################
# Revisions: 1.0
#
############################################################################
import random

# # Initial setting to play is set to True
# play = True

# # While play is true, play game
# while play:
    
#     playGame = input("Would you like to play a game of blackjack, Y/N? ")

#     if playGame == "Y" or playGame == "y":

#         print("Let's play!")

#     elif playGame == "N" or playGame == "n":

#         print("Good bye.")

#         play = False

#     else:

#         print("Response was invalid.")

def card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]
    #cards = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    #num = random.randint(1,11)
    #print(f"Random index: {num}.")
    #randomCard = cards[num]
    #print(f"RandomCard: {randomCard}.")
    randomCard = cards[random.randint(1,11)]
    #print(f"My random card: {randomCard}.")
    return randomCard
    #print(cards)
    #print(num)
    #dealerCardOne = cards(num)
    #print(f"Your card is: {dealerCardOne}.")

def deal():
    dealerCardOne = card()
    dealerCardTwo = card()
    usersCardOne = card()
    usersCardTwo = card()
    dealersTotal = dealerCardOne + dealerCardTwo
    usersTotal = usersCardOne + usersCardTwo
    print(f"Dealer card one: {dealerCardOne}.")
    print(f"Dealer card two: {dealerCardTwo}.")
    print(f"Users card one: {usersCardOne}.")
    print(f"Users card two: {usersCardTwo}.")
    
    if dealersTotal > 21:

        # Check if either of the cards is an ace, if so, convert to a 1
        if dealerCardOne == 11:

            dealerCardOne = 1
            print(f"Dealer card one is an ace, converting to a 1.")

        elif dealerCardTwo == 1:

            dealerCardTwo = 1
            print(f"Dealer card two is an ace, converting to a 1.")
        
        else:

            print(f"Dealer busted: {dealersTotal}!")

    elif usersTotal > 21:

        # Check if either of the cards is an ace, if so, convert to a 1
        if usersCardOne == 11:

            usersCardOne = 1
            print(f"User card one is an ace, converting to a 1.")

        elif userCardTwo == 1:

            userCardTwo = 1
            print(f"User card two is an ace, converting to a 1.")
        
        else:

            print(f"You busted: {usersTotal}!")

    else:
        print(f"Dealer has: {dealersTotal}.")
        print(f"User has: {usersTotal}.")



deal()



#print{f"Dealer's total: {dealersTotal}."}
#print{f"Your total: {usersTotal}."}

    # dealerTotal
    # userTotal

    # if dealerTotal == 21 and userTotal == 21:
    #     print(f"Dealer has {dealerTotal} and User has {userTotal}, so the game is a draw.")
    #     exit 
    # elif dealerTotal == 21
    #     dealerWins
    #     exit 
    # elif userTotal == 21
    #     userWins 
    #     exit 
    # else
    #     print dealerCardOne
    #     print userTotal
    #         ask for another card
    #         if yes
    #             draw cards
    #         if no
    #             stand
    #             dealer draws

    # if card = 1:
    #     if cardTotal > 21, set card to 1
        