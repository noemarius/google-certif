#!/usr/bin/env python3
import emails
import os
import reports
import datetime


sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

inputfolderpath = "supplier-data/descriptions/"
outputfolderpath = "/tmp/"
outputfilename = "processed.pdf"
keylist = ["name", "weight", "description", "image_name"]
reporttitle = "Processed Update on "+ datetime.datetime.now().strftime("%b %d, %Y")
reportpath = outputfolderpath+outputfilename

def list_to_dict(listcontent, keylist):
    contentdict = dict(zip(keylist, listcontent)) 
    return contentdict

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def convert_txt_to_dict(filepath):
    content = []
    with open(inputfolderpath+filepath) as file:
        for line in file:
            newline = line.rstrip('\r\n')
            content.append(newline)

    formatedcontent = list_to_dict(content, keylist)
    return formatedcontent

def main():
    filelist = get_foldercontent(inputfolderpath)
    filescontent = []
    for file in filelist:
        filescontent.append(convert_txt_to_dict(file)["name"])
        filescontent.append(convert_txt_to_dict(file)["weight"])
    mergedcontent = '\\n'.join([str(elem) for elem in filescontent])
    reports.generate_report(reportpath, reporttitle, mergedcontent)

    message = emails.generate_email(sender, recipient, subject, body, reportpath)
    print(message)
    emails.send_email(sender, message)


if __name__ == '__main__':
    main()
