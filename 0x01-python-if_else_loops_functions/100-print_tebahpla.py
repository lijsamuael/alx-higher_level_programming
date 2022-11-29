#!/usr/bin/python3
for x in range(ord("z"), ord("a") - 1, -1):
    print("{}".format(chr(x - (32 if x % 2 == 1 else 0))), end="")
