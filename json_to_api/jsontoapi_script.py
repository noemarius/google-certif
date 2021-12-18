#!/usr/bin/env python3
import os
import pandas as pd
import json

inputfolderpath = "./data/"
outputfolderpath = "./opt/"

def get_filelist(folderpath):
    filelist = []
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            filelist.append(root+file)
    return filelist

def read_csv(file):
    return pd.read_csv(file)

def export_json(dataframe, of):
    dataframe.to_json(of)

def main():
    filelist = get_filelist(inputfolderpath)
    for file in filelist:
        i = read_csv(file)
        print (i)

if __name__ == '__main__':
    main()