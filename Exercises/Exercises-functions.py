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

# Exercise 3. Define a function called myfunc that takes in a Boolean value (True or False). If True, return 'Hello', and if False, return 'Goodbye'
# For example, a function that returns 'Inside' if a is True and 'Outside' if a is False could look like:
# Example:
# myfunc(False)
# Output: 'Outside'
def myfunc(a):
    if a:
        print('Hello')
    else:
        print('Goodbye')
myfunc(True)
myfunc(False)

# Exercise 4. Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.
# myfunc('Hello','Goodbye',False)
# Output: 'Goodbye'
def myfunc(x, y, z):
    if z == True:
        return x
    return y
print(myfunc('Hello', 'Goodbye', True))
print(myfunc('Hello', 'Goodbye', False))
