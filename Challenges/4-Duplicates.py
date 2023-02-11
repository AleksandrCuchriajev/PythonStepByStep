# Find duplicates in some list and make an list of them
some_list = ['a', 's', 'e', 'a', 'b', 's']

duplicates = []
for item in some_list:
    if some_list.count(item) > 1 and (item not in duplicates):
        duplicates.append(item)
print(duplicates)
