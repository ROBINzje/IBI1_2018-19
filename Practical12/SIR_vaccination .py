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
#the whole polulation
N=10000
#create a list for the proportion of vaccinated people
vac_prop=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
#a list to store the lists of infected numbers at each time point for each vaccinated proportion
I_vac=[]


#go through each vaccinated proportion
for i in vac_prop:
    #an empty list to record number I at eah time point
    Ilist=[]
    t=0
    #the condition that at least oen person get infected at t=0 
    if i <1:
        #at t=0 the resistive people (i*N vaccinated and 0 recovered)
        #convert float to int
        R=int(i*N)
        #at least 1 infected (prevent dividing 0 for p1)
        I=1
        #susceptible size
        S=N-R-I     
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
            #record the number of people infected at current time point
            Ilist.append(I)
        #record the whole process as a list into list I_vac for the current vaccination proportion
        I_vac.append(Ilist)
    #the condition that all are vaccinated
    #create a list filled with 0s that no one gets infected at each time point
    else:
        for t in range(1000):
            Ilist.append(0)
        #add the 0 list to the I_vac
        I_vac.append(Ilist)
        

#visualization
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#for each vaccination proportion create a curve to represent the number of infected people
for i in range(len(vac_prop)):
    y=I_vac[i]
    #show percent when the proportion is over 0
    if i !=0:
        plt.plot(range(t+1),y,label='{:3.2f}%'.format(vac_prop[i]*100))
    else:
        plt.plot(range(t+1),y,label='0')
#for multiple curves use legend to make it clear
plt.legend()
#x,y labels
plt.xlabel('time')
plt.ylabel('number of people')
#title
plt.title('SIR with different vaccination rates')
#save the figure
plt.savefig(r'C:\Users\ROBIN\Desktop\GK project\IBI1_2018-19\Practical12\SIR_vaccination' ,type='png')




    