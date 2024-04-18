# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:12:47 2024

@author: thedr
"""

def combine_dictionaries(dict1, dict2):
    result = dict1.copy()  # start with dict1's keys and values
    for key, value in dict2.items():
        if key in result:
            # if key is in dict1, add dict2's value to it
            result[key] += value
        else:
            # if key is not in dict1, add it to result
            result[key] = value
    return result

# Test the function
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
print(combine_dictionaries(dict1, dict2)) 