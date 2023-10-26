# Create a function for mean and median
# Each function takes a single list of integers as an argument

def mean(numList):
    ''' Returns mean or average of list

    Args:
        numList: integer list, list in inputted numbers to find average of

    Returns:
        int, represents average percent of numList argument
    '''
    return (sum(numList) / len(numList))
print(mean([90,95,96,100]))

def median(numList):
    ''' Calculates median (middle of list)
    Args:
        numList: integer list, list of inputted numbers to find median of
    Returns:
        int
    '''
    numList = sorted(numList)
    middle = len(numList) // 2
    if len(numList) % 2 == 0: # Even list length, have to take middle two
        # e.x [1,2,3,4,5,6]
        left = numList[middle]
        right = numList[middle - 1]
        return (left + right) / 2 
    else: # Odd list length, can just take middle term
        return middle
print(median([1,2,3,4,5,6]))

