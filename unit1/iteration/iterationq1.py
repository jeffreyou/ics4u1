
n = int(input())
product = n
'''
for i in range(n, 0, -1):
  product *= i

print(product)
''' # Factorial Calculator using For Loop

count = n
while count > 0:
    product *= count
    count -= 1

print(product) # Factorial Calculator using while loop




  
  