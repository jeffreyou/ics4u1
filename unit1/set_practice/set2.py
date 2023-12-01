# Create a function that compares if two lists are unique, as in, both lists don’t have the same values
# **Without sets**

def unique_list(list1,list2):
    for i in range(max(len(list1),len(list2))):
        if list1[i] in list2:
            return False
    return True
print(unique_list([1,2,3],[4,5,6]))

# By using sets, create the same functions above
def unique_list2(list1,list2):
    sym_diff = set(list1) ^ set(list2)
    if len(sym_diff) == len(list1) + len(list2):
        return True
    else:
        return False
print(unique_list2([1,2,3],[4,3,6]))