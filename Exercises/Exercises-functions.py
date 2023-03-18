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

# Exercise 7. Define a function called is_greater that takes in two arguments, and returns True if the first value
# is greater than the second, False if it is less than or equal to the second.
# Example;
# is_greater(5,9)
# Output: False
def is_greater(num1,num2):
  return num1>num2
print(is_greater(5,9))

# Exercise 8.  Define a function called is_even and return the list of even numbers from any list given, for example:
# is_even([1,2,5,4,6,7,8,9,23,44])
# Output [2, 4, 6, 8, 44]
def is_even(my_list):
    return [num for num in my_list if num % 2 == 0]
print(is_even([1, 2, 8, 5, 4, 6, 7, 10, 9, 23, 44,100]))
