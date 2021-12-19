#!/usr/bin/env python3
import os
import requests

inputfolderpath = "./data/"
outputfolderpath = "./opt/"
keylist = ["title", "name", "date", "feedback"]
IP = "replace me"
URL = f"http://{IP}/feedback/"

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

    formatedcontent = list_to_dict(content, keylist)
    return formatedcontent

def json_to_rest(contentjson):
    try:
        response = requests.post(URL, data=contentjson)
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