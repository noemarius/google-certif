from PIL import Image

filepath = "./data/1.jpg"

def load_img(fileloc):
    return Image.open(fileloc)

def resize_img(lfile):
    return lfile.resize((640,480))

def rotate_img(lfile):
    return lfile.rotate(45)

def save_file(modifiedfile, filename):
    return modifiedfile.save(filename)

def main():
    loadedfile = load_img(filepath)
    rotatedimg = rotate_img(loadedfile)
    resizedimg = resize_img(rotatedimg)
    save_file(resizedimg, "./data/modimg.jpg")

if __name__ == "__main__":
    main()
