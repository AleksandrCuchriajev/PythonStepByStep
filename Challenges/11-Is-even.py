# Create the function high_even to get the highest even number from the given list of odd and even numbers.
# Print result in Console
# For example: print(high_even([10,2,3,5,6,8,9,44]))
#  Result: 44

def high_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return evens


# print(high_even([10,2,3,5,6,8,9,44]))
print(max(high_even([10, 2, 3, 5, 6, 8, 9, 44])))
