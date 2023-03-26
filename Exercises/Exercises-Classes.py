# Exercise 1
'''
Given the below class: 
'''
class Friend:
    species = 'human'
    def __init__(self, name, age):
        self.name = name
        self.age = age
#1. Instantiate the Friend object with 3 friends
friend1=Friend('Alex',25)
friend2=Friend('Sonya',30)
friend3=Friend('John',42)
#2. Create a function that finds the oldest friend
def get_oldest_friend(*args):
    return max(args)
#3. Print out: "The oldest friend is x years old.". x will be the oldest friend age by using the function in 2
print(f"The oldest friend is {get_oldest_friend(friend1.age, friend2.age, friend3.age)} years old.")

# Exercise 2.
# Given the below class:  

class Friends():
    all_friends = []
    def __init__(self, all_friends):
        self.all_friends = all_friends

    def introduce(self):
        for friend in self.all_friends:
            print(friend.introduce())

class My_Friend():
    is_best_friend = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'Hi, my name is {self.name}'

class Sam(My_Friend):
    def speak(self, greats):
        return f'{greats}'

class Randy(My_Friend):
    def speak(self, greats):
        return f'{greats}'

#1. Add another class which inherits from class My_Friend
class Rembo(My_Friend):
    def speak(self, greats):
        return f'{greats}'
    
#2. Create a list of all of the friends my_friends = [] (create 3 friend instances from the above) 
my_friends = [Sam('Sam', 23), Randy('Randy', 21), Rembo('Rembo', 22)]

#3. Instantiate the Friend class with all your friends use variable friends
friends=Friends(my_friends)

#4. Output all of the friends walking using the friends instance
friends.introduce()
