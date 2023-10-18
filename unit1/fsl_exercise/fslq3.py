userInput = input()

def consonantCalculator(rawText):
    consonantCount = 0
    for character in rawText:
        character = character.lower()
        if character not in {'a','e','i','o','u'}:
            consonantCount += 1
    return consonantCount

print(consonantCalculator(userInput))
