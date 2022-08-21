# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len_of_list = len(names)
len_for_random = len_of_list - 1
pick = random.randint(0,len_for_random)
print("The bill must be paid by " + names[pick])
# could have used random.randint(0, len_of_list -1) to simplify
