# Print pattern n amount of times
# E.X input n = 5
# Output:
# 1
# 10
# 101
# 1010
# 10101
# Print 1 if odd, 0 if even
n = int(input())
print()

def patternCreator(n):
    ''' 
    
    '''
    for j in range(1,n+1): # Vertical Line Counter
        pattern_string = []
        count = 0
        for i in range(1,j+1): # Horizontal Line
            if i % 2 == 0:
                pattern_string.append('0')
            else:
                pattern_string.append('1')
        pattern_string = ''.join(pattern_string)
        print(pattern_string)
patternCreator(n)
