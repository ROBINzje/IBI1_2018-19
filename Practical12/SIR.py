# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:16:22 2019

@author: ROBIN
"""
#import necessary pkgs to create arrays and plot the results
import numpy as np
import matplotlib.pyplot as plt


#specify the possibilities: beta for an susceptible person to be infected, gamma for an infected person to recover and possess resistance
beta=.3
gamma=.05
#the number of the whole population
N=10000
#specify each groups (S for the susceptible, I for the infected and R for the recovered)
S=10000
I=1
R=0
#initialize time for the loop
t=0
#for each stage/group of people, create a list to store the results for each time point
Ilist=[]
Rlist=[]
Slist=[]


#go through the loop for 1000 times
while t<1000:
    #counter
    t+=1   
    #guarantee each person can only change 0 or 1 time during one loop (i.e. allow S->I & I->R, prevent S->I->R in one loop)
    currI=I
    #modify beta based on the infected ratio
    p1=beta*currI/N
    #with infection possibility p1, generate 0 or 1 for each S. 0 for infected and 1 for staying susceptible
    toI=np.random.choice(range(2),S,p=[p1,1-p1])
    #the newly infected people change from S to I. Modify the numbers of both groups
    for i in toI:
        if i==0:
            I+=1
            S-=1
    #with recovery possibility gamma, generate 0 or 1 for each I. 0 for recovery and 1 for staying infected
    toR=np.random.choice(range(2),currI,p=[gamma,1-gamma])
    #the newly recovered people change from I to R. Modify the numbers of both groups
    for j in toR:
        if j==0:
            R+=1
            I-=1
    #record the number of people in each group
    Ilist.append(I)
    Rlist.append(R)
    Slist.append(S)
    
    
#visualization
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#draw 3 curves for S, I, R respectively with labels. 
plt.plot(range(t), Ilist, label='infected')
plt.plot(range(t),Rlist, label='recovered')
plt.plot(range(t),Slist, label='susceptible')
#for multiple curves use legend to be more clear
plt.legend()
#the x,y labels
plt.xlabel('time')
plt.ylabel('number of people')
#title
plt.title('SIR model')
#show the figure
#plt.show() results in an empty file after saving it
#save the figure
plt.savefig(r'C:\Users\ROBIN\Desktop\GK project\IBI1_2018-19\Practical12\SIR' ,type='png')

    