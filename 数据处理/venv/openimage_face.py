import requests
from lxml import etree
from time import  sleep
import  os
import csv
import numpy as np
import cv2
from shutil import copyfile

tlist=['ImageID',
       'Source',
       'LabelName',
       'Confidence',
       'XMin',
       'XMax',
       'YMin',
       'YMax',
       'IsOccluded',
       'IsTruncated',
       'IsGroupOf',
       'IsDepiction',
       'IsInside']
csvf=csv.reader(open('/Users/chenchaocun/Downloads/train-annotations-bbox.csv','r'))


flag=0
dit_person={}
dit_car={}
dit_head={}
dit_face={}
for cs in csvf:
    if flag==0:
        flag+=1  #排除第一行表头
        continue
    name = cs[0]
    if cs[1]=='activemil' and float(cs[3])<0.7:
        continue

    if cs[2]=='/m/01g317':#人
        if (not name in dit_person.keys()):
            dit_person[name]=[]
        box=cs[4:8]
        for b in box:
            dit_person[name].append(b)
    elif cs[2]=='/m/04hgtk':#人头
        if (not name in dit_head.keys()):
            dit_head[name]=[]
        box = cs[4:8]
        for b in box:
            dit_head[name].append(b)
    elif cs[2]=='/m/0dzct':#人脸
        if (not name in dit_face.keys()):
            dit_face[name]=[]
        box = cs[4:8]
        for b in box:
            dit_face[name].append(b)

import  zipfile
# igp='/Volumes/Car/train_01/'
# iglist=os.listdir(igp)
num=0
ziplist=['/Volumes/学习/openimageV2/train_01.zip','/Volumes/学习/openimageV2/train_02.zip',
         '/Volumes/学习/openimageV2/train_03.zip',
         '/Volumes/学习/openimageV2/train_04.zip',
         '/Volumes/学习/openimageV2/train_05.zip',
          '/Volumes/学习/openimageV2/train_06.zip',
         '/Volumes/学习/openimageV2/train_07.zip',
         '/Volumes/学习/openimageV2/train_08.zip']
