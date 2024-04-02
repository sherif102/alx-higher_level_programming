<<<<<<< HEAD
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    if argLen == 1:
        print("{} arguments.".format(argLen - 1))
    elif argLen == 2:
        print("{} argument:".format(argLen - 1))
    else:
        print("{} arguments:".format(argLen - 1))
    for i in range(1, argLen):
        print("{}: {}".format(i, sys.argv[i]))
=======
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    if argLen == 1:
        print("{} arguments.".format(argLen - 1))
    elif argLen == 2:
        print("{} argument:".format(argLen - 1))
    else:
        print("{} arguments:".format(argLen - 1))
    for i in range(1, argLen):
        print("{}: {}".format(i, sys.argv[i]))
>>>>>>> d2a0194760306840a30b5a375f4a9ea8ea1303fe
