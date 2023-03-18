# Exercise 1. Write a function called myfunc that prints the string 'Hello World'.
def myfunc():
  print('Hello World')

# Exercise 2. Define a function called myfunc that takes in a name, and prints 'Hello Name' 
# Do not use f-strings. 
# Example: 
# myfunc('Aleksandr')
# Output: Hello Aleksandr
def myfunc(name):
    print('Hello {}'.format(name))
myfunc('Aleksandr')

# Exercise 3. Define a function called myfunc that takes in a Boolean value (True or False). If True, return 'Hello', and if False, return 'Goodbye'
# Example:
# myfunc(False)
# Output: 'Goodbye'
def myfunc(a):
    if a:
        print('Hello')
    else:
        print('Goodbye')
myfunc(True)
myfunc(False)

# Exercise 4. Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.
# Example: 
# myfunc('Hello','Goodbye',False)
# Output: 'Goodbye'
def myfunc(x, y, z):
    if z == True:
        return x
    return y
print(myfunc('Hello', 'Goodbye', True))
print(myfunc('Hello', 'Goodbye', False))

# Exercise 5. Define a function called myfunc that takes in two arguments and returns their sum.
# Example:
# myfunc(5,12)
# Output: 17
def myfunc(num1,num2):
  return num1+num2
print(myfunc(5,12))

# Exercise 6. Define a function called is_even that takes in one argument, and returns True if the passed-in value is even, False if it is not.
# Example:
# is_even(15)
# Output: False
def is_even(num):
  return num%2==0
print(is_even(15))
