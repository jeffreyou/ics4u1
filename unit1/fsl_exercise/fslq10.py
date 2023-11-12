# Create a function that removes duplicates from given list 
def duplicate_remover(raw_list):
    ''' Removes duplicates of given list
    Args:
        raw_list: inputted list to be cleaved

    Return:
        new_list: list cleaned of any duplicates
    '''
    new_list = []
    for item in raw_list:
        if item not in new_list:
            new_list.append(item)
    return new_list
print(duplicate_remover(['a','b','b','c','d','d']))