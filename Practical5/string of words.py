# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:39:48 2019

@author: ROBIN
"""

word=input('give me a string of words: ')
word1=word.split(' ')
li=[]
for i in word1:
    j=list(i)
    j.reverse()
    q=''.join(j)
    li.append(q)
li.sort()
li.reverse()
print(li)