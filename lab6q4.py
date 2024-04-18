# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:55:31 2024

@author: thedr
"""

df={m:m*m for m in range(1,6)}
print(df)
print(df.values())
print(df.keys())
dada={}
print(dada.values())
print(dada.keys())
if dada.keys()=='dict_keys([])':
    print('empty')