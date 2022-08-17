#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in pounds: "))
# 🚨 Don't change the code above 👆

# Convert metric to imperial
kgPerPound = float(0.45359237)
metersPerInches = float(0.0254)
convertPounds = weight * kgPerPound
convertInches = height * metersPerInches


sum = (float(convertPounds)/(float(convertInches) ** 2))
print("BMI: " + str(round(sum, 2)))

#Write your code below this line 👇

if sum >= 35:
   print("You are clinically obese.")
elif sum >= 30:
    print("You are obese.")
elif sum >= 25:
    print("You are overweight.")
elif sum >= 18.5:
    print("You are normal weight.")
else:
    print("You are underweight.")
