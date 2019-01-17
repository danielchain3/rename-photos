from os import listdir
from os.path import isfile, join
import piexif

DATE_VALUE = 36867      #described by the spec

def main(

def getDate(fileName):
    exif_dict = piexif.load(fileName)
    exif = exif_dict["Exif"]        #Get the exif dict
    date = exif[DATE_VALUE]
    return date

exif_dict = piexif.load("1.jpg")["Exif"]

