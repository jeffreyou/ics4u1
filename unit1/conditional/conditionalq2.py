counter = 0

for i in range(6):
    result = input()
    if 'W' in result:
       # counter = counter + 1  ALTERNATIVE WAY
       counter += 1
    elif not('L') in result:
        print("Invaild input, please enter \"W\" or \"L\"")

if counter >= 5:
    print(1)
elif counter >= 3 and counter <= 4:
    print(2)
elif counter >= 1 and counter <= 2:
    print(3)
else:
    print("Eliminated")
