#!/usr/bin/python3
for x in range(0, 100):
    print("0" if x < 10 else "",
          "{}".format(x), sep="",
          end=", " if x != 99 else "\n")
