import cv2
img=cv2.imread('/Users/chenchaocun/Downloads/9c641795227c890d.jpg')

with open('/Users/chenchaocun/Downloads/wider_val.txt', 'r', encoding='utf-8') as f:
    annotations = f.readlines()

for an in annotations:
    if '#' in an:
        jpg_name=an.strip().split('#')
    else:
        an=an.strip().split(' ')

        print(an)
        label=[]
        cx=float(an[0])
        cy=float(an[1])
        cw=float(an[2])
        ch=float(an[3])
        x_l_eye=float(an[4])
        y_l_eye = float(an[5])
        x_r_eye = float(an[7])
        y_r_eye = float(an[8])
        x_nose= float(an[10])
        y_nose = float(an[11])
        x_l_zui =float(an[13])
        y_l_zui = float(an[14])
        x_r_zui = float(an[16])
        y_r_zui = float(an[17])
        if x_l_eye <0 or x_r_eye<0 or x_nose<0 or y_nose<0 or x_l_zui<0 or y_l_zui< 0 or x_r_zui<0 or y_r_zui<0:
            continue

        cv2.circle(img, (int(x_l_eye), int(y_l_eye)), 1, (255, 0, 0), 2)
        cv2.circle(img, (int(x_r_eye), int(y_r_eye)), 1, (255, 0, 0), 2)
        cv2.circle(img, (int(x_nose), int(y_nose)), 1, (255, 0, 0), 2)
        cv2.circle(img, (int(x_l_zui), int(y_l_zui)), 1, (255, 0, 0), 2)
        cv2.circle(img, (int(x_r_zui), int(y_r_zui)), 1, (255, 0, 0), 2)
        cv2.rectangle(img, (int(cx), int(cy)),(int(cx+cw),int(cy+ch)), (0, 0, 255), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX

    #print(im)
cv2.imshow('sf', img)
cv2.waitKey(10000)


# import shutil,os
# path='/Volumes/程序/人脸扩增/flapAndRoate_roate-AUG/rotate_5/'
# files= os.listdir(path)
# for file in files:
#     if file.endswith('.txt'):
#
#         print(os.path.join(path, file))
#         os.remove(os.path.join(path, file))