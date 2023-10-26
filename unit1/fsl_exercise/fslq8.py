# Create a function that takes in a string with comma separated values and returns a list of integers
def commaSeparated(text):
    return text.split(',')
userInput = input()
print(commaSeparated(userInput))