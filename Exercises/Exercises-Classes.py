# Exercise 1
'''
Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
'''

cat1=Cat('a',2)
cat2=Cat('b',3)
cat3=Cat('c',1)

def get_oldest_cat(*args):
    return max(args)


print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")