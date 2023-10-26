# Given a string of input "A - Z" calculate the score of input
# Letter A has a score of 26
# Letter B has a score of 25
# ...
# Letter Z has a score of 1 

userInput = input()

def scoreCalculator(userInput):
    '''
    Docstring
    '''
    totalScore = 0
    alphabet = 'ABCDEFGHJIKLMNOPQRSTUVWXYZ'[::-1] # Reverses alphabet 
    for character in userInput:
        totalScore += alphabet.find(character) + 1 # Finds index of alphabet string (Adds +1 because Z starts at 1)
    return totalScore

print(scoreCalculator(userInput))