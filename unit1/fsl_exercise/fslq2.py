# String palindrome calculator
# Palindrome: Where the term is the same reversed e.x tacocat

rawText = input()

if rawText[::-1] in rawText:
    print(f"{rawText} is a palindrome")