for z in ziplist:
    print(z)
    with zipfile.ZipFile(z, mode='r') as zfile:  # 只读方式打开压缩包
        flag=0
        for zp in zfile.filelist:  # 获取zip文档内所有文件的名称列表
            if flag==0:
                flag+=1
                continue
            name=str(zp.filename)
            num += 1
            print(z,num)
            with zfile.open(name, mode='r') as image_file:
                content = image_file.read()  # 一次性读入整张图片信息
                img = np.asarray(bytearray(content), dtype='uint8')
                img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                # cv2.imshow('image', image)
                # cv2.waitKey(5000)
                ig=name.split('/')[1]
                dk = ig.split('.jpg')[0]
                # if dk in dit_person.keys():
                #     box = dit_person[dk]
                #     h, w, c = img.shape
                #     boxes = np.array(box, dtype=np.float32).reshape(-1, 4)
                #     # ------------------------新建xml
                #     root = etree.Element("annotation")
                #     child1 = etree.SubElement(root, "folder")
                #     child1.text = "JPEGImages"
                #     child2 = etree.SubElement(root, "filename")
                #     child2.text = ig
                #     child3 = etree.SubElement(root, "path")
                #     child3.text = "JPEGImages/" + ig
                #     child4 = etree.SubElement(root, "source")
                #     child5 = etree.SubElement(child4, 'database')
                #     child5.text = 'Unknown'
                #     child6 = etree.SubElement(root, 'size')
                #     child7 = etree.SubElement(child6, 'width')
                #     child7.text = str(w)
                #     child8 = etree.SubElement(child6, 'height')
                #     child8.text = str(h)
                #     child9 = etree.SubElement(child6, 'depth')
                #     child9.text = str(c)
                #     child10 = etree.SubElement(root, 'segmented')
                #     child10.text = '0'
                #     # ----------------------------
                #     for b in boxes:
                #         x1 = int(w * float(b[0]))
                #         x2 = int(w * float(b[1]))
                #         y1 = int(h * float(b[2]))
                #         y2 = int(h * float(b[3]))
                #         # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                #         # 生成xml
                #         child11 = etree.SubElement(root, 'object')
                #         child12 = etree.SubElement(child11, 'name')
                #         child12.text = 'person'
                #         child13 = etree.SubElement(child11, 'pose')
                #         child13.text = 'Unspecified'
                #         child14 = etree.SubElement(child11, 'truncated')
                #         child14.text = '0'
                #         child15 = etree.SubElement(child11, 'difficult')
                #         child15.text = '0'
                #         child16 = etree.SubElement(child11, 'bndbox')
                #         child17 = etree.SubElement(child16, 'xmin')
                #         child17.text = str((int)(x1))
                #         child18 = etree.SubElement(child16, 'ymin')
                #         child18.text = str((int)(y1))
                #         child19 = etree.SubElement(child16, 'xmax')
                #         child19.text = str((int)(x2))
                #         child20 = etree.SubElement(child16, 'ymax')
                #         child20.text = str((int)(y2))
                #     tree = etree.ElementTree(root)
                #     tree.write('/Volumes/Car/提取类型/person/xml/' + dk + '.xml', pretty_print=True, xml_declaration=True,
                #                encoding='utf-8')
                #     cv2.imwrite('/Volumes/Car/提取类型/person/ig/'+ig,img)
                    # cv2.imshow('df', img)
                    # cv2.waitKey(5000)
                # elif dk in dit_head.keys():
                #     box = dit_head[dk]
                #     h, w, c = img.shape
                #     boxes = np.array(box, dtype=np.float32).reshape(-1, 4)
                #     # ------------------------新建xml
                #     root = etree.Element("annotation")
                #     child1 = etree.SubElement(root, "folder")
                #     child1.text = "JPEGImages"
                #     child2 = etree.SubElement(root, "filename")
                #     child2.text = ig
                #     child3 = etree.SubElement(root, "path")
                #     child3.text = "JPEGImages/" + ig
                #     child4 = etree.SubElement(root, "source")
                #     child5 = etree.SubElement(child4, 'database')
                #     child5.text = 'Unknown'
                #     child6 = etree.SubElement(root, 'size')
                #     child7 = etree.SubElement(child6, 'width')
                #     child7.text = str(w)
                #     child8 = etree.SubElement(child6, 'height')
                #     child8.text = str(h)
                #     child9 = etree.SubElement(child6, 'depth')
                #     child9.text = str(c)
                #     child10 = etree.SubElement(root, 'segmented')
                #     child10.text = '0'
                #     # ----------------------------
                #     for b in boxes:
                #         x1 = int(w * float(b[0]))
                #         x2 = int(w * float(b[1]))
                #         y1 = int(h * float(b[2]))
                #         y2 = int(h * float(b[3]))
                #         # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                #         # 生成xml
                #         child11 = etree.SubElement(root, 'object')
                #         child12 = etree.SubElement(child11, 'name')
                #         child12.text = 'head'
                #         child13 = etree.SubElement(child11, 'pose')
                #         child13.text = 'Unspecified'
                #         child14 = etree.SubElement(child11, 'truncated')
                #         child14.text = '0'
                #         child15 = etree.SubElement(child11, 'difficult')
                #         child15.text = '0'
                #         child16 = etree.SubElement(child11, 'bndbox')
                #         child17 = etree.SubElement(child16, 'xmin')
                #         child17.text = str((int)(x1))
                #         child18 = etree.SubElement(child16, 'ymin')
                #         child18.text = str((int)(y1))
                #         child19 = etree.SubElement(child16, 'xmax')
                #         child19.text = str((int)(x2))
                #         child20 = etree.SubElement(child16, 'ymax')
                #         child20.text = str((int)(y2))
                #     tree = etree.ElementTree(root)
                #     tree.write('/Volumes/程序/挑选类型/head1/xml/' + dk + '.xml', pretty_print=True, xml_declaration=True,
                #                encoding='utf-8')
                #     cv2.imwrite('/Volumes/程序/挑选类型/head1/ig/' + ig, img)
                #     # cv2.imshow('df', img)
                #     # cv2.waitKey(5000)
                if dk in dit_face.keys():
                    box = dit_face[dk]
                    h, w, c = img.shape
                    boxes = np.array(box, dtype=np.float32).reshape(-1, 4)
                    # ------------------------新建xml
                    root = etree.Element("annotation")
                    child1 = etree.SubElement(root, "folder")
                    child1.text = "JPEGImages"
                    child2 = etree.SubElement(root, "filename")
                    child2.text = ig
                    child3 = etree.SubElement(root, "path")
                    child3.text = "JPEGImages/" + ig
                    child4 = etree.SubElement(root, "source")
                    child5 = etree.SubElement(child4, 'database')
                    child5.text = 'Unknown'
                    child6 = etree.SubElement(root, 'size')
                    child7 = etree.SubElement(child6, 'width')
                    child7.text = str(w)
                    child8 = etree.SubElement(child6, 'height')
                    child8.text = str(h)
                    child9 = etree.SubElement(child6, 'depth')
                    child9.text = str(c)
                    child10 = etree.SubElement(root, 'segmented')
                    child10.text = '0'
                    # ----------------------------
                    for b in boxes:
                        x1 = int(w * float(b[0]))
                        x2 = int(w * float(b[1]))
                        y1 = int(h * float(b[2]))
                        y2 = int(h * float(b[3]))
                        # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                        # 生成xml
                        child11 = etree.SubElement(root, 'object')
                        child12 = etree.SubElement(child11, 'name')
                        child12.text = 'face'
                        child13 = etree.SubElement(child11, 'pose')
                        child13.text = 'Unspecified'
                        child14 = etree.SubElement(child11, 'truncated')
                        child14.text = '0'
                        child15 = etree.SubElement(child11, 'difficult')
                        child15.text = '0'
                        child16 = etree.SubElement(child11, 'bndbox')
                        child17 = etree.SubElement(child16, 'xmin')
                        child17.text = str((int)(x1))
                        child18 = etree.SubElement(child16, 'ymin')
                        child18.text = str((int)(y1))
                        child19 = etree.SubElement(child16, 'xmax')
                        child19.text = str((int)(x2))
                        child20 = etree.SubElement(child16, 'ymax')
                        child20.text = str((int)(y2))
                    tree = etree.ElementTree(root)
                    tree.write('/Volumes/程序/挑选类型/face1/xml/' + dk + '.xml', pretty_print=True, xml_declaration=True,
                               encoding='utf-8')
                    cv2.imwrite('/Volumes/程序/挑选类型/face1/ig/'+ig,img)
        zfile.close()








