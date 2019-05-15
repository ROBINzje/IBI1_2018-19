# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:42:12 2019

@author: ROBIN
"""
#get n from user and change into integer
n=int(input('give me a number: '))
#create a string
st=str(n + " is ")
#change n into number
n=int(n)
#use loop: find the largest power of 2 that is smaller than n
while n>=1:
    i=0
    while 2**i<=n:
        i+=1
    i=i-1
#elongate the string 
    st = st + "2**"+str(i)+"+"
#n reduce 2**i to find the next i
    n=n-2**i
#remove the last "+" 
st=st[:-1]
#print the answer
print(st)

    
