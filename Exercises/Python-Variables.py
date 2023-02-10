# Exercise 1. You have two variables a and b, the value for each received from user input. 
# Make a program which swap these variables values so the a will get the value of b
# and b will get the value of a. Print variables in Console.

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
