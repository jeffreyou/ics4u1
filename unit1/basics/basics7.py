start = input()
placeholder = input()

num_cookies = 0
big_cookies = 0

# Counting cookies
for i in range (len(placeholder)):
    if 'c' in placeholder[i]:
        num_cookies += 1
    elif 'b' in placeholder[i]:
        big_cookies += 1

# Printing total # of cookies sold
print(num_cookies + big_cookies)

# Printing cookie profit
profit = ((num_cookies * 1.25) + (big_cookies * 2.00)) - ((num_cookies * 0.50) + (big_cookies * 0.75))
print(profit)

# Printing total money made
print(profit + start)
