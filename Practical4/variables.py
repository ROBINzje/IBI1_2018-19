# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:28:40 2019

@author: ROBIN
"""

a=123
b=123123
print(b%7)
c=b/7
d=c/11
e=d/13
print(a==e)

X=True
Y=False
Z=(X and not Y)or(Y and not X)
print(Z)
W=(X!=Y)
print(W)

X=False
Y=False
Z=(X and not Y)or(Y and not X)
print(Z)
W=(X!=Y)
print(W)

X=True
Y=True
Z=(X and not Y)or(Y and not X)
print(Z)
W=(X!=Y)
print(W)

X=False
Y=False
Z=(X and not Y)or(Y and not X)
print(Z)
W=(X!=Y)
print(W)
