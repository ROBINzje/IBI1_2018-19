# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:51:48 2019

@author: ROBIN
"""

import matplotlib.pyplot as plt 
s=list(input('give a sequence of DNA: '))
a=s.count('A')
c=s.count('C')
t=s.count('T')
g=s.count('G')
frac1=[a,c,t,g]
labels=['A','C','T','G']
plt.pie(frac1,labels=labels,autopct='%1.2f%%')
plt.title=('DNA pie chart')
plt.show()