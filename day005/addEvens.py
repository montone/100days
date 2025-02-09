total = 0
for number in range(0,101):
    if number % 2 == 0:
        total += number
    else:
        continue

print("All even numbers from 1 to 100 summed equal: " + str(total))

