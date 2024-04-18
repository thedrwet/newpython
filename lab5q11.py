# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 07:39:28 2024

@author: thedr
"""

lis=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
jk=[]
for i in lis:
    jk.append(list(i))
for i in range(0,len(jk)):
    jk[i].pop(2)
    jk[i].append(100)
print(jk)
lis.clear()

for i in jk :
    lis.append(tuple(i))
print(lis)