# Exercise 1. # Write a program that switches the values stored
# in the variables a and b. A program should work for different inputs , 
# any value of a and b. Print variables in Console.
'''
For example -> Input
a: 4
b: 8
For Example -> Output
a: 8
b: 4
''' 

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
