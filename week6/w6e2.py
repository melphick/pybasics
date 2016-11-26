#!/usr/bin/python

"""
Converts a list to a dictionary where the index of the list is used as the
key to the new dictionary (the function will return the new dictionary).
"""

def list_to_dict(a_list):
    a_dict = {}
    for i in a_list:
        print i
        a_dict[i] = a_list[i]
    return a_dict


a = range(10)

print list_to_dict(a)
