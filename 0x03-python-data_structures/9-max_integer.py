#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return (None)
    else:
        maxi = my_list[0]
        for dig in range(len(my_list)):
            if my_list[dig] > maxi:
                maxi = my_list[dig]
        return (maxi)
