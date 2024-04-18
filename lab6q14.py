# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:57:49 2024

@author: thedr
"""

def match_key_values(dict1, dict2):
    for (key, value) in dict1.items():
        if key in dict2 and dict2[key] == value:
            print(f'{key}: {value} is present in both dictionaries')

# Example usage:
dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}
match_key_values(dict1, dict2)  # Output: key1: 1 is present in both dictionaries
