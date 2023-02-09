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
