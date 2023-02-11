# Exercise 1. You have two variables is_Student and is_Expert. Check different conditions
is_Student = False
is_Expert = True
# Check if Student AND Expert and print: You are student expert
# Check if Student AND but NOT Expert and print: At least you are getting there
# If you are not Student print: You need to study. More knowledge ahead of you
if is_Student and is_Expert:
  print('You are student expert')
elif is_Student and not is_Expert:
  print('At least you are getting there')
elif not is_Student:
  print('You need to study. More knowledge ahead of you')
  
# Exercise 2. # Write a program that works out whether if a given
# number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 4 is even because 4 ÷ 2 = 2
# 2 does not have any decimal places. Therefore, the division is clean.
# e.g. 3 is odd because 3 ÷ 2 = 1.5
# 3 is not a whole number, it has decimal places.
# Therefore, there is a remainder of 0.5, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you
# the remainder after a division.
"""
e.g. 6 ÷ 2 = 3 with no remainder.
therefore: 6 % 2 = 0
5 ÷ 2 = 2 x 2 + 1, remainder is 1.
therefore: 5 % 2 = 1
14 ÷ 4 = 3 x 4 + 2, remainder is 2.
therefore: 14 % 4 = 2
"""
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
