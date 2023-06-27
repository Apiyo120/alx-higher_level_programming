#!/usr/bin/python3

def safe_print_division(a, b):
    """It returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    else:
        print("The division was successful.")
    finally:
        print("Inside result: {}".format(div))
    return (div)
