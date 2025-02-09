print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_or_right = input("left if right?").lower
if left_or_right == "right":
    print("You fell into a hole.\nGame over.")
else:
    swim_or_wait = input("swim or wait?").lower
    if swim_or_wait == "swim":
        print("You've been attacked by a trout.\nGame over.")
    else:
        which_door = input("red, blue, or yellow door?").lower
        if which_door == "blue":
            print("You've been eated by a beast.\nGame over.")
        elif which_door == "red":
            print("You've been burned by fire.\nGame over.")
        else:
            print("You win!")

