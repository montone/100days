#!/usr/bin/env python3

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You may ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You must pay $12.")
    elif age >= 12:
        print("You must pay $7.")
    else:
        print("You must pay $5.")
else:
    print("Sorry, you are too short to ride the rollercoaster")
    #exit(1)
    #quit(2)