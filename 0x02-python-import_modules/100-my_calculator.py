#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = [
            ["+", add],
            ["-", sub],
            ["*", mul],
            ["/", div]
            ]

    operator = sys.argv[2]

    for opr in operators[:]:
        if opr[0] == operator:
            print("{} {} {} = {}".format(sys.argv[1],
                                         sys.argv[2],
                                         sys.argv[3],
                                         opr[1](int(sys.argv[1]),
                                         int(sys.argv[3]))))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
