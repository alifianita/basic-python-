#!/usr/bin/env python
# coding: utf-8

# In[17]:


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()

server = 'smtp.gmail.com'
portmail = 587

message = "Python Final Project"
sender = "haesunpia.yo@gmail.com"
receiver = ['reall.alifianita@gmail.com', 'amalia.alifianita@gmail.com']

password = "Blackpinkinyourarea"
msg['From'] = "haesunpia.yo@gmail.com"
msg['To'] = " , ".join(receiver)
msg['Subject'] = "Hallo"

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

server.login(msg['From'], "Blackpinkinyourarea")

server.sendmail(sender,receiver, msg.as_string())

server.quit()

print ("Successfully sent email to receiver")

#sources
#https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975
#https://answer-id.com/id/53557096


# In[ ]:




