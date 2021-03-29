import cv2 as cv
import numpy as np
import time

# def BGR2HSV(_img):
#
#     img = _img.copy() / 255.
#
#     hsv = np.zeros_like(img, dtype=np.float32)
#
# # get max and min
#
#     max_v = np.max(img, axis=2).copy()
#
#     min_v = np.min(img, axis=2).copy()
#
#     min_arg = np.argmin(img, axis=2)
#
#
#     hsv[..., 0][np.where(max_v == min_v)]= 0
#
# ## if min == B
#
#     ind = np.where(min_arg == 0)
#
#     hsv[..., 0][ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
#
# ## if min == R
#
#     ind = np.where(min_arg == 2)
#
#     hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
#
# ## if min == G
#
#     ind = np.where(min_arg == 1)
#
#     hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300
#
# # S
#
#     hsv[..., 1] = max_v.copy() - min_v.copy()
#
# # V
#
#     hsv[..., 2] = max_v.copy()
#
#     return hsv

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*60
        else:
            h = ((g-b)/m)*60 + 360
    elif mx == g:
        h = ((b-r)/m)*60 + 120
    elif mx == b:
        h = ((r-g)/m)*60 + 240
    if mx == 0:
        s = 0
    else:
        s = m/mx
    v = mx

    #此时h,s,v值范围分别是0-360, 0-1, 0-1，在OpenCV中，H,S,V范围是0-180,0-255,0-255，加上下面代码转换：
    H = h / 2
    S = s * 255.0
    V = v * 255.0

    return H,S,V


src = cv.imread("/Users/chenchaocun/Downloads/1607584823322.jpg")



i=1
t1=time.time()
#print(src[0:1,0:1])
for x in range(src.shape[0]):
    for y in range(src.shape[1]):
        R=int(src[x:x+1,y:y+1][0][0][2])
        G=int(src[x:x+1,y:y+1][0][0][1])
        B=int(src[x:x+1,y:y+1][0][0][0])
        #print(rgb2hsv(R,G,B))
        h,s,v=rgb2hsv(R,G,B)


        #print(h,s,v)
        if (h>=11 and h<=34) and (s>=43 and s<=255) and (v>46 and v<=255) :
            i+=1
            print('yellow')
#print(i)
#print(x*y)
if float(i)/(x*y)>0.6:
    pass
    #print('过滤掉')
print(time.time()-t1)












