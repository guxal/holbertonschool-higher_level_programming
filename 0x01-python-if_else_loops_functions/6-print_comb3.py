#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if (b > a):
            print("{}{}".format(a, b),
                  end=", " if a != 8 else '\n')
