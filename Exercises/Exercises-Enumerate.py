# Exercise 1. Find the index of 50 in my_list. Hint: use enumerate function
my_list = list(range(101))

for i, char in enumerate(my_list):
    if char == 50:
        print(f"the index of {char} is {i}")
