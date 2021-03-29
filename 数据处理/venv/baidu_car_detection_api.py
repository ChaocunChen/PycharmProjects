import requests

import base64

import numpy as np
import cv2
import os
import json
from lxml import etree
import  os
import cv2
import xml.etree.ElementTree as ET
import  time
'''
车辆检测
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
access_token = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vGoPnY9aaFFthhWiqQmN5gtk&client_secret=EQNX4YYrDTyZ6Hxw8vautKwRGbExNIg4'
res=requests.get(access_token)
if res:
    ok = res.json()
access_token = ok['access_token']
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
jpg_dir='/Volumes/生活+资料/20200820新增数据/'
num=1
ccc=0
xp='/Volumes/生活+资料/xml/'
for jpg in os.listdir(jpg_dir):
    ccc+=1

    print(ccc)
    jpg_name=jpg.split('.')[0]
    im = cv2.imread(jpg_dir + jpg)
    if im is None:
        continue
    # print(jpg_name)

    f = open(jpg_dir+jpg, 'rb')



    img = base64.b64encode(f.read())


    wname=jpg_name
    num+=1



    h,w,c=im.shape
    #print(h,w)


    params = {"image": img}
    response = requests.post(request_url, data=params, headers=headers)



    # try:
    #     response = requests.post(request_url, data=params, headers=headers)
    # except Exception:
    #     response = requests.post(request_url, data=params, headers=headers)



    root = etree.Element("annotation")
    child1 = etree.SubElement(root, "folder")
    child1.text = "JPEGImages"
    child2 = etree.SubElement(root, "filename")
    child2.text = jpg
    child3 = etree.SubElement(root, "path")
    child3.text = "JPEGImages/" + jpg
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


    if response:
        allmsg=response.json()
        #print (allmsg)
        try:
            #print(len(response.json()['vehicle_info']))
            for msg in allmsg['vehicle_info']:
                if msg["type"]=="carplate" or  msg["type"]=="motorbike" or msg["type"]=="tricycle":
                    continue
                x1 = int(msg['location']['left'])
                x2 = int(float(msg['location']['left']) + float(
                    msg['location']['width']))  # left is xmin ,top is ymin

                y1 = int(msg['location']['top'])
                y2 = int(float(msg['location']['top']) + float(
                    msg['location']['height']))
                # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
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
                child17.text = str((int)(x1))
                child18 = etree.SubElement(child16, 'ymin')
                child18.text = str((int)(y1))
                child19 = etree.SubElement(child16, 'xmax')
                child19.text = str((int)(x2))
                child20 = etree.SubElement(child16, 'ymax')
                child20.text = str((int)(y2))
            tree = etree.ElementTree(root)
            tree.write(xp + jpg_name + '.xml', pretty_print=True, xml_declaration=True,
                       encoding='utf-8')
        except:
            continue




                #print(response.json()['vehicle_info'][i])
                #print(response.json()['vehicle_info'][i]['location']['top'])





