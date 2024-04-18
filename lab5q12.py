# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:21:08 2024

@author: thedr
"""


lis=[(10, 20, 40), (40, 50, 60), (70, 80, 90),(),()]
print(lis.count(()))
for i in range(0,lis.count(())):
    lis.remove(())
print(lis)