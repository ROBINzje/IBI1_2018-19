# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:53:46 2019

@author: 94979
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import re

sub=[]
name=[]
email=[]

contentlist=[]
sub_new=[]
name_new=[]
email_new=[]

re_loginname = re.compile(r'(\S+)@')
fhand = open(r'D:\test\IBI1_2018-19\practical6\address_information.csv','r')
#use with statement to close file after it is used.
#with open(lfile,'r') as infor
read=fhand.read()


All = re.split(r',|\n',read)

#extract the email header
for c in All:
    if re.match('^T',c):
        sub.append(c)
#mlist=[]
#for i in range(0,len(all),3)：
        #
#filter_list = mlist

#extract names
for n in All:
    if re.match('[A-Z][a-z]+$',n):
        name.append(n)
name.remove('Subject')# remove the exception'Subject'

#extract email address
for m in All:
    if re.match(r'^[0-9A-Za-z_]+@[0-9A-Za-z_\.]+$',m):
        email.append(m)



body = open(r'D:\test\IBI1_2018-19\practical6\body.txt')
text = ''
for line in body:
    text += line #read body line by line
body.close()      
str1=r'^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$'


for i in range(0,len(email)):
    if re.match(str1,email[i]):#find the legal email addresses
        print(email[i]+" "+":"+"Correct Address")
        sub_new.append(sub[i])
        name_new.append(name[i])
        email_new.append(email[i])
    else:
        print(email[i]+" "+":"+"Wrong Address")
      

#send emails for every legal email address
sender = input('From: ')
password = input('Password: ')
username=re_loginname.search(sender).group(1)
mail_host="smtp.zju.edu.cn"  

 
for u in range(0,len(email_new)):
    subject=sub_new[u]
    content_new=re.sub(r'user',name[i],text)#replace the salutation with names      
    
    msg = MIMEText(content_new, 'plain', 'utf-8')
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] =  Header(email_new[u], 'ascii')
    msg['Subject'] = Header(subject,'utf-8')
    
    try:
        server = smtplib.SMTP('smtp.zju.edu.cn',25)
        server.login(username, password)
        server.sendmail(sender, [email_new[u]], msg.as_string())
        server.quit()
        print('Mail sent successfully!')
    except smtplib.SMTPException:
        print('Mail delivery failed')