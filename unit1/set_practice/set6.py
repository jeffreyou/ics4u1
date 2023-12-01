'''6. Create a function that act similarly to “the Power set” and returns a 2D list of all possible subset of a set.
Example: A = {0,1,2}
P({0,1,2}) = {{}, {0},{1},{2},{0,1},{0,2},{1,2},{0,1,2}}
#But we want a list of sets
Note: We can’t have a set within a set in Python 3; Therefore, the result of this function should be a list of sets.
P({0,1,2}) = [{}, {0},{1},{2},{0,1},{0,2},{1,2},{0,1,2}]
P{0,1,2,3,} = [{},{0},{1},{2},{3},{0,1},{0,2},{0,3}]
'''

def power_set(combinations):
    list_combinations = []
    set_combinations = set()
    for digit in range(len(combinations)):
        for item in combinations:
            set_combinations.add(item)
            if len(set_combinations) <= digit + 1:
                set_combinations.add(item)
            if set_combinations not in list_combinations:
                list_combinations.append(set_combinations)
                set_combinations = set()
                    
    return list_combinations
print(power_set([0,1,2]))