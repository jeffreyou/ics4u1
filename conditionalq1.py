num = int(input("Enter a non negative integer: "))

if num < 0:
    print("Invaild: Negative integer");
else:
    if num % 10 == 2 or num % 10 == 8:
        print(num, "is 2 away from a multiple of 10.")
    else:
        print(num, "is NOT 2 away from a multiple of 10.")