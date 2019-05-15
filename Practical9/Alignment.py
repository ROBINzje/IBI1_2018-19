"""
Created on Wed Apr 17 10:27:02 2019

@author: ROBIN
"""
#import necessary package
import pandas as pd
#create a dictionary for biosum62 
dic={}
#import the matrix
text=open('biosum62.txt').read()
lines=text.splitlines()
#get each idnex for the dic

index1=lines[0].split()
for line in lines[1:]:
    splitted=line.split()
    dic_for_each={}
    for i in index1:
        value=splitted[index1.index(i)+1]
        dic_for_each[i]=value
    dic[line[0]]=dic_for_each
def score(x1,x2):#x1,x2 are sequences
    p=0
    alignment=[]
    name1=x1.splitlines()[0]    
    name2=x2.splitlines()[0]
    list1=list(x1.splitlines()[1:][0])   
    list2=list(x2.splitlines()[1:][0])
    for num in range(len(list1)):#x1,x2 are of the same length
       nu_acid1=list1[num]
       nu_acid2=list2[num]
       single_score=int(dic[nu_acid1][nu_acid2])
       p+=single_score
       if nu_acid1==nu_acid2:
           alignment.append(nu_acid1)
       elif single_score>=0:
           alignment.append('+')
       else:
           alignment.append(' ')
    df=pd.DataFrame({name1:x1.splitlines()[1:][0],"alignment":''.join(alignment),name2:x2.splitlines()[1:][0]},index=[0])    
    score_per_aa=p/len(list1)
    print(df.unstack())
    print('score for each amino acid is '+str(score_per_aa))
    print('overall score is '+str(p))
    return  
seq1=open('seq1.txt').read()
seq2=open('seq2.txt').read()
seq3=open('seq3.txt').read()
score(seq1,seq2)
score(seq1,seq3)
score(seq2,seq3)
