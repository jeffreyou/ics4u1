# String cleaning
# Removes non-alphabetical characters and returns lowercase version of cleaned string 

userInput = input()

def stringCleaner(rawText):
    ''' Removes given string of any non-alphabetical characters and returns lowercase version of cleaned string

    Args: 
        rawText = given text to clean

    Returns: 
        cleaned string
    '''
    for i in range(len(rawText)):
        if not rawText[i].isalpha():
            cleaned = rawText.replace(rawText[i], '') # Cleans non-alphabetical charcaters
    return cleaned.lower() # Lowercases entire cleaned string 

print(stringCleaner(userInput)) # Need to call function 
        