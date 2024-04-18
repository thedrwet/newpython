# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:51:43 2024

@author: thedr
"""

from collections import Counter

# Define the list of dictionaries
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Initialize a Counter object
counter = Counter()

# Iterate over each dictionary in the list
for d in data:
    # Add the amount to the counter for the item
    counter[d['item']] += d['amount']

# Print the counter
print(counter)