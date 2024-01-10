#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    leng = len(my_list)
    list_new = []
    for dig in range(leng):
        if my_list[dig] % 2 == 0:
            list_new.append(True)
        else:
            list_new.append(False)
    return list_new
