# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:54:25 2019

@author: ROBIN
"""
#import pkgs
import xml.dom.minidom
import re
import pandas as pd

DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
find_str=collection.getElementsByTagName("defstr")
targets=[]
idlist=[]
namelist=[]
deflist=[]
childnumberlist=[]
direct_children={}
terms=collection.getElementsByTagName('term')

#use recursion to find total children of one parent t and store the numbers into generation_list
def findchild (t):  
    #at the bottom--no children
    if t not in direct_children:
        return 
    else:
        generation_list.append(len(direct_children[t]))
        for child in direct_children[t]:
            findchild(child)
#go through each term
for t in terms:    
    #extract information
    text=t.getElementsByTagName('defstr')[0]  
    name=t.getElementsByTagName('name')[0].childNodes[0].data
    data=text.childNodes[0].data
    idd=t.getElementsByTagName('id')[0].childNodes[0].data
    #find the autophagosome-related term
    if re.search("autophagosome",data)!=None:
        #add information into corresponding lists
        targets.append(t)              
        definition=data
        idlist.append(idd)
        namelist.append(name)
        deflist.append(definition)
    #create a dictionary of parents with their direct children
    #first find direct parents
    if t.getElementsByTagName('is_a'):       
        parents=t.getElementsByTagName('is_a')
        #may have many parents
        for i in parents:
            #parents id
            parent=i.childNodes[0].data
            #store parent id in direct_children if it has direct children
            if parent in direct_children:
                direct_children[parent].add(idd)
            else:
                direct_children[parent]={idd}
#find total number of children (all generations)
for targetid in idlist:
    if targetid not in direct_children:
        childnumberlist.append(0)
    else:
        generation_list=[]#the numbers of children for each generation
        #fill in generation_list
        findchild(targetid)  
        #numbers of children of the top parent: sum up the generation_list
        ch_num=sum(generation_list)
        #record the child numbers for the dataframe
        childnumberlist.append(ch_num)
        
#use dataframe to integrate information
df=pd.DataFrame({'id':idlist,'name':namelist,'definition':deflist,'childnodes':childnumberlist})
df.index = range(1,len(df)+1) 
#convert df to excel
df.to_excel(r'C:\Users\ROBIN\Desktop\GK project\IBI1_2018-19\Practical8\go_obo.xlsx')

    
    
  
        