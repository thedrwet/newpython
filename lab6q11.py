# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:02:53 2024

@author: thedr
"""


def top_three_items(data):
    items = list(data.items())  # convert the dictionary to a list of tuples
    items.sort(key=lambda x: x[1], reverse=True)  # sort the list of tuples based on the second element (price)
    return items[:3]  # return the first three items

# Example usage:
shop_data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print(top_three_items(shop_data))  # Output: [('item4', 55), ('item1', 45.5), ('item3', 41.3)]
