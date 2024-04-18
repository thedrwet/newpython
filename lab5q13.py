# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:28:38 2024

@author: thedr
"""
def swap(a,b):
    temp=a
    a=b
    b=temp

lis=[('item1', '12'), ('item2', '15'), ('item3', '24')]
jk=[]
for i in lis:
    jk.append(list(i))
for i in range(0,len(jk)):
    jk[i][1]=float(jk[i][1])
print(jk)
