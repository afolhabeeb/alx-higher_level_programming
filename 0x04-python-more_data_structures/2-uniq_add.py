#!/usr/bin?python3

def uniq_add(my_list=[]):
    unique_ints = set()
    total_sum = 0

    for num in my_list:
        if num not in unique_ints:
            unique_ints.add(num)
            total_sum += num

    return (total_sum)
