#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    lKeys = list(a_dictionary.keys())
    for i in lKeys:
        num += 1
    return (num)
