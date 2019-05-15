# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:18:56 2019

@author: ROBIN， inpired by Melanie I Stefan
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:16:22 2019

@author: ROBIN
"""
#import necessary pkgs to create arrays and plot the results
import numpy as np
import matplotlib.pyplot as plt
#initiate population (zero for susceptible)
population=np.zeros((100,100))
#randomly choose one point as the first infected person 
outbreak = np.random.choice (range(100),2) 
#(1 for infected)
population[outbreak[0],outbreak[1]]=1
#specify the possibilities: beta for an susceptible person to be infected, gamma for an infected person to recover and possess resistance
beta=.3
gamma=.05
# an infected person can contact v people at one time. v is specified as 5.
v=5
#initialize time for the loop
t=0
#go through the loop for 100 times
while t<=50:
    #counter
    t+=1
    '''reference Melanie's work in describing infection process 
    orginal codes in the same folder (Practical12)
    '''
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        #search adjacent neighbours
        xrange=range(x-1,x+2)
        yrange=range(y-1,y+2)
        #a list to store the position of neighbours
        neighbours=[]
        for xr in xrange:
            for yr in yrange:
                neighbours.append((xr,yr))
        #avoid infecting itself
        neighbours.remove((x,y))
        #a list of indexes of v neighbours that contact the infected person 
        chs=np.random.choice(range(v),v)
        #choose new people to be infected among the contacted neighbors, with possibility beta
        for c in chs:
            xNeighbour=neighbours[c][0]
            yNeighbour=neighbours[c][1]
            # make sure I don't fall off an edge
            if xNeighbour!= -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                # only infect neighbours that are susceptable
                if population[xNeighbour,yNeighbour]==0:
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        #each infected individuals (except the newly infected) can recover at the possibility of gamma
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
    #for each time point create a heat plot
    plt.figure(figsize=(6,4),dpi=150) 
    plt.imshow(population,cmap='viridis',interpolation='nearest')
    #a way for creating a small video:
    #type 'matplotlib qt' before running the code to show it in a sepqrate window
    #for each time point, use plt.cla() to delete the former picture
'''reference: (Stefan, 2019) infection_snippet.py
'''   
 
 
 
 