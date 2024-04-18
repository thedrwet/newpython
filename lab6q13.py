# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:19:20 2024

@author: thedr
"""

from collections import defaultdict

def create_dict(keys, values):
    d = defaultdict(set)  # Create a defaultdict with sets as default values
    for k, v in zip(keys, values):
        d[k].add(v)  # Add each value to the set for the corresponding key
    return d

# Example usage:
keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]
print(create_dict(keys, values))  # Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
