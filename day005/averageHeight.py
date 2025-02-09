# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sums=0
items=0
for height in student_heights:
    sums += student_heights[items]
    items += 1

print("Average height is: " + str(round(sums / items)))
#print("Sums equals = " + str(sums))
#print("Items equals " + str(items))