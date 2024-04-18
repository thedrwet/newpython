# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:54:26 2024

@author: thedr
"""

# Create the dictionary
dict_values = {
    'x': list(range(11, 20)),
    'y': list(range(21, 30)),
    'z': list(range(31, 40))
}

# Access the fifth value of each key
fifth_values = {key: values[4] for key, values in dict_values.items()}

# Print the dictionary and the fifth values
print("The dictionary is:")
for key, values in dict_values.items():
    print(f"{key} has value {values}")

print("\nThe fifth value of each key is:")
for key, value in fifth_values.items():
    print(f"{key} {value}")
