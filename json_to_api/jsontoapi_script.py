#!/usr/bin/env python3
import os
import pandas as pd
import json
import requests

inputfolderpath = "./data/"
outputfolderpath = "./opt/"
keylist = ["title", "name", "date", "feedback"]

def get_filelist(folderpath):
    filelist = []
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            filelist.append(root+file)
    return filelist

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def read_csv(file):
    return pd.read_csv(file)

def export_json(dataframe, of):
    dataframe.to_json(of)

def list_to_dict(listcontent, keylist):
    contentdict = dict(zip(keylist, listcontent)) 
    return contentdict

def convert_txt_to_dict(filepath):
    content = []
    with open(filepath) as file:
        for line in file:
            #i.readline()
            newline = line.rstrip('\r\n')
            content.append(newline)
        #content = content.split("\\n")
    formatedcontent = list_to_dict(content, keylist)
    return formatedcontent

def main():
    #filelist = get_filelist(inputfolderpath)
    filelist = get_foldercontent(inputfolderpath)
    for file in filelist:
        #df = read_csv(inputfolderpath+file)
        #outputfilename = outputfolderpath+os.path.splitext(os.path.basename(file))[0]+".json"
        #export_json(df, outputfilename)
        parsedcontent = convert_txt_to_dict(inputfolderpath+file)
        print(parsedcontent)
if __name__ == '__main__':
    main()