#!/usr/bin/env python3
import emails
import os
import getpass
reportpath = "opt/report.pdf"
sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
password = getpass.getpass('Password? ')

def main():
    message = emails.generate_email(sender, recipient, subject, body, reportpath)
    emails.send_email(sender, password, message)


if __name__ == '__main__':
    main()
