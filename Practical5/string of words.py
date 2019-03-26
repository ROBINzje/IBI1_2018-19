# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:39:48 2019

@author: ROBIN
"""
#obtain string from user
word=input('give me a string of words: ')
#create a list of individual words.
word1=word.split(' ')
#create a list to store q
li=[]
#the aim of the loop is to reverse letters of each word.
#firstly create a list of individual letters, secondly reverse, finally join the letter together.
for i in word1:
    j=list(i)
    j.reverse()
    q=''.join(j)
#after generating q, store it in li.
    li.append(q)
#put li in right order, then reverse.
li.sort()
li.reverse()
#show li in console
print(li)