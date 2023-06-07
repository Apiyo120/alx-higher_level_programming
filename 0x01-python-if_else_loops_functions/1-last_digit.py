#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

value = abs(number) % 10

if number > 5:
    print("Last digit of", number, "is", value, "and is greater than 5")

if number == 0:
    print("Last digit of", number, "is", value, "and is 0")
if number < 6 != 0:
    print("Last digit of", number, "is", value, "and is less than 6 and not 0")
