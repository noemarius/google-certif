#!/usr/bin/env python3
import os
import requests

inputfolderpath="./supplier-data/images/"
url = "http://localhost/upload/"

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def post_img(imgfile):
    with open(inputfolderpath+imgfile, 'rb') as openedfile:
        r = requests.post(url, files={'file': openedfile})
        r.raise_for_status()

def main():
    filelist = get_foldercontent(inputfolderpath)
    print(filelist)
    for file in filelist:
        if ".jpeg" in file:
            post_img(file)

if __name__ == '__main__':
    main()