userInput = input()

def consonantCalculator(rawText):
    consonantCount = 0
    for character in rawText:
        character = character.lower()
        if character not in {'a','e','i','o','u'}:
            consonantCount += 1
    return consonantCount

def vowelCalculator(rawText):
    vowelCount = 0
    for character in rawText:
        character = character.lower()
        if character in {'a','e','i','o','u'}:
            vowelCount += 1
    return vowelCount

print(consonantCalculator(userInput))
print(vowelCalculator(userInput))