# p='/Users/jianwu/Desktop/test/Person/'
# iglist=os.listdir(p)
# tp=p+'Label/'
# for ig in iglist:
#     if ig[0]=='.' or ig=='Label':
#         continue
#     img=cv2.imread(p+ig)
#     print(ig)
#     with open(tp+ig.split('.jpg')[0]+'.txt', 'r', encoding='utf-8') as f:
#         annotations = f.readlines()
#     for an in annotations:
#         an=an.strip().split(' ')
#         boxlist=an[1:]
#         boxes = np.array(boxlist, dtype=np.float32).reshape(-1, 4)
#         for b in boxes:
#             x1=int(b[0])
#             y1 = int(b[1])
#             x2 = int(b[2])
#             y2 = int(b[3])
#             cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 4)
#     cv2.imshow('df', img)
#     cv2.waitKey(5000)













# f0=open('/Users/jianwu/Desktop/剩余.txt','a')
# with open('/Users/jianwu/Desktop/can.txt', 'r', encoding='utf-8') as f:
#     annotations = f.readlines()
# dit={}
# for an in annotations:
#     an=an.strip().split(':')
#     name=an[0]
#     boxs=an[1]
#     dit[name]=boxs
# with open('/Users/jianwu/Desktop/label.txt', 'r', encoding='utf-8') as f:
#     annotations1 = f.readlines()
# dit1={}
# for an in annotations1:
#     name=an.strip().split('款')
#     dit1[name[0]+"款"]=1
#
# def sp(s):
#     strlist = s.split('&')
#     ok1 = strlist[0].split(' ')
#     ok2 = strlist[1].split(' ')
#     str1=""
#     for s in ok1:
#         str1+=s
#     for s in ok2:
#         str1 += s
#     return  str1
#
# for d in dit.keys():
#     str1=sp(d)
#     for d1 in dit1.keys():
#         d1=d1[:-5]
#         str2=sp(d1)
#         if str1 in str2 or str2 in str1:
#             print(d,d1)







