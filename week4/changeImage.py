#!/usr/bin/env python3
from PIL import Image
import os

filepath = "./supplier-data/images/"

class Modimg():
    def __init__(self, path, r, x, y):
        self.path = path
        self.r = r
        self.x = x
        self.y = y
        self.lmg = Image.open(self.path)
        self.opt = path


    def resize_img(self):
        self.lmg = self.lmg.resize((self.x,self.y))

    def rotate_img(self):
        self.lmg = self.lmg.rotate(self.r)

    def save_img(self):
        newname = os.path.splitext(self.opt)[0]+".jpeg"
        self.lmg = self.lmg.convert("RGB")
        self.lmg = self.lmg.save(newname, 'jpeg')



def get_filelocs(folderpath):
    fileloc_list = []
    files = os.listdir(filepath)
    for file in files:
        if "tiff" in file:
            fileloc_list.append(filepath+file)
    return fileloc_list

def main():
    file_list = get_filelocs(filepath)
    print(file_list)
    for i in file_list:
        i = Modimg(i, 0, 600, 400)
        #i.rotate_img()
        i.resize_img()
        i.save_img()

if __name__ == "__main__":
    main()