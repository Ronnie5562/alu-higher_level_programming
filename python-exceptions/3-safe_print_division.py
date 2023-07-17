#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
