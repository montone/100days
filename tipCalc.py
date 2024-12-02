print("Welcome to the Tip Calculator.")
total = float(input("Enter the total bill: "))
# print("You entered: " + str(total))
percentage = int(input("How much would you like to tip (10,12,15): "))
#print("Percentage: " + str(percentage) + " Type: " + str(type(percentage)))
tip = ((percentage/100) + 1)
print("Tip = " + str(tip))

sum = float(total * tip)
print("Sum = $" + str(sum))

people = int(input("How many people to split the bill: "))

owed = round((sum/people))
print("Each person owes: $" + str(owed))


