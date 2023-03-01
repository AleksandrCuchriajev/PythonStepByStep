# Exceptions

# Exercise 1

# Write an exception that catches the error when someone tries to open the following file that does not exist in this directory.
# Output the message "File not found". Open the file with a suitable construct if it does exist in the future - without errors because the file was not closed correctly.
# file = open("text.txt", mode="r")
#   print(file)
try:
  with open("text.txt", mode="r") as file:
    print(file)
except FileNotFoundError:
  print('File not found')
  
# Exercise 2

# See what type of error occurs when executing the following code. Catch the error with **try except** and output an appropriate error message.
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

# Exercise 3 

# Create an error class that is called if 'names' is an empty dictionary. Then an `EmptyDictionaryError` should occur with the hint that the dictionary 'names' contains no element.
# names = {}
# if len(d) == 0:
#    print("Your error here")
class EmptyDictionaryError(Exception):
   pass
names = {}
if len(names) == 0:
   raise EmptyDictionaryError("names contains no element")

