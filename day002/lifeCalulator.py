#!/usr/bin/env python3
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

current_age = int(age)
max_age = 90
years_till_max = max_age - current_age
months_till_max = max_age * 12

weeks_till_max = max_age * 52
days_till_max = weeks_till_max * 7
print(f"If you live until you are 90, you have\n{years_till_max} years left, \n{months_till_max} months left, \n{weeks_till_max} weeks left, \n{days_till_max} days left, \nuntil you reach 90")



