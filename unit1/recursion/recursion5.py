'''
Q5) Maximum Element in an array

Write a recursive function to find the maximum element in an array that contains comparable data type values.
''' 

max_value = 0
print(max_value)

def max_element(a_list):
    if len(a_list) == 0:
        return max_value
    else:
        if a_list[0] > max_value:
            max_value = a_list[0]
        else:
            max_value = a_list[1]
        return max_element(a_list[1:])
print(max_element([1,2,6,4,7]))