#!/usr/bin/pyton3

def safe_print_list(my_list=[], x=0):
    count = 0
    for dig in range(x):
        try:
            print("{}".format(my_list[dig]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return(count)
