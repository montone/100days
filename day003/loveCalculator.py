# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if name1 and name2:

    name1_lower = name1.lower()
    name2_lower = name2.lower()

else:
    print("You failed to enter two names.  Exiting")
    exit(1)


t11 = name1_lower.count("t")
r11 = name1_lower.count("r")
u11 = name1_lower.count("u")
e11 = name1_lower.count("e")
t21 = name2_lower.count("t")
r21 = name2_lower.count("r")
u21 = name2_lower.count("u")
e21 = name2_lower.count("e")

l12 = name1_lower.count("l")
o12 = name1_lower.count("o")
v12 = name1_lower.count("v")
e12 = name1_lower.count("e")
l22 = name2_lower.count("l")
o22 = name2_lower.count("o")
v22 = name2_lower.count("v")
e22 = name2_lower.count("e")

true_tally = t11 + r11 + u11 + e11 + t21 + r21 + u21 + e21
love_tally = l12 + o12 + v12 + e12 + l22 + o22 + v22 + e22

names_string = str(true_tally) + str(love_tally)
names_tally = int(names_string)

#print(f"Name1 T: {t11 + t21}")
#print(f"Name1 R: {r11 + r21}")
#print(f"Name1 U: {u11 + u21}")
#print(f"Name1 E: {e11 + e21}")
#print(f"Name1 L: {l12 + l22}")
#print(f"Name1 O: {o12 + o22}")
#print(f"Name1 V: {v12 + v22}")
#print(f"Name1 E: {e12 + e22}")

#print(f"names concatenated is: {true_tally}{love_tally}")
#print("names_string: " + names_string)

if names_tally <= 10 or names_tally >= 90:
    print(f"Your score is ***{names_tally}***, you go together like coke and mentos")
elif names_tally >=40 and names_tally <= 50:
    print(f"Your score is ***{names_tally}***, you are alright together")
else:
    print(f"Your score is ***{names_tally}***.")