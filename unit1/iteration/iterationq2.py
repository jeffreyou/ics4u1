num = int(input())

if num > 1:
    for i in range(1, num + 1, 1): # If don't want to include 1 and itself, change to 2 and remove + 1
        if num % i == 0:
            print(i)
else:
    print("Please input a positive integer")
