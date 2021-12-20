#!/usr/bin/env python3
import os
import requests

inputfolderpath=""
url = "http://localhost/upload/"

def get_foldercontent(folderpath):
    return os.listdir(folderpath)

def post_img(imgfile):
    with open(imgfile, 'rb') as openedfile:
        r = requests.post(url, files={'file': openedfile})
        r.raise_for_status()

def main():
    filelist = get_foldercontent(inputfolderpath)
    for file in filelist:
        post_img(file)

if __name__ == '__main__':
    main()