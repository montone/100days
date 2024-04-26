#!/usr/bin/env python3

############################################################################
#
# Author: Mike Montone
#
# Date: 04/26/2024
#
# Purpose: Tip calulator
#
############################################################################
# Revisions:
#	- Removed percentages from prompt.
#
############################################################################

print("Welcome to the tip calulator.")
bill = float(input("What was the total of the bill? "))
percent = int(input("How much tip would you like to give? 10, 15, or 20 "))
people = int(input("How many people are splitting the bill? "))

tip = round(bill * (percent / 100), 2)
owe = round(tip / people, 2)
total = round(tip + bill)

print(f"Your bill total is: {total}")
print(f"The tip total comes to: {tip}")
print(f"Each person owes {owe}")
print(f"Total owed is bill {bill} + tip {tip} = {total}")
