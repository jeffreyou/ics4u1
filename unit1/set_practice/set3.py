# Define a universal set U
universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Define a set A
set_A = {2, 4, 6, 8, 10}

# Calculate the complement of set A with respect to the universal set U
complement_A = universal_set - set_A

# Print the result
print("Universal Set U:", universal_set)
print("Set A:", set_A)
print("Complement of A:", complement_A)

def complement(set_a,universe_set):
    return set(universe_set) - set(set_a)
print(complement(set_A,universal_set))