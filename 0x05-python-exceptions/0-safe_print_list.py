#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	y = 0
	try:
		while (y < x):
			if (y != x - 1):
				print("{}".format(my_list[y]), end="")
				y = y + 1
			else:
				print("{}".format(my_list[y]))
				break
		return y + 1
	except:
		print("")
		return y