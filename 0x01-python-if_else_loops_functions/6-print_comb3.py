#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j >= i and i != j:
            if i == 8 and j == 9:
                print(89)
            else:
                print("{}".format(str(i) + str(j)), end=", ")
