from os import listdir
from os.path import isfile, join
from pymdeco import services
import piexif
import sys

DATE_VALUE = 36867      #described by the spec
srv = services.FileMetadataService()

def main():
    dirs = sys.argv[1:]
    for directory in dirs:
        os.chdir(directory)
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for fileName in files:
            if fileName.lower().endswith((".jpg", ".jpeg", ".heic")):
                os.rename(fileName, getPhotoDate(fileName))


def getPhotoDate(fileName):
    exif_dict = piexif.load(fileName)
    exif = exif_dict["Exif"]        #Get the exif dict
    date = exif[DATE_VALUE]
    return date

def getVideoDate(fileName):
    meta = srv.get_metadata(fileName).to_json(indent=2))
    data = meta["file_timestamps"]["modified"]

if __name__ == "__main__":
    main()
