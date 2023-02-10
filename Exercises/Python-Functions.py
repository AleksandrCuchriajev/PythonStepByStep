# Exercises Functions
"""
Exercise 1
Create a function that returns the smaller of two given numbers
if both numbers are even, but returns the greater if one or
both numbers are odd.
For example:
smaller_of_two_evens(2,4) --> 2
smaller_of_two_evens(2,5) --> 5
"""


# def smaller_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a > b:
#             return b
#         else:
#             return a
#     else:
#         if a > b:
#             return a
#         else:
#             return b


def smaller_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(smaller_of_two_evens(2, 4))
print(smaller_of_two_evens(2, 5))

"""
Exercise 2
Create a function takes a two-word string and returns 
True if both words begin with same letter
For example:
check_words('Best Coat') --> False
check_words('Crackers Cat') --> True
"""


def check_words(text):
    my_list = text.lower().split(" ")
    return my_list[0][0] == my_list[1][0]


print(check_words('crackers Cat'))
print(check_words('Best Coat'))

'''
Exercise 3
Create the function of two integers and return True if the sum of
 the integers is 20 or if one of the integers is 20. Otherwise return False
For example:
makes_twenty(20,3) --> True
makes_twenty(5,15) --> True
makes_twenty(5,20) --> True
makes_twenty(1,5) --> False
'''


def makes_twenty(num1, num2):
    # if num1 + num2 == 20 or num1 == 20 or num2 == 20:
    #     return True
    # else:
    #     return False
    return (num1 + num2) == 20 or num1 == 20 or num2 == 20


print(makes_twenty(20, 3))
print(makes_twenty(5, 15))
print(makes_twenty(5, 20))
print(makes_twenty(1, 5))

'''
Exercise 4
Create a function that capitalizes the first and fourth letters of a string
For example:
capitalize_string('acoptex') --> AcoPtex
Please note: 'acoptex'.capitalize() returns 'Acoptex'
'''


# def capitalize_string(text_string):
#     new_string = ""
#     for letter in text_string:
#         if text_string.index(letter) == 0 or text_string.index(letter) == 3:
#             new_string += letter.upper()
#             #new_string += letter.capitalize()
# else:
#     new_string += letter
# print(new_string)


# def capitalize_string(text_string):
#     first_letter = text_string[0].upper()
#     between_letters = text_string[1:3]
#     fourth_letter = text_string[3].upper()
#     rest_letters = text_string[4:]
#
#     return print(first_letter + between_letters + fourth_letter + rest_letters)

def capitalize_string(text_string):
    first_half = text_string[0:3].capitalize()
    second_half = text_string[3:].capitalize()

    return print(first_half + second_half)


capitalize_string("acoptex")

'''
Exercise 5
For the given sentence, return the same sentence with the words reversed
For example:
reverse_order('I am home') --> 'home am I'
reverse_order('I am ready') --> 'ready am I'

Please note: 
The .join() method may be useful here. The .join() method allows you
to join together strings in a list with some connector string. 
For example, some uses of the .join() method:
"-".join(['1','2','3']) --> '1--2--3'

So, if you had a list of words you wanted to turn back
into a sentence, you could just join them with a single space string:
" ".join(['I','am','home]) -> "I am home"
'''


def reverse_order1(sentence):
    my_list = sentence.split()
    reverse_list = my_list[::-1]
    return print(" ".join(reverse_list))


def reverse_order2(sentence):
    my_list = sentence.split()
    my_list.reverse()
    return print(" ".join(my_list))


reverse_order1('I am home')
reverse_order2('I am ready')

'''
Exercise 6
Create the function with an integer num as parameter and return True 
if num is within 10 of either 100 or 200
For example:
almost_there(91) --> True
almost_there(105) --> True
almost_there(140) --> False
almost_there(208) --> True
Please note: abs(num) returns the absolute value of a number
'''


def almost_there(num):
    # return 190 <= num <= 210 or 90 <= num <= 110
    return abs(100 - num) <= 10 or abs(200 - num) <= 10


# print(almost_there(91))
# print(almost_there(105))
# print(almost_there(140))
# print(almost_there(208))

'''
Exercise 7
Create the function with a list of ints, 
return True if the array contains a 1 next to a 2.
For example:
find_12([1, 2, 3]) → True
find_12([1, 5, 2, 4]) → False
find_12([3, 2, 4]) → False
'''


