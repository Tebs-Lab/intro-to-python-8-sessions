'''
Complete this function such that it returns the median value from a list of numbers.

Remember, the median is the value at the center of the sorted dataset. 
If there are an even number of values in the dataset the median is the 
mean of the two center values.
'''
def median(input_list):
    n = len(input_list)
    sorted_list = sorted(input_list)

    # No elements, no median
    if n == 0:
        return None
    # Even case
    elif n % 2 == 0:
        a = sorted_list[n // 2]
        b = sorted_list[n // 2 - 1]
        return (a + b) / 2
    # Odd case
    else:
        return sorted_list[n // 2] # Note: Integer division is needed for odd n


# Very Simple Tests
assert median([]) == None
assert median([1]) == 1
assert median([10,20]) == 15
assert median([1,2,3,4,5]) == 3
assert median([5,1,4,3,2]) == 3

# Add at least 3 more tests!
assert median([11,11]) == 11
assert median([50, 40, 30]) == 40
assert median([9,8,7,6,5,4,3,2,1]) == 5

print("All Tests Passed!")
