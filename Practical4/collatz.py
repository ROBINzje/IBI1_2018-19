# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:19:31 2019

@author: ROBIN
"""
#input a positive integer n
n=int(input("positive number="))
#use loop: conduct the function on n that has not reach -421 tail
while (n-421)%1000!=0:
#the Collatz function
    if n%2 == 0:
        n = n/2
    else: n = 3*n + 1
#print out n
print(n)

