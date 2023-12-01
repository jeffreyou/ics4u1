'''
Q3) Palindrome 

Write a program that checks if a word is a palindrome recursively. You may assume that the word is all lowercase and has no special characters nor numbers.

Is tacocat a palindrome? Yes.. yes it is.
'''

def palindrome(text, index = 0):
    if index > len(text) // 2:
        return True
    elif text[index] != text[(-index)-1]:
        return False
    else:
        return palindrome(text,index+1)
print(palindrome("tacocadt"))