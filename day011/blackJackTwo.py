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

def checkScore():
    pass

def tallyHand(hand):
    
    total = 0
    i = 0
    
    while i < len(hand):
        total = total + hand[i]
        i += 1
    
    return total


def deal(dealersHand, playersHand):
    dealersHand.append(drawCard())
    playersHand.append(drawCard())    
    dealersHand.append(drawCard())
    playersHand.append(drawCard())

def drawCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]
    #cards = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11] # debug statement, forces all aces
    randomCard = cards[random.randint(1,11)]
    #print(f"...drawCard: {randomCard}")    # debug statement
    return randomCard

def playGame():
    pass

dealersHand = []
playersHand = []

deal(dealersHand, playersHand)

print(f"dealersHand size is: {len(dealersHand)}")
print(f"... Dealer, card one: {dealersHand[0]}")
print(f"... Dealer, card two: {dealersHand[1]}")
print(f"... Dealers total: {tallyHand(dealersHand)}")
print(f"playersHand size is: {len(playersHand)}")
print(f"... Players, card one: {playersHand[0]}")
print(f"... Players, card two: {playersHand[1]}")
print(f"... Players total: {tallyHand(playersHand)}")



