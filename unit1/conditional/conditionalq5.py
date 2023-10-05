x = int(input())
y = int(input())

if x > 0: # Quadrant 1 or 4 (x is postive)
    if y > 0:
        print(1)
    else:
        print(4)
else: # Quadrant 2 or 3 (x is negative)
    if y > 0:
        print(2)
    else:
        print(3)