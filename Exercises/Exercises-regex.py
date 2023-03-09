# Exercise 1. Create password checker. The password should be at least 8 characters long,
# with any sort of letters, numbers and special symbols @#$%
import re

pattern = re.compile(r"([a-zA-Z\d%$@#]{7,}\d)")
password = "aaA1$@%1"
a = pattern.fullmatch(password)
print(a)
