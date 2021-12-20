#!/usr/bin/env python3
import os
import requests

inputfolderpath = "./supplier-data/descriptions/"
outputfolderpath = "./opt/"
keylist = ["name", "weight", "description", "image_name"]
IP = "localhost"
URL = "http://{}/fruits/".format(IP)

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def list_to_dict(listcontent, keylist):
    contentdict = dict(zip(keylist, listcontent))
    return contentdict

def convert_txt_to_dict(filepath):
    content = []
    with open(filepath) as file:
        for line in file:
            newline = line.rstrip()
            content.append(newline)
    filename = os.path.basename(filepath).replace(".txt",".jpeg")
    print(content)
    print(filename)
    content[3] = filename
    formatedcontent = list_to_dict(content, keylist)
    modformatedcontent = convert_weight(formatedcontent)
    return modformatedcontent

def convert_weight(content):
    content[keylist[1]] = int(content[keylist[1]].strip(" lbs"))
    return content

def json_to_rest(contentdict):
    try:
        response = requests.post(URL, data=contentdict)
        response.raise_for_status()
        return response
    except Exception as e:
        print(e)

def main():
    filelist = get_foldercontent(inputfolderpath)
    for file in filelist:
        parsedcontent = convert_txt_to_dict(inputfolderpath+file)
        #postedcontent = json_to_rest(parsedcontent)
        print(parsedcontent)

if __name__ == '__main__':
    main()