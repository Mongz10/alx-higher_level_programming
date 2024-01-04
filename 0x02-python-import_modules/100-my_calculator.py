#!/usr/bin/python3

if _name_ == "_main_":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 !3:
        print("Usage: ./100_my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops + {"+": add, "_": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unkown opearator. Available operators: +, _, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
