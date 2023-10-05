num = int(input())
count = 0


for i in range(2, num - 1, 1):
    if num % i == 0:
        count += 1
        # Could also break and print "not a prime number" here

if(count == 0):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")