# Create a function that returns true if the given integer is a prime number
def prime_checker(user_int):
    ''' Checks if integer given is prime
    Args:
        user_int = int datatype, integer to determine prime status

    Return:
        True = true if user_int is prime
        False = false if user_int is NOT prime
    '''
    for i in range(2,user_int):
        if user_int % i == 0:
            return False
    return True # Will only pass after iterating through entire for loop
print(prime_checker(18))