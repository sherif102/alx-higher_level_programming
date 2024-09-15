#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argNumber = sys.argv
argLen = len(argNumber) - 1
if argLen == 0:
    print("0 arguments.")
elif argLen == 1:
    print("1 argument:")
    print("1: {}".format(argNumber[1]))
else:
    print("{} arguments:".format(argLen))
    for i in range(1, argLen + 1):
        print("{}: {}".format(i, argNumber[i]))
