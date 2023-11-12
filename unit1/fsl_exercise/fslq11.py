# Create a function that returns a list of factors of the integer argument
def factors_list(user_int):
    ''' Returns list of factors given integer
    Args:
        user_int = int argument, number to return factors of
    
    Return:
        factors = list datatype, returns list of factors of user_int
    '''
    factors = []
    for i in range(1,user_int + 1):
        if user_int % i == 0:
            factors.append(i)
    return factors
user_int = int(input())
print(factors_list(user_int))
