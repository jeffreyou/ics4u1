# Printing nth Fibonacci Sequence 
num = int(input())
digit1 = 0 # F(0)
digit2 = 1 # F(1)
fibonacciNum = 0 # F(2)

for i in range(2, num+1): # fibonacciNum  starts at F(2)
    fibonacciNum = digit1 + digit2
    digit1 = digit2
    digit2 = fibonacciNum
    
print(fibonacciNum)


    