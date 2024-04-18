# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:47:35 2024

@author: thedr
"""

import itertools

# Define the dictionary
data = {'1':['a','b'], '2':['c','d']}

# Get the values from the dictionary
values = data.values()

# Generate all combinations
combinations = list(itertools.product(*values))

# Print each combination
for combination in combinations:
    print(''.join(combination))
