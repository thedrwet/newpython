# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:46:19 2024

@author: thedr
"""
maxi=12121212
hg=[]
kj=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in kj:
    hg.append(list(i))
print(hg)
for j in hg:
    if j[2]<maxi:
        maxi=j[2]