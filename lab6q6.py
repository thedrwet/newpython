# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:02:39 2024

@author: thedr
"""
def print_distinct_values(dictionary):
    distinct_values = set(dictionary.values())
    for value in distinct_values:
        print(value)

# Test the function
dictionary = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
print_distinct_values(dictionary)  # Output: 10, 20, 30
