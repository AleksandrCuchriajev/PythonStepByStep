# Exercise 1. Handle the exception thrown by the code below by using try and except blocks (TypeError).
# for i in ['a','b','c']:
#    print(i**2)
try:
  for i in ['a','b','c']:
    print(i**2)
except TypeError:
  print("An error occurred!")

# Exercise 2. Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
# x = 5
# y = 0
# z = x/y
try:
  x = 5
  y = 0
  z = x/y
except ZeroDivisionError:
  print("You can't divide by zero")
finally:
  print('All Done')
  
# Exercise 3. Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
# def ask():
#    pass
# ask()
# Output: Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, your number squared is:  4
def ask():    
    while True:
        try:
            user_input = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break   
    print('Thank you, your number squared is: ',n**2)
ask()

# Exercise 4. Write an exception that catches the error when someone tries to open the following file that does not exist in this directory.
# Output the message "File not found". Open the file with a suitable construct if it does exist in the future - without errors because the file was not closed correctly.
# file = open("text.txt", mode="r")
#   print(file)
try:
  with open("text.txt", mode="r") as file:
    print(file)
except FileNotFoundError:
  print('File not found')
  
# Exercise 5. See what type of error occurs when executing the following code. Catch the error with **try except** and output an appropriate error message.
# names = ["Alex", "Sam", "Red"]
# scores = {"Alex": 50, "Sam": 100}

# def print_scores():
#     for name in names:
#         print(scores[name])

# print_scores()
  
# Output:
# 50
# 100
# key is missing

names = ["Alex", "Sam", "Red"]
scores = {"Alex": 50, "Sam": 100}

def print_scores():
   for name in names:
       print(scores[name])
try:
  print_scores()
except KeyError:
  print('key is missing')

# Exercise 6. Create an error class that is called if 'names' is an empty dictionary. Then an `EmptyDictionaryError` should occur with the hint that the dictionary 'names' contains no element.
# names = {}
# if len(d) == 0:
#    print("Your error here")
class EmptyDictionaryError(Exception):
   pass
names = {}
if len(names) == 0:
   raise EmptyDictionaryError("names contains no element")

