line = input("Enter a string: ")
sum = 0

for x in range(len(line)):
    sum += ord(line[x])

print(f"Number of ASCII characters: {sum}")
