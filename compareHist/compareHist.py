import numpy as np
import cv2
import random
# org = []
for x in xrange(1,31):
    org.append(x)
images1={}
index1={}
images2={}
index2={}
result=[]

def readImageCalHist(imagePath,ind_dic,img_dic):
    # extract the image filename (assumed to be unique) and
    # load the image, updating the images dictionary
    filename = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    img_dic[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # extract a 3D RGB color histogram from the image,
    # using 8 bins per channel, normalize, and update
    # the index
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
    [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist).flatten()
    ind_dic[filename] = hist    
    
    
#======== first class =======#
for i in org:
    count = str(i)
    if i <10:
        count = str(0)+str(i)
    im = "/Users/viplab/Documents/dataset/tmp/crocodile/image_00"+count+".jpg"
    readImageCalHist(im,index1,images1)
    
#======== second class =======#
for i in xrange(1,31):
    count = str(i)
    if i <10:
        count = str(0)+str(i)
    im = "/Users/viplab/Documents/dataset/tmp/sunflower/image_00"+count+".jpg"
    readImageCalHist(im,index2,images2)
    
#Method: CV_COMP_CORREL , CV_COMP_INTERSECT , CV_COMP_CHISQR 

for i in xrange(0,30):
    c1 = index1.values()[i]
    c2 = index2.values()[i]
    d = cv2.compareHist(c1,c2, cv2.cv.CV_COMP_CHISQR )
    result.append(d)
    
    
totall_d = sum(result)
avg = totall_d / len(result)
print 'result: ',result 
print 'totaly',totall_d 
print 'avg:' , avg
