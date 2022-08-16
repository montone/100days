#!/usr/bin/env python3

print("Welcome to the tip calculator!")
bill_amt = input("Enter the total amount of the bill: ")
tip_perc = input("Enter the percentage of tip you'd like to apply (12, 15, 20): ")
num_people = input("Enter how many people to divide the bill by: ")

print(f"The bill came to: {bill_amt}")
print(f"The bill tip is: {tip_perc}")
print(f"Divide the bill by: {num_people}")

bill = float(bill_amt)
tip = bill * (int(tip_perc)/100)
total = bill + tip
average = total / int(num_people)
check = average * int(num_people)
print(f"bill: {bill}")
print(f"tip:  {tip}")
print(f"total: {total}")
print(f"Each person owes: {average}")
#print(f"Check work: does calculated: {check} equal total + tip: {total}")
