# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 00:05:16 2024

@author: thedr
"""

s = 'w3resource'

# Initialize an empty dictionary
letter_counts = {}

# Iterate over each character in the string
for char in s:
    # If the character is already in the dictionary, increment its count
    if char in letter_counts:
        letter_counts[char] += 1
    # Otherwise, add the character to the dictionary with a count of 1
    else:
        letter_counts[char] = 1

# Print the dictionary
print(letter_counts)