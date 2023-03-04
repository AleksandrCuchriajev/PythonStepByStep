# Exercise 1. Create set my_set with numbers from 0 to 100 multiplied by 3. Print the set
my_set = [num * 3 for num in range(0, 101)]
print(my_set)
# Exercise 2. Create set my_set with odd numbers from 0 to 100 squared. Print the set
my_set = [num ** 2 for num in range(0, 101) if num % 2 != 0]
print(my_set)
# Exercise 3. From example_dict create dictionary my_dict with values squared. Print dictionary
example_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict = {key: value ** 2 for key, value in example_dict.items()}
print(my_dict)
# Exercise 4. From example_dict create dictionary my_dict with even values squared. Print dictionary
example_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_dict = {k: v ** 2 for k, v in example_dict.items() if v % 2 == 0}
print(my_dict)
