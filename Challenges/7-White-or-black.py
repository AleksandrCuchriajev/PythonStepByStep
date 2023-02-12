# You are going to write a virtual coin toss program. It will randomly tell the user "White" or "Black".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. White, not white.
# There are many ways of doing this. You should generate a random number, either 0 or 1. Then use that number
# to print out White or Black, 1 means White 0 means Black
"""
Example Output
White
or
Black
"""
import random
random_side = random.randint(0, 1)
if random_side == 1:
    print("White")
else:
    print("Black")