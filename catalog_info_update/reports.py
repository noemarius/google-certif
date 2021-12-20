#!/usr/bin/env python3
import os
import datetime
import reports
import reportlab

inputfolderpath = ""
outputfolderpath = ""
outputfilename = "processed.pdf"
keylist = ["name", "weight", "description", "image_name"]
reporttitle = "Processed Update on "+ datetime.now().strftime("%b %d, %Y")

def list_to_dict(listcontent, keylist):
    contentdict = dict(zip(keylist, listcontent)) 
    return contentdict

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def convert_txt_to_dict(filepath):
    content = []
    with open(filepath) as file:
        for line in file:
            newline = line.rstrip('\r\n')
            content.append(newline)

    formatedcontent = list_to_dict(content, keylist)
    return formatedcontent

def buildreport(attachment, title, paragraph):
    reports.generate_report(attachment, title, paragraph)

def main():
    filelist = get_foldercontent(inputfolderpath)
    filescontent = []
    for file in filelist:
        filescontent.append(convert_txt_to_dict(file)["name"])
        filescontent.append(convert_txt_to_dict(file)["weight"])
        filescontent.append(convert_txt_to_dict(file)["\\n"])
    buildreport(outputfolderpath+outputfilename, reporttitle, filescontent)




if __name__ == "__main__":
    main()