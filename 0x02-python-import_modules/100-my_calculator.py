#!/usr/bin/python3

if __name__ == "__main__":
    """Build my own calculator!"""
    import sys
    from calculator_1 import mul, sub, add, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    av = sys.argv[2]

    dic = {"+": add, "-": sub, "*": mul, "/": div}

    if av not in dic:
        print("Unknown dic. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, av, b, dic[av](a, b)))
