#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for digit in range(x):
            count += 1
            print("{:d}".format(my_list[digit]), end="")
    except (ValueError, TypeError):
        pass

    print('')
    return(count)
