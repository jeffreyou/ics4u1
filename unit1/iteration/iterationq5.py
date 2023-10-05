num = int(input())
factors = []
highestFactor = 0

for i in range(1, num):
    count = 0
    for j in range(1, num): # used to iterate through each num to check factor
        if i % j == 0:
            count += 1
            if count > highestFactor:
                highestFactor = i
print(f"the highest factor of {num} is {highestFactor}")
    
        