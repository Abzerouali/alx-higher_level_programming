#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_mod = -(-number % 10) if number < 0 else (number % 10)
if abs_mod > 5:
    print(f"Last digit of {number} is {abs_mod} and is greater than 5")
elif abs_mod == 0:
    print(f"Last digit of {number} is {abs_mod} and is 0")
else:
    print(f"Last digit of {number} is {abs_mod} and is less than 6 and not 0")
