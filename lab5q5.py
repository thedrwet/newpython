# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 23:26:33 2024

@author: thedr
"""

maxi=0
word='ds'
j=['adasd','afasfm','afasf','afafaf','afafa','bvbxbcxb']
for i in j:
    if len(i)>maxi:
        word=i
        maxi=len(i)
print(word)
print(maxi)

