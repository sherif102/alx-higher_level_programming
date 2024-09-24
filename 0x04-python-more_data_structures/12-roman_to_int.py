#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        rs = roman_string + 'O'
        rv = {'O': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        rk = list(rv)
        result = 0
        for x in range(0, len(rs) - 1):
            if rs[x] in rk:
                if rv[rs[x]] < rv[rs[x + 1]]:
                    result -= rv[rs[x]]
                else:
                    result += rv[rs[x]]
            else:
                return 0
        return result
