'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divides evenly into n).

Two numbers A and B are amicable numbers and are considered to be an amicable pair if the following is true:
	
	d(A) = B and d(B) = A where A != B.
'''
from math import sqrt

def factor_finder(x):
    factor_list = {1} # Set of factors
    upperbound = (int(sqrt(x) + 1))
    for div in range(2,upperbound): # Only checks half of factors
        if x % div == 0:
            factor_list.add(div)
            factor_list.add(x // div) # Can calculate pairs without checking 
    return factor_list

def amicable_num():
    amicable_sum = 0
    for a in range(1,10000):
        b = sum(factor_finder(a))
        if a == sum(factor_finder(b)):
            amicable_sum += a + b
    return amicable_sum
print(amicable_num())