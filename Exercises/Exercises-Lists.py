# Exercise 1. What is the output of this code?
# Guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])

print(new_list[-2])

print(new_list[1:3])

new_list[0] = 'm'
print(new_list)

my_list = [3, 4, 7]
bonus = my_list + [8]
my_list[0] = 'a'
print(my_list)

print(bonus)

# Exercise 2. Using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.pop(0)
# 2. Remove "Blueberries" from the list.
basket.pop()
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
# 5. Count how many apples in the basket
basket.count("Apples")
# 6. empty the basket
basket.clear()
print(basket)

# Exercise 3. Fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Alex', 'Rick', 'John', 'Rendy']

new_friend = ['Sam']

print(friends.sort() + new_friend)

# Solution: (there are multiple ways to do this, so your answer may vary)
# friends.extend(new_friend)
# print(sorted(friends))

# Exercise 4. You have a list:
my_list = [1,2,3,4,5,6,7,8,9,10]
# Count the integers in the list using the loop
count=0
for num in my_list:
  count+=num
print(count)
