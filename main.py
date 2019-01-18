from os import listdir
from os.path import isfile, join
import re, os, piexif, sys

DATE_VALUE = 36867      #described by the spec

def main():
    dirs = sys.argv[1:]
    for directory in dirs:
        files = [f for f in listdir(directory) if isfile(join(directory, f))]
        os.chdir(directory)
        for fileName in files:
            if fileName.lower().endswith((".jpg", ".jpeg")):
                os.rename(fileName, getPhotoDate(fileName))
            else:
                print(fileName + " is not a valid image")


def getPhotoDate(fileName):
    exif_dict = piexif.load(fileName)
    exif = exif_dict["Exif"]        #Get the exif dict
    date = exif[DATE_VALUE].decode("utf-8")
    name = re.sub('[^0-9]','', date) + ".jpeg"
    return name

if __name__ == "__main__":
    main()
