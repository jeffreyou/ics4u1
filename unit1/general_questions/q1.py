# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Brute Force: 5m Runtime

def smallest_num():
    is_divisible = False
    num = 20
    while is_divisible is False:
        is_divisible = True # Has to reset through each iteration 
        for i in range(1,20):
            if num % i > 0: # num is NOT evenly divisible by numbers from 1-20
                is_divisible = False
                break # Avoids unecessary iterations 
        num += 1
    return num # Will only pass if num is divisible by numbers from 1-20
print(smallest_num())