# We have a list of continents and my_list
continents = ["Africa", "Antarctica", "Asia", "Australia and Oceania", "Europe", "North America", "South America"]
my_list = ["Asia", "Acoptex", 777, "Sonia", "China", "South Africa", "Antarctica"]

# Exercise 1. Output all continents from the continents list one after the other.
# Desired output:
'''
Africa
Antarctica
Asia
Australia and Oceania
Europe
North America
South America
'''
for continent in continents:
    print(continent)
print("#####################################################")

# Exercise 2. Output only the inhabited continents from the continents list.
# Note: Antarctica is uninhabited. So you can skip this continent at the output.
# Desired output:
'''
Africa
Asia
Australia and Oceania
Europe
North America
South America
'''
for continent in continents:
    if continent == "Antarctica":
        continue
    print(continent)
print("#####################################################")

# Exercise 3. Output only the continents from the my_list.
# You can loop through the my_list and then use the variable continents to check
# if an element of the my_list also appears in the list continents.
# Desired output:
'''
Asia
Antarctica
'''
for item in my_list:
    if item in continents:
        print(item)
print("#####################################################")

# Exercise 4. How many continents are included in the my_list?
# Write a loop to count the number of continents in the my_list and then output this value.
# Desired output:
'''
2 
'''
count = 0
for item in my_list:
    if item in continents:
        count += 1
print(count)
# or
counts = []
for item in my_list:
    if item in continents:
        counts.append(item)
print(len(counts))
print("#####################################################")

# Exercise 5. The seller wants to run a discount campaign in his shop to boost a business.
# You should simplify the calculation of the reduced prices with an if-elif-else structure.
#   items costing between 0 and 20 euro (inclusive) will be reduced by 25%;
#   items costing between 20 (not inclusive) and 50 euro (inclusive) will be reduced by 50%.
#   all other items, i.e. items costing more than 50 euro, will be reduced by 70%.
# Output the new discounted price for the price variable.
# Desired output:
'''
30.0
'''
price = 50
if price <= 20:
    price = price * 0.75
elif price <= 50:
    price = price * 0.5
else:
    price = price * 0.3
print(price)
print("#####################################################")

# Exercise 6. Calculate for each of the old prices from the prices list the appropriate reduced prices
# and save them in the new_prices list. Output this list.
# Desired output:
'''
[7.5, 22.5, 19.2, 16.0]
'''
prices = [10, 45, 64, 32]
new_prices = []
for price in prices:
    if price <= 20:
        price = price * 0.75
    elif price <= 50:
        price = price * 0.5
    else:
        price = price * 0.3
    new_prices.append(price)
print(new_prices)
print("#####################################################")

# Exercise 7. We have a list of chaos, in which new and old prizes are mixed.
# Can you restore an order by using everything you have already learned.
# Scroll through the items in the chaos list. With a new price, simply drag the
# new value from the string and append it to the order list. With an old price,
# you get the old value, calculate the new price and add this value to the order list.
# Finally, output the complete order list, which only contains new prices (and only numbers).
# Tip: With the 'in'`' operator you can check if 'old' or 'new' appears in a list item
# ('old' in 'old price: 100') and decide if you want to make the discount or not.
# Desired output:
'''
[15.0, 40, 16.5, 16.2, 82]
'''
chaos = ["old price: 20", "new price: 40", "old price: 33", "old price: 54", "new price: 82"]
order = []
for item in chaos:
    price = int(item.split(": ")[1])
    if 'old' in item:
        if price <= 20:
            price = price * 0.75
        elif price <= 50:
            price = price * 0.5
        else:
            price = price * 0.3
    order.append(price)
print(order)
