#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= 97 <= 123):
            b = ord(c) - 32
        else:
            b = ord(c)
        
        print("{}".format(chr(b)), end='')
    print("{}".format(''))
