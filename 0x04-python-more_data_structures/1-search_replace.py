#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nList = list(map(lambda b: replace if b ==  search else b, my_list))
    return (nList)
