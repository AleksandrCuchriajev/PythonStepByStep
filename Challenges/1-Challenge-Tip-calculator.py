# Create a program for calculation of pay including the tip between people who split the bill
# The tip percentage should be 10, 12, 15.
# For example:
# If the bill was $120.00, split between 3 people, with 10% tip.
# Each person should pay (120.00 / 3) * 1.10 = 44.0
# Format the result to 2 decimal places = 44.00
# There are 2 ways to round a number. You might have to do some Googling to solve this.
bill = float(input("What was the total bill? \n$"))
persons = int(input("How many people to split the bill? \n"))
percents = float(input("How much tip would you like to give? 10,12,15 : %"))
tip = 1 + percents / 100
pay_each_person = (bill / persons) * tip
final_number = "{:.2f}".format(pay_each_person)
print(f"Each person should pay: ${final_number}")
