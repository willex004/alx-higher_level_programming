#!/usr/bin/python3
def no_c(my_string):
    nString = my_string.translate({ord(a): None for a in 'cC'})
    return nString
