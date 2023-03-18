# Exercise 1. Write a function called myfunc that prints the string 'Hello World'.
def myfunc():
  print('Hello World')

# Exercise 2. Define a function called myfunc that takes in a name, and prints 'Hello Name' 
# Do not use f-strings. Example: 
# myfunc('Aleksandr')
# Output: Hello Aleksandr
def myfunc(name):
    print('Hello {}'.format(name))
myfunc('Aleksandr')
