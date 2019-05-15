# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:22:13 2019

@author: ROBIN, inspired by Melanie I Stefan
"""
#Melanie's code: convert xml file to cps and generate modelResult.csv
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
    
        
        
#------------------------------------------------------------------------------
xml_to_cps() 
#os.system("")
import numpy as np
import re
import matplotlib.pyplot as plt
results=[]
#import os
with open('modelResults.csv') as file:
    file=file.readlines()
    for i in range(len(file)):
        line=file[i]
        line=re.split(r',|\n',line)
        line.remove('')
        results.append(line)
    results=np.array(results)
    results=results[1:].astype(np.float)


#########time course visualization#########
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#data for each curves
plt.plot(results[:,0],results[:,1], label='Predator(b=0.02,d=0.4)')
plt.plot(results[:,0],results[:,2], label='Prey(b=0.1,d=0.02)')
#for multiple curves use legend to be more clear
plt.legend()
#the x,y labels
plt.xlabel('time')
plt.ylabel('population size')
#title
plt.title('Time course')
plt.show()

#########limit cycle visualization#########
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#data for each curves
plt.plot(results[:,1],results[:,2])
#the x,y labels
plt.xlabel('predator population')
plt.ylabel('prey population')
#title
plt.title('Limit cycle')
plt.show()

#########change parameters#########
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("predator-prey_copy.xml")
collection=DOMTree.documentElement
para=collection.getElementsByTagName('parameter')
for i in para:
    if i.getAttribute('id')=='k_predator_breeds':
        i.setAttribute('value','0.3')
        print(i.attributes['value'].value)
    if i.getAttribute('id')=='k_predator_dies':
        i.setAttribute('value','0.1')
        print(i.attributes['value'].value)
    if i.getAttribute('id')=='k_prey_breeds':
        i.setAttribute('value','0.9')
        print(i.attributes['value'].value)
    if i.getAttribute('id')=='k_prey_dies':
        i.setAttribute('value','0.3')
        print(i.attributes['value'].value)
copy = open('predator-prey_copy.xml','w')
DOMTree.writexml(copy)
copy.close()
xml_to_cps('predator-prey_copy.xml','predator-prey_copy.cps')

with open('modelResults.csv') as file:
    file=file.readlines()
    for i in range(len(file)):
        line=file[i]
        line=re.split(r',|\n',line)
        line.remove('')
        results.append(line)
    results=np.array(results)
    results=results[1:].astype(np.float)


#time course visualization
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#data for each curves
plt.plot(results[:,0],results[:,1], label='Predator(b=0.02,d=0.4)')
plt.plot(results[:,0],results[:,2], label='Prey(b=0.1,d=0.02)')
#for multiple curves use legend to be more clear
plt.legend()
#the x,y labels
plt.xlabel('time')
plt.ylabel('population size')
#title
plt.title('Time course')
plt.show()

#limit cycle visualization
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#data for each curves
plt.plot(results[:,1],results[:,2])
#the x,y labels
plt.xlabel('predator population')
plt.ylabel('prey population')
#title
plt.title('Limit cycle')
plt.show()

#########many changes to the parameters#########
t=0
while t<100:
    t+=1
    for i in range(0,4):
        np.random.sample()
para=collection.getElementsByTagName('parameter')
for i in para:
    if i.getAttribute('id')=='k_predator_breeds':
        i.setAttribute('value','0.3')
        print(i.attributes['value'].value)
    if i.getAttribute('id')=='k_predator_dies':
        i.setAttribute('value','0.1')
        print(i.attributes['value'].value)
    if i.getAttribute('id')=='k_prey_breeds':
        i.setAttribute('value','0.9')
        print(i.attributes['value'].value)
    if i.getAttribute('id')=='k_prey_dies':
        i.setAttribute('value','0.3')
        print(i.attributes['value'].value)
copy = open('predator-prey_copy.xml','w')
DOMTree.writexml(copy)
copy.close()
xml_to_cps('predator-prey_copy.xml','predator-prey_copy.cps')

with open('modelResults.csv') as file:
    file=file.readlines()
    for i in range(len(file)):
        line=file[i]
        line=re.split(r',|\n',line)
        line.remove('')
        results.append(line)
    results=np.array(results)
    results=results[1:].astype(np.float)


#time course visualization
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#data for each curves
plt.plot(results[:,0],results[:,1], label='Predator(b=0.02,d=0.4)')
plt.plot(results[:,0],results[:,2], label='Prey(b=0.1,d=0.02)')
#for multiple curves use legend to be more clear
plt.legend()
#the x,y labels
plt.xlabel('time')
plt.ylabel('population size')
#title
plt.title('Time course')
plt.show()

#limit cycle visualization
#size and dpi of figure
plt.figure(figsize =(6,4),dpi=150)
#data for each curves
plt.plot(results[:,1],results[:,2])
#the x,y labels
plt.xlabel('predator population')
plt.ylabel('prey population')
#title
plt.title('Limit cycle')
plt.show()





    
        

    

