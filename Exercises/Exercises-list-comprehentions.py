# Exercise 1. Create list my_list with numbers from 0 to 100 multiplied by 2. Print the list
my_list = [num * 2 for num in range(0, 101)]
print(my_list)
# Exercise 2. Create list my_list with even numbers from 0 to 100 squared. Print the list
my_list = [num ** 2 for num in range(0, 101) if num % 2 == 0]
print(my_list)
