#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_del = []
    for key, val in a_dictionary.items():
        if val == value:
            dict_del.append(key)

    for key in dict_del:
        del a_dictionary[key]

    return (a_dictionary)
