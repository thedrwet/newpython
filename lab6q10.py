# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 07:59:29 2024

@author: thedr
"""

def count_values_in_key(dictionary, key):
    if key in dictionary:
        return len(dictionary[key])
    else:
        return "Key not found in dictionary"

# Example usage:
my_dict = {"key1": [1, 2, 3, 4], "key2": [1, 2]}
print(count_values_in_key(my_dict, "key1"))  # Output: 4
