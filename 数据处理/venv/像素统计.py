import cv2 as cv
import numpy as np

src = cv.imread("/Users/chenchaocun/Downloads/1607584823322.jpg", cv.IMREAD_GRAYSCALE)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

min, max, minLoc, maxLoc = cv.minMaxLoc(src)
print("min: %.2f, max: %.2f"% (min, max))
print("min loc: ", minLoc)
print("max loc: ", maxLoc)

means, stddev = cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f"% (means, stddev))


# import os,shutil
# img_path='/Users/chenchaocun/Desktop/openimages_20_8_0.99_result/'
# resut_path='/Users/chenchaocun/Downloads/ccc/'
# save_path = '/Users/chenchaocun/Downloads/openimgaes_partial/'
# jpg_list = [x.strip() for x in os.listdir(img_path) if x.endswith('.jpg')]
# #print(jpg_list)
# resut_list= [x.strip() for x in os.listdir(resut_path) if x.endswith('.jpg')]
# #print(resut_path)
# a = [x for x in jpg_list if x in resut_list]
#
# for jpg_name in a:
#     print(jpg_name)
#     shutil.move(img_path+jpg_name,save_path+jpg_name)
