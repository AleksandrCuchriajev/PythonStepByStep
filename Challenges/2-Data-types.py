# Write a program that adds the digits in a 2-digit number.
# Your program should work for different inputs,
# any two-digit number.
"""
For Example -> Input
24
Example Output
2 + 4 = 6
6
"""
two_digit_number = input("Type your two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)
