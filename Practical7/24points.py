# -*- coding: utf-8 -*-
"""
Created on Mon April 1 18:52:23 2019

@author: ROBIN, inspired by yangjiaolei
"""
#inport fraction for division
from fractions import Fraction
#input string (4 numbers)
numstr=input("Please input numbers to computer 24:(use ',' to divide them)\n")
#recursive function to calculate 24 points
def Cal(n):
            global t
            #counter
            t+=1
            #at the bottom of the recursion 'tree' check the result
            if n == 1:
                if float(num[0]) == 24:
                    return 1#'1' indicates 24 has been calculated successifully
                else:
                    return 0#'0' indicates no '24' was found
            else:
                #choose 2 numbers i,j in order for operation. n is the list length
                for i in range(n):
                    for j in range(i+1,n):
                        #store i,j in a,b
                        a = num[i]
                        b = num[j]
                        #remove i,j
                        #the last number that replaces j
                        num[j] = num[n-1]
                        
                        #use 4 operations to calculate a new number and replace i in list
                        num[i] = a+b
                        #recursion is used for each operation respectively
                        if Cal(n-1):
                            return 1
                        
                        num[i] = a-b
                        if Cal(n-1):
                            return 1
                    
                        num[i] = b-a
                        if Cal(n-1):
                            return 1
                    
                        num[i] = a*b
                        if Cal(n-1):
                            return 1
                        #floats are not precise.
                        #if floats are used, use approximate number in the result (a small range around 24)
                        if a != 0:
                            num[i] = Fraction(b,a)
                            if Cal(n-1):
                                return 1
                            
                        if b != 0:
                            num[i] = Fraction(a,b)
                            if Cal(n-1):
                                return 1
            
            return 0
#input must be integers not floats
if "." in numstr or "/" in numstr:
    print("The input number must be integers from 1 to 23")
else:
    #create a list to store input numbers
    numlist=numstr.split(",")
    #convert str to int
    num=list(map(int,numlist))
    #numbers must be between 1 and 23
    if max(num)>23 or min(num)<1:
        print("The input number must be integers from 1 to 23")
    #calculate 24 points
    else:
        #initiate counter
        t=0
        #24 exists (return 1)
        if Cal(len(num)):
            print("Yes")
        #no 24 was found (return 0)
        else:
            print("No")
        #print recursion time
        print("Recursion times:"+str(t))