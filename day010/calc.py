############################################################################
# Name: calc.py
# Date: 2025-02-09
# Author: TBD
############################################################################
# Purpose: Hundred Days of Code: Day 10
#
############################################################################
# Revisions:
#
# Notes: Where the hell is art.log file?
############################################################################

import art

def calculator():

    print(art.logo)
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    # function dictionary$
    operations = {
        "+": add,
        "=": subtract,
        "*": multiply,
        "/": divide,
    }

    should_accumulate = True
    n1 = float(input("Enter a number: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What is the next number: "))

        print(f"Using n1: {n1} and n2: {n2} Operation {operation_symbol}")
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()