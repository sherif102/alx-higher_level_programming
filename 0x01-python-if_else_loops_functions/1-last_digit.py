#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
snumber = str(number)
last_digit = int(snumber[len(snumber) - 1])
if (number < 0):
    last_digit = last_digit * (-1)

if (last_digit > 5):
    print("Last digit of {0} is {1} and is greater "
          "than 5".format(number, last_digit, 5))
elif (last_digit == 0):
    print("Last digit of {0} is {1} and is 0".format(number, last_digit, 5))
else:
    print("Last digit of {0} is {1} and is less than"
          " 6 and not 0".format(number, last_digit, 5))
