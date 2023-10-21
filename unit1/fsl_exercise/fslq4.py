n = int(input())
print("\n")

def patternCreator(n):
    count = 0
    patternSequence = []
    while(n > count):
        if count < n:
            patternSequence[count] = '1'
            count += 1
        if count < n:
            patternSequence[count] = '0'
            count += 1
    finalPattern = ','.join(patternSequence)
    return finalPattern
print(patternCreator(n))