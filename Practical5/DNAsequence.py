# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:51:48 2019

@author: ROBIN
"""
#import necessary packages
import matplotlib.pyplot as plt 
#obtain DNA sequrne from the user and store them in a list
dna=list(input('give a sequence of DNA: '))
#count the nucleotides respectively in DNA sequence 
a=dna.count('A')
c=dna.count('C')
t=dna.count('T')
g=dna.count('G')
#for the first argument of the plot, create a list containing the calculated nucleotide numbers.
number=[a,c,t,g]
#for the 'label' argument of the plot, specify the nucleotide types corresponding with the 'number' list.
labels=['A','C','T','G']
#Practical requirement: print a dictionary of each amount of nucleotides.
dna_dict={'A':a, 'C':c,'T':t, 'G':g}
print(dna_dict)
#create the pie plot
plt.pie(number,labels=labels,autopct='%1.2f%%')
plt.title=('DNA pie chart')
plt.show()


