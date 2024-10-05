#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    if (x == 0):
        return y
    try:
        while (y < x):
            if (y == x - 1):
                print("{}".format(my_list[y]))
                y += 1
            else:
                print("{}".format(my_list[y]), end="")
                y += 1
        return y
    except IndexError:
        print("")
        return y
