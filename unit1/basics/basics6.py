line1 = input()
line2 = input()
line3 = input()

fence = 0

for i in range (len(line1)):
    if line1[i] == 'F':
        fence += 1

for j in range (len(line2)):
    if line2[j] == 'F':
        fence += 1

for k in range (len(line3)):
    if line3[k] == 'F':
        fence += 1

print(fence)
print(fence % 12)
print((fence % 12) * 14.95)
