# Write function that cleans and returns list of whitespaces and non-alphabetical characters

def listCleaner(rawText):
    newList = []
    for i in range(len(newList)): # List index
        newList = rawText[i].strip()
        for j in range(len(newList[i])): # String index
            if not newList[i][j].isalpha:
                newList.replace(newList[i][j], '')
    return newList

print(listCleaner(['a3d%  ', ' aw251%^   ']))