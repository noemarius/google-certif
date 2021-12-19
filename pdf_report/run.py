#! /usr/bin/env python3

import smtplib
import os
from email.message import EmailMessage
import getpass
import mimetypes
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

class Email():
    def __init__(self, sender, recipient, body, attachment):
        self.s = sender
        self.r = recipient
        self.b = body
        self.mail = EmailMessage()
        self.a = attachment


    def set_params(self):
        self.mail["From"] = self.s
        self.mail["To"] = self.r
        self.mail.set_content(self.b)
        attachment_path = os.path.basename(self.a)
        print(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(self.a, 'rb') as afile:
            self.mail.add_attachment(afile.read(), maintype=mime_type,subtype=mime_subtype,filename=attachment_path)
        return self.mail

class MailServer():
    def __init__(self, sender, password, message) -> None:
        mailserverurl= ""
        mail_server = smtplib.SMTP_SSL(mailserverurl)
        mail_server.set_debuglevel(1)
        self.ms = mail_server
        self.s = sender
        self.p = password
        self.m = message
        
    def serverauth(self):
        self.ms.login(self.s, self.p)

    def sendmail(self):
        self.ms.send_message(self.m)

    def closeconnection(self):
        self.ms.quit()


class BuildReport():
    def __init__(self, outputfile, inputdata, title):
        self.id = inputdata
        self.of = outputfile
        self.t = title
        report = SimpleDocTemplate(self.of)
        self.report = report

    def make_table(self):
        table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
        table_data = []
        for k, v in self.id.items():
            table_data.append([k, v])
        report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
        return report_table

    def make_pie(self):
        report_pie = Pie(width=3, height=3)
        report_pie.data = []
        report_pie.labels = []
        for id_name in sorted(self.id):
            report_pie.data.append(self.id[id_name])
            report_pie.labels.append(id_name)
        report_chart = Drawing()
        report_chart.add(report_pie)
        return report_chart

    def make_report(self):
        styles = getSampleStyleSheet()
        report_title = Paragraph(self.t, styles["h1"])
        try:
            self.report.build([report_title, self.make_table(), self.make_pie()])
        except Exception as e:
            print(e)

def main():
    #mail_pass = getpass.getpass('Password? ')
    sender = "noe.marius@gmail.com"
    recipient = "notme@gmail.com"
    body = "just a bunch of random letters"
    attachment = "./data/dumd.txt"
    outputfile = "./opt/report.pdf"
    title = "A Complete Inventory of My Fruit"
    fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
    }
    #newmail = Email(sender, recipient, body, attachment)
    #print (newmail.set_params())
    newreport = BuildReport(outputfile, fruit, title)
    print(newreport.make_report())

if __name__ == "__main__":
    main()