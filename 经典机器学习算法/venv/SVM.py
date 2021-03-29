#coding=utf-8
import cv2
import numpy as np
im= cv2.imread('/Users/chenchaocun/Downloads/JPG/JPG/IMG_2587.jpg',0)
img2= cv2.imread('/Users/chenchaocun/Downloads/JPG/JPG/IMG_2589.jpg',0)
hest = 0


h,w = np.shape(im)
for row in range(h):
    for col in range(w):
        #print(im[row][col])
        hest=im[row][col]
    print(hest)
print('hest={}'.format(hest))

