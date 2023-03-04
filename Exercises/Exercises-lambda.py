my_list = [1, 2, 3]

# Exercise 1. Write the map() function with lambda
# def square_2(num):
#     return num * 2
#
#
# print(list(map(square_2, my_list)))

print(list(map(lambda num: num * 2, my_list)))
