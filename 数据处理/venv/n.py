import numpy as np
import cv2
import os
import json
from lxml import etree
import  os
import cv2
import xml.etree.ElementTree as ET

def getiou(box,boxlist):
    riou=-1
    for b in boxlist:
        arae1=(box[2]-box[0])*(box[3]-box[1])
        arae2=(b[2]-b[0])*(b[3]-b[1])
        minx=max(b[0],box[0])
        miny=max(b[1],box[1])
        maxx=min(b[2],box[2])
        maxy=min(b[3],box[3])
        w=(maxx-minx)
        if w<0:
            w=0
        h=(maxy-miny)
        if h<0:
            h=0
        iouarae=w*h
        IOU=iouarae/(arae1+arae2-iouarae)
        if IOU>riou:
            riou=IOU
    return riou


xp='/Volumes/生活+资料/20200820新增数据/'
wxp='/Volumes/生活+资料/xml/'
xlist=os.listdir(xp)
num=1
for x in xlist:
    if x[0]=='.':
        continue
    if '.jpg' in x:
        continue
    wname=x.split('.xml')[0]
    num+=1

    # ------------------------新建xml
    root = etree.Element("annotation")
    child1 = etree.SubElement(root, "folder")
    child1.text = "JPEGImages"
    child2 = etree.SubElement(root, "filename")
    child2.text = wname + ".jpg"
    child3 = etree.SubElement(root, "path")
    child3.text = "JPEGImages/" + wname + ".jpg"
    child4 = etree.SubElement(root, "source")
    child5 = etree.SubElement(child4, 'database')
    child5.text = 'Unknown'
    child6 = etree.SubElement(root, 'size')

    child9 = etree.SubElement(child6, 'depth')
    child9.text = str(3)
    child10 = etree.SubElement(root, 'segmented')
    child10.text = '0'
    #----------------------------
    print(xp+x)
    myin_file = open(xp+ x)
    mytree = ET.parse(myin_file)
    myrootsrc = mytree.getroot()



    boxs = []
    for obj in myrootsrc.iter('object'):
        box=[]
        xmlbox = obj.find('bndbox')
        box.append(int(xmlbox.find('xmin').text))
        box.append(int(xmlbox.find('ymin').text))
        box.append(int(xmlbox.find('xmax').text))
        box.append(int(xmlbox.find('ymax').text))
        boxs.append(box)

    tmpboxlist=[]
    for box in boxs:
        iou=0
        if len(tmpboxlist)==0:
            tmpboxlist.append(box)
        else:
            iou=getiou(box,tmpboxlist)
            print(iou)
        if iou>0.66:
            continue
        else:
            tmpboxlist.append(box)
        # 生成xml
        child11 = etree.SubElement(root, 'object')
        child12 = etree.SubElement(child11, 'name')
        child12.text = 'car'
        child13 = etree.SubElement(child11, 'pose')
        child13.text = 'Unspecified'
        child14 = etree.SubElement(child11, 'truncated')
        child14.text = '0'
        child15 = etree.SubElement(child11, 'difficult')
        child15.text = '0'
        child16 = etree.SubElement(child11, 'bndbox')
        child17 = etree.SubElement(child16, 'xmin')
        child17.text = str(box[0])
        child18 = etree.SubElement(child16, 'ymin')
        child18.text = str(box[1])
        child19 = etree.SubElement(child16, 'xmax')
        child19.text = str(box[2])
        child20 = etree.SubElement(child16, 'ymax')
        child20.text = str(box[3])

    for obj in myrootsrc.iter('size'):
        w = obj.find('width').text
        h = obj.find('height').text
    child7 = etree.SubElement(child6, 'width')
    child7.text =w
    child8 = etree.SubElement(child6, 'height')
    child8.text =h
    # 存储xml
    tree = etree.ElementTree(root)
    tree.write(wxp + wname + '.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')