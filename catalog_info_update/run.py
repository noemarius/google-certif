#!/usr/bin/env python3
import os
import requests

inputfolderpath = "./data/"
outputfolderpath = "./opt/"
keylist = ["name", "weight", "description", "image_name"]
IP = "replace me"
URL = "http://{}/feedback/".format(IP)

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def list_to_dict(listcontent, keylist):
    contentdict = dict(zip(keylist, listcontent)) 
    return contentdict

def convert_txt_to_dict(filepath):
    content = []
    with open(filepath) as file:
        for line in file:
            newline = line.rstrip('\r\n')
            content.append(newline)
    content.append(os.path.split(os.path.basename(file))+".jpg")
    formatedcontent = list_to_dict(content, keylist)
    modformatedcontent = convert_weight(formatedcontent)
    return modformatedcontent

def convert_weight(content):
    content[keylist[1]] = int(content.replace(" lbs", ""))
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
        formateddict = dict_to_json(parsedcontent)
        postedcontent = dict_to_rest(formateddict)
        print(postedcontent.text)

if __name__ == '__main__':
    main()