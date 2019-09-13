#!/usr/bin/python3
if __name__ == "__main__":
    import sys
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
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    for opr in operators[:]:
        if ord(opr[0]) == ord(operator):
            print("{} {} {} = {}".format(a, operator, b, opr[1](a, b)))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
