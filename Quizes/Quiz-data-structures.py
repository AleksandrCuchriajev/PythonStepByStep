# Question 1: What data structure?
# You want to assign a city to a postal code, e.g. 99177 = Silute,
# 98175 = Klaipeda, etc. Each postal code occurs only once.
# Later, you want to be able to determine which city belongs to
# a postal code. For example, the user should be able to enter 98175,
# and the program should automatically add "Klaipeda" for the city.
# Which data structure is suitable here? B
#    A) List
#    B) Dictionary
#    C) Set
#    D) Tuple

# Question 2: What data structure?
# You want to write a program in which you can capture cities of Europe.
# Each city may only occur once, so if, for example, "Vilnius" has already
# been entered, "Vilnius" should not be able to be entered again.
# Which data structure is suitable here? C
#    A) List
#    B) Dictionary
#    C) Set
#    D) Tuple

# Question 3: What data structure?
# You have been asked to temporarily store all orders for an online
# shop in a data structure so that you can generate a report that will
# be printed later. The data originally comes sorted from a database.
# This sort order is to be retained. No search by order ID, customer,
# etc. is required. You only need to temporarily store all orders so
# that you can generate the evaluation (print them out one after the other).
# Any additional queries are not required. Which data structure is suitable here? A
#    A) List
#    B) Dictionary
#    C) Set
#    D) Tuple

# Question 4: What data structure?
# You have written a function and want to return several values
# (always the same, for example, first name, last name, age) of a customer.
# What data structure would you return here? A (imutable), D (immutable, faster processing)
#    A) List
#    B) Dictionary
#    C) Set
#    D) Tuple
def user_data():
    return ("Alex", "Best", 50)


a, b, c = user_data()
print(a)
print(b)
print(c)
