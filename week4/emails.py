#!/usr/bin/env python3
import smtplib
import os
from email.message import EmailMessage
import mimetypes

class Email():
    def __init__(self, sender, recipient, subject , body, attachment):
        self.s = sender
        self.r = recipient
        self.b = body
        self.o = subject
        self.mail = EmailMessage()
        self.a = attachment


    def set_params(self):
        self.mail["From"] = self.s
        self.mail["To"] = self.r
        self.mail["Subject"] = self.o
        self.mail.set_content(self.b)
        attachment_path = os.path.basename(self.a)
        print(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(self.a, 'rb') as afile:
            self.mail.add_attachment(afile.read(), maintype=mime_type,subtype=mime_subtype,filename=attachment_path)
        return self.mail
        
class MailServer():
    def __init__(self, sender, password, message):
        mailserverurl= "localhost"
        mail_server = smtplib.SMTP_SSL(mailserverurl)
        mail_server.set_debuglevel(1)
        self.ms = mail_server
        self.s = sender
        self.m = message
        self.p = password
        
    def serverauth(self):
        self.ms.login(self.s, self.p)

    def sendmail(self):
        self.ms.send_message(self.m)

    def closeconnection(self):
        self.ms.quit()


def generate_email(sender, recipient, subject, body, attachment):
    builtmail = Email(sender, recipient, subject,body, attachment)
    return builtmail

def send_email(sender, password, message):
    mail = MailServer(sender, password, message)
    mail.serverauth()
    mail.sendmail()
    mail.closeconnection()

