# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:19:31 2019

@author: ROBIN
"""
#input a positive integer n
n=int(input("positive number="))
#create an infinite loop
while 1==1:
#the Collatz function
        if n%2 == 0:
            n = n/2
        else: n = 3*n + 1
#display n sequence
        print(n)
#interrupt when firstly reach 4,2,1
        if n==1:
            break 

