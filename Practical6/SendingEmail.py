# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:05:15 2019

@author: ROBIN
"""
#import necessary pkgs, including re, pandas, and pkgs for sending emails
import re
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import getpass


#define function to send the email, given the information of the sender and the receiver
def send_email(addr,subject,text):
    ##prepare information to send an email
    server = smtplib.SMTP(sv,25) #setup SMTP object, port for server is 25
    server.login(sender, pw) #log in using the sender address and password
    msg = MIMEText(text, 'plain', 'utf-8') #decode the body text
    #specify the subject, sender address and receiver address
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] =  Header(addr, 'ascii')
    #send the email
    try:
        server.sendmail(sender, addr, str(msg))
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Error")
    server.quit()
    
#read the body text and convert it to a list where each line is converted to a string element
with open('body.txt') as body:
    body=body.readlines()
#read address information as dataframe
df=pd.read_csv('address_information.csv')
#a list to store the names with correct email addresses
addrlist=[]
sbjlist=[]
sdbodylist=[]
#a loop to judge whether the email address is correct or nto, for the correct addresses, end the eamil
for i in df['EmailAddress'].values:
    #correct address always start with 'i', it can also be replaced by other functions (such as re.search(r'com',i)!=None)
    if i.startswith('i'):
        #print the correct address
        print(i+' :Correct Address!')
        #find the line with correct address for searching the corresponding name and subject
        line=df.loc[df['EmailAddress'] == i]
        #use the line to find the name
        validname=line['name'].values
        #use the line to find the subject
        subject=line['Subject'].values
        #extract the first line of the body text, it is going to be changed
        fstline=body[0]
        #replace 'User' with the correct name
        sdline=re.sub('User',validname[0],fstline)
        #replace the original first line the the modified one and convert the  body text list to a string object
        body[0]=sdline
        sdbody=''.join(body)
        #store the information of the correct names, email addresses, subjects, body texts to four lists respectively.
        addrlist.append(i)
        sbjlist.append(subject[0])
        sdbodylist.append(sdbody)
    #for the wrong address just print out it
    else:
        print(i+' :Wrong Adress!')


#to sign in, input the email address and password from the sender
sender=input('From: ')
#the server name
sv='smtp.'+re.findall('@(.+)', sender)[0]
pw=getpass.getpass('Password: ')

#actually send the email to the selected addresses
for j in range(len(addrlist)):
    send_email(addrlist[j],sbjlist[j],sdbodylist[j])

