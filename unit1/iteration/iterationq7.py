# Calculates the average of the inputted marks 
# Assuming input is entered as "mark, mark, mark"
mark = input() # Assuming input is between 0-100
markList = mark.split(',') # Separating input 
markSum = 0

for i in range(0, len(markList)): # Iterating through entire list
    markSum += int(markList[i])

print(f"Average: {markSum / len(markList)}")


