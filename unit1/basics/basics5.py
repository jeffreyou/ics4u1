import random

dc = int(input("Enter the difficulty class: "))
check = random.randint(1,20)
if check > dc:
    print("You passed the check!")
else:
    print("You've failed the check!")
