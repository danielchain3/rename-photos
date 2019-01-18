from os import listdir
from os.path import isfile, join
#froom pymdeco import services
import re
import os
import piexif
import sys

DATE_VALUE = 36867      #described by the spec
#srv = services.FileMetadataService()

def main():
    dirs = sys.argv[1:]
    for directory in dirs:
        files = [f for f in listdir(directory) if isfile(join(directory, f))]
        os.chdir(directory)
        for fileName in files:
            if fileName.lower().endswith((".jpg", ".jpeg")):
                os.rename(fileName, getPhotoDate(fileName))


def getPhotoDate(fileName):
    exif_dict = piexif.load(fileName)
    exif = exif_dict["Exif"]        #Get the exif dict
    date = exif[DATE_VALUE].decode("utf-8")
    name = re.sub('[^0-9]','', date) + ".jpeg"
    return name

#def getVideoDate(fileName):
#    meta = srv.get_metadata(fileName).to_json(indent=2))
#    data = meta["file_timestamps"]["modified"]

if __name__ == "__main__":
    main()
