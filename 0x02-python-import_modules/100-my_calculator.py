#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

a = 10
b = 5
n = len(sys.argv) - 1
if n < 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if op == '+' or op == '-' or op == '*' or op == '/':
    print("{} + {} = {}" .format(a, b, add(a, b)))
    print("{} - {} = {}" .format(a, b, sub(a, b)))
    print("{} * {} = {}" .format(a, b, mul(a, b)))
    print("{} / {} = {}" .format(a, b, div(a, b)))
