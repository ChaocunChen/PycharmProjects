import numpy as np
import cv2
import os
import json
from lxml import etree
import  os
import cv2
import xml.etree.ElementTree as ET

# path = '/Users/chenchaocun/Downloads/fruit/Annotations/'
# #move_path = '/Users/chenchaocun/Downloads/ccc/'
# text_list=os.listdir(path)
# text_list.sort()
#
# #print(text_list)
#
#
# for an in text_list:
#     #print(an)
#     if an.endswith('.xml'):
#         if an[0] == '.':
#             continue
#
#         myin_file = open(path + an)
#         mytree = ET.parse(myin_file)
#         myrootsrc = mytree.getroot()
#         for name in myrootsrc.iter('annotation'):
#             #jpg_name=name.find('path').text.split('/')[1].split('.')[0]
#             jpg_name=an.split('.xml')[0]
#             print(jpg_name)
#
#
#
#         for obj in myrootsrc.iter('size'):
#             w = obj.find('width').text
#             h = obj.find('height').text
#             #print(w,h)
#
#         label_txt=open('/Users/chenchaocun/Downloads/fruit/yolov5/'+jpg_name+'.txt','a+')
#
#         for target in myrootsrc.iter('object'):
#
#             bb=target.find('bndbox')
#             print(bb)
#             label_name=target.find('name').text
#             #print(label_name)
#
#
#             xmax = bb.find('xmax').text
#
#             ymax = bb.find('ymax').text
#             x_center=(float(xmax)+float(bb.find('xmin').text))/2
#             y_center=(float(ymax)+float(bb.find('ymin').text))/2
#
#             xmin = int(bb.find('xmin').text)
#             ymin = int(bb.find('ymin').text)
#             x_center_=x_center/float(w)
#             y_center_=y_center/float(h)
#             w_=str((int(xmax)-int(xmin))/(float(w)))
#             h_= str((int(ymax)-int(ymin))/(float(h)))
#             writ_txt = '0' + ' ' + str(x_center_) + ' ' + str(y_center_) + ' ' + w_ + ' ' + h_ + '\n'
#
#             # if label_name=='sleep':
#             #     writ_txt = '1' + ' ' + str(x_center_) + ' ' + str(y_center_) + ' ' + w_ + ' ' + h_ + '\n'
#             #
#             #
#             # if label_name=='noaction':
#             #     writ_txt = '0' + ' ' +str(x_center_)+' '+str(y_center_) +' '+w_ +' ' +h_ +'\n'
#             print(writ_txt)
#             label_txt.write(writ_txt)
#         label_txt.close()




img=cv2.imread('/Users/chenchaocun/Downloads/wider_9994.jpg')

with open('/Users/chenchaocun/Downloads/wider_9994.txt', 'r', encoding='utf-8') as f:
    annotations = f.readlines()
for an in annotations:
    an=an.strip().split(' ')
    print(an)
    label=an[0]
    cx=float(an[1])
    cy=float(an[2])
    cw=float(an[3])
    ch=float(an[4])

    h,w,c=img.shape
    x1=int(w*cx) - int(int(cw*w)/2)
    y1=int(h*cy) - int(int(ch*h)/2)
    x2=x1+int(cw*w)
    y2=y1+int(ch*h)
    # if (x2-x1)>900:
    #     print(im)
    cv2.rectangle(img, (x1, y1),(x2,y2), (0, 0, 255), 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, label, (x1, y1), font, 1.2, (255, 255, 255), 2)
    #print(im)
cv2.imshow('sf', img)
cv2.waitKey(10000)

# img_list=os.listdir('/Users/chenchaocun/Downloads/fruit/JPEGImages')
# for im in img_list:
#     im_name=im.split('.jpg')[0]
#
#
#     img=cv2.imread('/Users/chenchaocun/Downloads/fruit/JPEGImages/'+im)
#
#     with open('/Users/chenchaocun/Downloads/1212/'+im_name+'.txt', 'r', encoding='utf-8') as f:
#         annotations = f.readlines()
#     for an in annotations:
#         an=an.strip().split(' ')
#         label=an[0]
#         cx=float(an[1])
#         cy=float(an[2])
#         cw=float(an[3])
#         ch=float(an[4])
#
#         h,w,c=img.shape
#         x1=int(w*cx) - int(int(cw*w)/2)
#         y1=int(h*cy) - int(int(ch*h)/2)
#         x2=x1+int(cw*w)
#         y2=y1+int(ch*h)
#         # if (x2-x1)>900:
#         #     print(im)
#         cv2.rectangle(img, (x1, y1),(x2,y2), (0, 0, 255), 1)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img, label, (x1, y1), font, 1.2, (255, 255, 255), 2)
#         #print(im)
#     cv2.imshow('sf', img)
#     cv2.waitKey(1000)