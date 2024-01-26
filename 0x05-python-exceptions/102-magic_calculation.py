#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for dig in range(1, 4):
        try:
            if dig > a:
                raise Exception("Too far")
            result += a ** b / dig
        except Exception:
            result = b + a
            break
        return(result)
