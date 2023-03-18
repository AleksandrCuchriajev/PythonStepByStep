# Exercise 1. Use for, .split(), and if to create a Statement that will print out words from sentence that start with 's':
sentence = 'Print only the words that start with s in this sentence'
my_list = sentence.lower().split()
for item in my_list:
    if item[0] == 's':
        print(item)

# Exercise 2. Use range() to print all the even numbers from 0 to 10.
for _ in range(0,11,2):
  print(_)

# Exercises 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([num for num in range(1, 50) if num % 3 == 0])

# Exercise 4. Go through the sentence below and if the length of a word is even print "even!"
sentence = 'Print every word in this sentence that has an even number of letters'
my_list = sentence.split()
for word in my_list:
    if len(word) % 2 == 0:
        print('even!')
    else:
        print('odd')

# Exercise 5. Write a program that prints the integers from 1 to 100. But for multiples
# of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1, 100):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz', num)
    if num % 3 == 0:
        print('Fizz', num)
    if num % 5 == 0:
        print('Buzz', num)

# Exercise 6. Use List Comprehension to create a list of the first letters of every word in the sentence below:
sentence = 'Create a list of the first letters of every word in this string'
print([word[0] for word in sentence.split()])
