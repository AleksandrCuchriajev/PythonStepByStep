# Exercise 1. Write the map() function with lambda
my_list = [1, 2, 3]
print(list(map(lambda num: num ** 2, my_list)))

# Exercise 2. Sort the list by second number in the tuple
my_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
my_list.sort(key=lambda x: x[1])
print(my_list)

