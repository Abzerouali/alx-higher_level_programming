#!/usr/bin/python3
def print_last_digit(number):
    abs_mod = (-number % 10) if number < 0 else (number % 10)
    print(abs_mod, end="")
    return (abs_mod)
