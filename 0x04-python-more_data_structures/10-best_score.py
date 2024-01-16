#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    best_dict_key = None
    best_dict_value = float("-inf")

    for key, value in a_dictionary.items():
        if value > best_dict_value:
            best_dict_key = key
            best_dict_value = value

    return (best_dict_key)

