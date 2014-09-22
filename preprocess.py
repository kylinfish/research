# -*- coding: utf-8 -*-
import numpy as np
import cv2

#path = '../dataset_flower/image_'
path = '/Users/viplab/Documents/dataset/TEST/image_'
number_of_types = 5 #類別種類
type_of_images = 80 #每種類圖片張數
max_size = number_of_types * type_of_images #總共檔案數量

def featureExtraction(name, i):
    #Color mean feature :[r,g,b,label]
    #50.73430769230769, 90.87095791001451, 97.54420319303338, 1
    img = cv2.imread(name)
    means = cv2.mean(img)
    p =  list(means)
    layer = (i-1)/type_of_images
    p[3]= layer
    return (p)


def Make_feature_set(filename,labelStr):
    feature_vector=str(max_size)+", "+str(3)+", "+labelStr
    for i in range(1, max_size+1):
        index= str(i)
        if (i< 10):
            fullname = path + "000"+ index + ".jpg"
        elif (i>=10 and i <100):
            fullname  = path +"00"+index+".jpg"
        elif (i>=100 and i <1000):
            fullname = path +"0"+index+".jpg"
        else:
            fullname = path +index + ".jpg"
        feature_vector +=  "\n"+str(featureExtraction(fullname, i)).split("[")[1].split("]")[0]
    file_RW(filename,True,feature_vector)
    print "end process of feature collecting "

def file_RW(filename, empty, content):
    #empty : empty orgin file before overwrite
    if (empty == True):
        open(filename,"w").close()
    f = open(filename, "r+")
    f.write(content)
    f.close()


