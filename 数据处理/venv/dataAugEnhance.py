import cv2,os,random
import numpy as np
from skimage import data, exposure,transform
img_file=os.listdir('/Users/chenchaocun/Downloads/nonface/')
num=0
for im in img_file:
    img = cv2.imread('/Users/chenchaocun/Downloads/nonface/'+im)


    flag = random.uniform(0.5, 1.5)  ##flag>1为调暗,小于1为调亮
    if img is None:
        continue
    rows, cols, channels = img.shape
    dst = img.copy()

    a = random.uniform(0.5, 1.5)
    b = random.uniform(10, 100)
    angle=random.randint(5, 20)
    for i in range(rows):
        for j in range(cols):
            for c in range(3):
                color = img[i, j][c] * a + b
                if color > 255:  # 防止像素值越界（0~255）
                    dst[i, j][c] = 255
                elif color < 0:  # 防止像素值越界（0~255）
                    dst[i, j][c] = 0
    cv2.imwrite('/Users/chenchaocun/Downloads/qq/' + str(num)+'_light.jpg', dst)

    import copy
    flip_img = copy.deepcopy(img)
    flip_img = cv2.flip(flip_img, 1)#水平镜像


    print(angle)
    cv2.imwrite('/Users/chenchaocun/Downloads/qq/'+str(num)+'_flip.jpg',flip_img)

    rotate_img=transform.rotate(img, angle, preserve_range=True).astype(np.uint8)
    cv2.imwrite('/Users/chenchaocun/Downloads/qq/' + str(num)+'_'+str(angle)+'_rotate.jpg', rotate_img)
    num += 1