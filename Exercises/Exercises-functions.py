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

# Exercise 9. Define a function called employee_of_the_month and get the tupple of employee of the month by working hours.
# Use list of tupples work_hours = [('alex', 200), ('billy', 20345), ('sandra', 3444)]
# Example:
# employee_of_the_month(work_hours)
# Output: ('billy', 20345)
work_hours = [('alex', 200), ('billy', 20345), ('sandra', 3444)]
def employee_of_the_month(work_hours):
    employee_name = ''
    current_max = 0
    for name, hours in work_hours:
        if hours > current_max:
            employee_name = name
            current_max = hours
    return (employee_name, current_max)
print(employee_of_the_month(work_hours))

# Exercise 10. Define a function called myfunc that takes in an arbitrary number of arguments, and returns the sum of those arguments.
# Example:
# myfunc(5,6,7,8)
# Output: 26
def myfunc(*args):
  return sum(args)
print(myfunc(5,6,7,8))

# Exercise 11. Define a function called myfunc that takes in an arbitrary number of arguments, 
# and returns a list containing only those arguments that are even.
# myfunc(5, 6, 7, 8,10,20)
# Output: [6, 8, 10, 20]
def myfunc(*args):
        return [args for args in args if args % 2 == 0]
#or
def myfunc(*args):
    even_list=[]
    for item in args:
        if item%2==0:
            even_list.append(item)
    return even_list
print(myfunc(5, 6, 7, 8, 10, 20))

# Exercise 12. Define a function called myfunc that takes in a string, and returns a matching
# string where every even letter is uppercase, and every odd letter is lowercase. Assume that the 
# incoming string only contains letters, and don't worry about numbers, spaces or punctuation. 
# The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.
# Example: 
# myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'
def myfunc(word):
    new_word = ''
    count = 0
    for letter in word:
        count += 1
        if count % 2 != 0:
            new_word += letter.lower()
        else:
            new_word += letter.upper()
    return new_word
print(myfunc('Anthropomorphism'))
# or
def myfunc(a):
    mixed_string = ""
    for item in range(len(a)):
        if item%2==0:
            mixed_string+=a[item].lower();
        else:
            mixed_string += a[item].upper();
    return mixed_string
print(myfunc('Anthropomorphism'))
