#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if (x <= i):
            continue
        if (x != 9 and i != 8):
            print("{}{}".format(i, x), end=", ")
print("89")
