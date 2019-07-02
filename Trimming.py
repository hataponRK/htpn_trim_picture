# -*- coding: utf-8 -*-

import cv2
import numpy as np
import glob
import sys
import codecs
import os

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename,dtype)
        img = cv2.imdecode(n,flags)
        return img
    except Exception as e:
        print(e)
        return None

def imwrite(filename,img,params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext,img,params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def Trimming(img):
    if img is None:
        return None

    height = img.shape[0]
    width = img.shape[1]

    trimmingWidth = (height * 16) // 9

    retPicture = img[0:height,0:trimmingWidth]
    #print("Trimming")
    #print(str(height) + "," + str(trimmingWidth))
    return retPicture


def FilesPathList(path,extension):
    fileNameList = glob.glob(path + "/*" + extension)

    print("FilesPathList")
    return fileNameList


def InputPictures(pathList):
    pictures = []

    for path in pathList:
        pictures.append(imread(path))


    print("InputPictures")
    return pictures

def OutPutPictures(pictures,fileName,directory):
    index = 0
    
    for picture in pictures:
        path = "{0}/{1}{2:03d}.png".format(directory,fileName,index)
        #print(path)
        imwrite(path,picture)
        index += 1

    print("OutPutPictures")

if __name__ == '__main__':

    #sys.stdin = codecs.getreader('utf-8')(sys.stdin)
    #sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

    print("output fileName")
    fileName = input()

    pathList = FilesPathList("./pictures",".png")

    pictures = InputPictures(pathList)

    afters = []

    for picture in pictures:
        img = Trimming(picture)
        if not(img is None):
            afters.append(Trimming(picture))
    print("Trimming")

    OutPutPictures(afters,fileName,"./result")

    print("Finished")