# Takes in input a and b, which is an integer value that's greater than 1 and prints the common factors that they share
a = int(input())
b = int(input())

for i in range(1,a):
    if a % i == 0:
        if b % i == 0:
            print(i)
    