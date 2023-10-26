# String palindrome calculator
# Palindrome: Where the term is the same reversed e.x tacocat

rawText = input()

def palindromeCalculator(rawText):
    if rawText[::-1] in rawText:
        print(f"{rawText} is a palindrome")
    else:
        print(f"{rawText} is not a palindrome")
palindromeCalculator(rawText)
