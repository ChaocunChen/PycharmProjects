from time import sleep
import threading
import numpy as np
import os,re

from skimage import data
import cv2


c = zip(range(4),'abcd')
print(list(c))
a,b = zip(*zip(range(4),'abcd'))
print(a,b)
print('done!')


img=cv2.imread('/Users/chenchaocun/Downloads/JPG/JPG/IMG_2717.jpg',1)
cv2.imwrite('/Users/chenchaocun/Downloads/JPG/JPG/cc.jpg',img)
# cv2.imshow('img',img)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()


img = data.load('/Users/chenchaocun/Downloads/JPG/JPG/cc.jpg',False)
#type(img)
#np.ndarray
print(img)
mask = img < 28
img[mask] = 255
cv2.imshow('img',img)
cv2.waitKey(10000)

