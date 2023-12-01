'''
Q2) Exponentiation

Write a program that evaluates the power to its integer representation.

2^4 = 2 x 2 x 2 x 2 = 16
'''
count = 0
product = 0
def exponentitation(base,power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return exponentitation(base,power-1) * base # Example of tail solution, calls function at the end
print(exponentitation(2,4)) 

    

    