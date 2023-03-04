# Exercise 1. Create set my_set with numbers from 0 to 100 multiplied by 3. Print the set
my_set = [num * 3 for num in range(0, 101)]
print(my_set)
# Exercise 2. Create set my_set with odd numbers from 0 to 100 squared. Print the set
my_set = [num ** 2 for num in range(0, 101) if num % 2 != 0]
print(my_set)