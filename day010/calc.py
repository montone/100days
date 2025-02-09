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
#
############################################################################

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

n1 = input("Enter a number: ")
n2 = input("Enter a number: ")
todo = input("Enter an operation using the following symbols +, -, * or /: ")

print(f"You would like to {todo} using {n1} and {n2}")
print(operations[todo](n1, n2))

