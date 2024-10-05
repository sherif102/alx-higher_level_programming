#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = y = 0
    if (x == 0):
        print("")
        return i
    try:
        while (y < x):
            if (type(my_list[y]) is not int):
                if (y == x - 1):
                    print("")
                y += 1
                continue
            if (y == x - 1):
                print("{:d}".format(my_list[y]))
            else:
                print("{:d}".format(my_list[y]), end="")
            y += 1
            i += 1
        return i
    except (IndexError, TypeError) as e:
        raise e
