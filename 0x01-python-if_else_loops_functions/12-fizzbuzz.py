#!/usr/bin/python3

def fizzbuzz():

    """Print a functio that print number from 1 - 100."""

    for number in range(1, 101):
        if number % 3 == 0:
            print("Fizz ", end="")

        elif number % 5 == 0:
            print("Buzz ", end="")

        elif number % 3 and number % 5 == 0:
            print("FizzBuzz ", end="")

        else:
            print("{} " .format(number), end="")
