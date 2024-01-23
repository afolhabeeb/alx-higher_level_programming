#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for digit in range(x):
        try:
            print("{:d}".format(my_list[digit]), end="")
            count += 1
        except (IndexError, TypeError, ValueError):
            continue
    print("")
    return(count)
