# Create a function that checks if two strings are anagrams
def anagramCalculator(string1, string2):
    if len(string1) == len(string2):
        charList = []
        for i in range(len(string1)): # both strings should be same length
            charList.append(string1[i])
        for j in range(len(charList)):
            if charList[j] in string2:
                return True
    return False

print(anagramCalculator('bored','robed'))