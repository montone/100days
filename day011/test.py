# def testFunction(myList):
#     print("Checking myList...")
#     if not myList:
#         print(f"myList is empty")
#     else:
#         print(f"myList is not empty and it has the length of is {len(myList)} long")

# myList = []

# testFunction(myList)
# myList.append("mike")
# myList.append("joe")
# myList.append("nancy")
# myList.append("caroline")

# testFunction(myList)

def testFunction(myList):
    myList.append("mike")
    myList.append("joe")
    myList.append("nancy")
    myList.append("caroline")

    

myList = []

print("Checking myList, first pass...")

if not myList:
    print(f"myList is empty")
else:
    print(f"myList is not empty and it has the length of is {len(myList)} long")

print("Checking myList, first second...")

testFunction(myList)
if not myList:
    print(f"myList is empty")
else:
    print(f"myList is not empty and it has the length of is {len(myList)} long")


