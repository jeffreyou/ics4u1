# Takes two strings and return sorted list of common characters 
def duplicate_finder(string1,string2):
    commonCharacters = []
    for character in string1: # see if characters in one string match the other
        if character in string2:
            commonCharacters.append(character)
    return sorted(commonCharacters)
print(duplicate_finder('hello','goodbye'))