import random

def random_ints(start,end,frequency):
    new_list = []
    for i in range(frequency):
        new_list.append(random.randint(start,end))
    return new_list

    
print(random_ints(1,10,5))