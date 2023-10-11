repeat = True
count = 0
nameList = []

while repeat:
    name = input()
    if name in 'X': # Returns false and ends loop if X is detected
        repeat = False
        break
    nameList.append(name) # Adds name into list
    count += 1

currentMax = len(nameList[0])
maxIndex = 0 # Used to keep track of length corresponding highest index
for i in range(1 , len(nameList)): # Iterates through entire list
    if currentMax < len(nameList[i]):
        maxIndex = i
print(nameList[maxIndex])
