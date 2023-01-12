#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lOrd = list(a_dictionary.keys())
    lOrd.sort()
    for a in lOrd:
        print("{}: {}".format(a, a_dictionary.get(a)))
