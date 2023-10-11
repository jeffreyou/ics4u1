perfectSum = 0
for i in range(1,10001): # Iterating through all numbers til 10000
    factorSum = 0
    for j in range(1, i): # Finding factors
        if i % j == 0:
            factorSum += j
    if factorSum == i: # Printing perfect number
        perfectSum += i

print(perfectSum)