# def find_12(list_to_check):
#     my_string = ""
#     for item in list_to_check:
#         my_string += str(item)
#     return '12' in my_string


# def find_12(list_to_check):
#     for i in range(0, len(list_to_check) - 1):
#         if list_to_check[i] == 1 and list_to_check[i + 1] == 2:
#             return True
#     return False

def find_12(list_to_check):
    for i in range(0, len(list_to_check) - 1):
        if list_to_check[i:i + 2] == [1, 2]:
            return True
    return False


print(find_12([1, 2, 3]))
print(find_12([1, 3, 3, 2]))
print(find_12([3, 2, 4]))

'''
Exercise 8
Create the function with a string as parameter, 
return a string where for every character in the original
there are three characters
For example:
increase_string('World') --> 'WWWooorrrlllddd'
increase_string('Acoptex') --> 'AAAcccooopppttteeexxx'
'''


def increase_string(my_string):
    my_new_string = ""
    for char in my_string:
        my_new_string += char * 3
    return print(my_new_string)


increase_string('World')
increase_string('Acoptex')

'''
Exercise 9 Black Jack
Create the function with three integers as parameters between 1 and 11, 
if their sum is less than or equal to 21, return their sum. If their
sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''


def blackjack(num1, num2, num3):
    if sum([num1, num2, num3]) <= 21:
        return sum([num1, num2, num3])
    elif 11 in [num1, num2, num3] and sum([num1, num2, num3]) - 10 <= 21:
        return sum([num1, num2, num3]) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

'''
Exercise 10
Return the sum of the numbers in the array,
except ignore sections of numbers starting with a 6
and extending to the next 9 (every 6 will be followed by 
at least one 9). Return 0 for no numbers.

skip_12([1, 3, 5]) --> 9
skip_12([4, 5, 6, 7, 8, 9]) --> 9
skip_12([2, 1, 6, 9, 11]) --> 14
'''


def skip_12(array):
    total = 0
    add = True
    for number in array:
        while add:
            if number != 6:
                total += number
                break
            else:
                add = False
        while not add:
            if number != 9:
                break
            else:
                add = True
                break
    return print(total)


skip_12([1, 3, 5])
skip_12([4, 5, 6, 7, 8, 9])
skip_12([2, 1, 6, 9, 11])

'''
Exercise 11
Create a function that takes in a list of integers and returns 
True if it contains 007
For example:
 if_existing_007([1,2,4,0,0,7,5]) --> True
 if_existing_007([1,0,2,4,0,5,7]) --> True
 if_existing_007([1,7,2,0,4,5,0]) --> False
'''


def if_existing_007(my_list):
    new_string = ""
    for number in my_list:
        new_string += str(number)
    if '007' in new_string:
        return True
    else:
        return False


print(if_existing_007([1, 2, 4, 0, 0, 7, 5]))
print(if_existing_007([1, 0, 2, 4, 0, 5, 7]))
print(if_existing_007([1, 7, 2, 0, 4, 5, 0]))

'''
Exercise 12
Create a function my_func which will have as a parameter list 'my_list' of integers
which will print the highest even number
'''


# def my_func(my_list):
# highest_number = 0
# for item in my_list:
#     if item % 2 == 0 and item > highest_number:
#        highest_number = item
# return highest_number

def my_func(my_list):
    evens = []
    for item in my_list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(my_func([1, 2, 3, 4, 5, 6]))
'''
Exercise 13
Create the function that returns the number of prime numbers that exist up to and including a given number
For example:
count_primes(100) --> 25
By convention, 0 and 1 are not prime.
'''


def count_primes(num):
    if num < 2:
        return 0
    # 2 or greater
    # List to store prime numbers
    primes = [2]
    # counter going up to the input num
    x = 3
    # x is going through every number up to input number
    while x <= num:
        # check if x is prime
        # for y in range(3, x, 2):
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return print(len(primes))


count_primes(100)
'''
Exercise 14
Create a function that takes in a single letter, and returns a 5x5 representation of that letter

print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *

HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "b".
'''
# def print_big(letter):
#     patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
#     alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])

my_dict = {'A':
        """
   *
 *   *
 *****
 *   *
 *   *
 """, 'B':
        """
 ** *
 *   *
 *****
 *   *
 ** *
 """}


def print_big(letter):
    return my_dict[letter.upper()]


print(print_big('a'))
