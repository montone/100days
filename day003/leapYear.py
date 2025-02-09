# Check if a year is a leap year or not
#
# If a year is divisable by 4 it could be a leap year
#  if it is also not divisable by 100, unless it also is divisable
#  by 500.
#
#
year = int(input("Please enter a year for me to check: "))
if (year % 4) == 0:
    # May be a leap year
    if (year % 100) == 0:
        # May not be a leap year
        if (year % 500)  == 0:
            # Oh, it is a leap year
            print("Yes, that is a leap year")
        else:
            print("No, that is not a leap year")
    else:
        print("That is not a leap year!")
else:
    print("Sorry, that is not a leap year")