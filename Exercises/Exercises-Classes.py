# Exercise 1
'''
Given the below class:   
# 1 Instantiate the Friend object with 3 friends
# 2 Create a function that finds the oldest friend
# 3 Print out: "The oldest friend is x years old.". x will be the oldest friend age by using the function in #2
'''
class Friend:
    species = 'human'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
friend1=Friend('Alex',25)
friend2=Friend('Sonya',30)
friend3=Friend('John',42)

def get_oldest_friend(*args):
    return max(args)

print(f"The oldest friend is {get_oldest_friend(friend1.age, friend2.age, friend3.age)} years old.")
