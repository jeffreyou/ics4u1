'''
Create a function that remove duplicate values from a list with that has N values (without using sets), 
**preserve the single instance of the duplicate**
'''

def duplicate_remover(text):
    new_list = []
    for i in range(len(text)):
        if text[i] not in new_list:
           new_list.append(text[i])
    return new_list
print(duplicate_remover(['a','a','a','b','c','c','d','e','f','f','g']))

# By using sets, create the same function above 
def duplicate_remover2(text):
   return set(text)
print(duplicate_remover2(['a','a','a','b','c','c','d','e','f','f','g']))