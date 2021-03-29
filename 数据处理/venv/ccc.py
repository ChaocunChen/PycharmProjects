import numpy as np
import cv2
import os
import json
from lxml import etree
import  os
import cv2
import xml.etree.ElementTree as ET
xp='/Users/chenchaocun/Downloads/xml/'
igp='/Users/chenchaocun/Downloads/ig/'

wigp='/Users/chenchaocun/Downloads/4s1/'
wxp='/Users/chenchaocun/Downloads/4s1/'
num=1
xlist=os.listdir(xp)
for x in xlist:
    if x[0]=='.':
        continue
    igname=x.split('.xml')[0] + '.jpg'
    wname=igname
    num+=1
    img=cv2.imread(igp+igname)
    h,w,c=img.shape
    root = etree.Element("annotation")
    child1 = etree.SubElement(root, "folder")
    child1.text = "JPEGImages"
    child2 = etree.SubElement(root, "filename")
    child2.text = wname+'.jpg'
    child3 = etree.SubElement(root, "path")
    child3.text = "JPEGImages/" + wname+'.jpg'
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

    myin_file = open(xp + x)
    mytree = ET.parse(myin_file)
    myrootsrc = mytree.getroot()

        lb=obj.find('name').text
        if lb=='Plate':
            continue
        xmlbox = obj.find('bndbox')
        # 生成xml
        child11 = etree.SubElement(root, 'object')
        child12 = etree.SubElement(child11, 'name')
        child12.text = 'Can'
        child13 = etree.SubElement(child11, 'pose')
        child13.text = 'Unspecified'
        child14 = etree.SubElement(child11, 'truncated')
        child14.text = '0'
        child15 = etree.SubElement(child11, 'difficult')
        child15.text = '0'
        child16 = etree.SubElement(child11, 'bndbox')
        child17 = etree.SubElement(child16, 'xmin')
        child17.text =  xmlbox.find('xmin').text
        child18 = etree.SubElement(child16, 'ymin')
        child18.text = xmlbox.find('ymin').text
        child19 = etree.SubElement(child16, 'xmax')
        child19.text = xmlbox.find('xmax').text
        child20 = etree.SubElement(child16, 'ymax')
        child20.text = xmlbox.find('ymax').text
        # 存储xml
    tree = etree.ElementTree(root)
    tree.write(wxp + wname + '.xml', pretty_print=True, xml_declaration=True,
               encoding='utf-8')
    cv2.imwrite(wigp+wname+'.jpg',img)