num = int(input())
fibonacciNum = 2
digit1 = 0
digit2 = 1

while fibonacciNum < num:
    print(digit1)
    digit1 = digit1 + digit2
    if fibonacciNum < num:
        print(digit2)
        digit2 = digit1 + digit2
    fibonacciNum += 1


    