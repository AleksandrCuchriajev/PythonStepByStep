# Exercise 1.
# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys:
# 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
    'age': 12,
    'username': "Alex",
    'weapons': [None],
    'is_active': True,
    'clan': "The sun"
}
# 2 iterate and print all the keys in the above user.
for key in user:
    print(key)
# 3 Add a new weapon to your user
user['weapons'].append("Gun")
print(user)
# 4 Add a new key to include 'is_banned'. Set it to false
user['is_banned']=False
print(user)
# 5 Ban the user by setting the previous key to True
user['is_banned']=True
print(user)
# 6 create a new user2 my copying the previous user and update the age value and username value.
user2=user.copy()
user2['age']=22
user2['username']="Sandra"
print(user2)