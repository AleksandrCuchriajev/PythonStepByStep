# Create a program using maths and f-Strings that tells us
# how many days, weeks, months we have left if we live until 75 years old.
# It will take your current age as the input and output a message
# with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly,
# even the positions of the commas and full stops.
"""
Example Input
45
Example Output
You have 10950 days, 1560 weeks, and 360 months left.
"""
age = input("What is your current age?")
years_left = 75 - int(age)
x = years_left * 365
y=years_left*52
z=years_left*12
print(f"You have {x} days, {y} weeks, and {z} months left.")