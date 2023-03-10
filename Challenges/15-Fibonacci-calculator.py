# Exercise 1. Make generator which calculates fibonacci numbers:
# generator version
def fibonacci(n):
    num1 = 0
    num2 = 1
    for _ in range(n):
        yield num1
        temp = num1 
        num1 = num2
        num2 = temp + num2

for _ in fibonacci(21):
  print(_)


# list version
def fibonacci2(n):
    num1 = 0
    num2 = 1
    total = []
    for _ in range(n):
        total.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2
    return total

print(fibonacci2(21))