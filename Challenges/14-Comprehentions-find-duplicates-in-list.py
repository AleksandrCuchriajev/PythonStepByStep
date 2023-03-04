# Find the duplicates in my_list using comprehension. Create the duplicates list and print it
my_list = ['a', 'b', 'g', 'd', 'b', 'c', 'd', 'f']
duplicates = list(set([item for item in my_list if my_list.count(item) > 1]))
print(duplicates)
