import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
  


for root, dirs, files in os.walk(".", topdown=False):
          for file in files:
             with open(os.path.join(root, file), "r") as auto:
                 if '.log' in file:                                               
                     if 'Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9NPE-M), Version 03.06.04.E RELEASE SOFTWARE (fc2)' in open (os.path.join(root, file)).read():
                         print('true - BOOT ' + file)
                     else:
                         print('false - BOOT ' + file)
                         # The email message
                         sender = 'geoff.hubbard@wwt.com'
                         # Put your email address in between the '' for receiver
                         receiver = 'geoff.hubbard@wwt.com'
                         # Structuring the email
                         msg = MIMEMultipart()
                         msg['From'] = sender
                         msg['To'] = receiver
                         msg['Subject'] = "Test Email"
                         body = ('false - BOOT ' + file)
                         msg.attach(MIMEText(body, 'plain'))

                         # Access sender email and send email
                         mail = smtplib.SMTP('mailhost.wwt.com', 25)
                         mail.send_message(msg)
                         mail.quit()

                     if 'ROM: 15.1(1r)SG5' in open (os.path.join(root, file)).read():
                         print('true - ROMMON ' + file)
                     else:
                         print('false - ROMMON' + file)

          

main()            


input('Press ENTER to exit')
