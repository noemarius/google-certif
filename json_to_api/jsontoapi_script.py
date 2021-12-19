#!/usr/bin/env python3
import os
import json
import requests

inputfolderpath = "./data/"
outputfolderpath = "./opt/"
keylist = ["title", "name", "date", "feedback"]
IP = ""
URL = f"http://{IP}/feedback"

def get_filelist(folderpath):
    filelist = []
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            filelist.append(root+file)
    return filelist

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def dict_to_json(contentdict):
    return json.dumps(contentdict)


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
        response = requests.post(URL, json=contentjson)
        response.raise_for_status()
        return response
    except Exception as e:
        print(e)

def main():
    filelist = get_foldercontent(inputfolderpath)
    for file in filelist:
        parsedcontent = convert_txt_to_dict(inputfolderpath+file)
        formatedjson = dict_to_json(parsedcontent)
        postedcontent = json_to_rest(formatedjson)
        print(postedcontent.text)

if __name__ == '__main__':
    main()