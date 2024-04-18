# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:16:56 2024

@author: thedr
"""

from collections import Counter
from operator import itemgetter

def sort_counter_by_value(data):
    return sorted(data.items(), key=itemgetter(1), reverse=True)

# Example usage:
data = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(sort_counter_by_value(data))  # Output: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
