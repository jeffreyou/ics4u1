# Write a program that can find the prime factors of a number
# Step 1: Take input
# Step 2: Find factors
# Step 3: Determine if factor is prime
num = int(input())

for i in range(2,num):
    if num % i == 0: # Finds factors
        count = 0
        for j in range(2,i): # Checking if factor prime number
            if i % j == 0:
                count += 1
        if count == 0:
            print(i)
        


