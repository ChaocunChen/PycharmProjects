#coding=utf-8
from lxml import etree
import  os,shutil
import cv2
import xml.etree.ElementTree as ET

old_xmlpath = '/Users/chenchaocun/Downloads/112/'
#old_imgpath = '/Volumes/程序/openimage_faces/face1/ig/'
# new_facepath='/Volumes/生活+资料/openimage_faces/img/'
# new_xmlpath = '/Volumes/生活+资料/openimage_faces/xml/'
save_parh ='/Users/chenchaocun/Downloads/48/'
text_list=os.listdir(old_xmlpath)
#print(text_list)
incorrect =0
#print(text_list[::-1])

for an in text_list:

    if an.endswith('.xml'):

        myin_file = open(old_xmlpath + an)
        mytree = ET.parse(myin_file)
        myrootsrc = mytree.getroot()
        img = cv2.imread(old_xmlpath + an.split('.xml')[0] + '.jpg', 1)

        for W_H in myrootsrc.iter('size'):

            W = W_H.find('width').text
            H = W_H.find('height').text
        import xml.dom.minidom
        dom = xml.dom.minidom.parse(old_xmlpath + an)  # 打开XML文件
        collection = dom.documentElement  # 获取元素对象
        objectlist = collection.getElementsByTagName('object')  # 获取标签名为box的信息
        count = objectlist.length
        #print(count)
        # if count==1:
        #     shutil.move(old_xmlpath + an, save_parh + an)
        #
        #     shutil.move(old_xmlpath + an.split('.xml')[0] + '.jpg', save_parh + an.split('.xml')[0] + '.jpg')


        for obj in myrootsrc.iter('object'):



            #bb=obj.find('bndbox')
            bb = obj.find('name').text
            if bb=='person':
                try:
                    shutil.move(old_xmlpath + an, save_parh + an)

                    shutil.move(old_imgpath + an.split('.xml')[0] + '.jpg', save_parh + an.split('.xml')[0] + '.jpg')
                except:
                    continue

            # xmin= bb.find('xmin').text
            # xmax = bb.find('xmax').text
            # ymin = bb.find('ymin').text
            # ymax = bb.find('ymax').text
        #     if int(xmax)-int(xmin)>= int(W)*0.65:
        #         try:
        #             shutil.move(old_xmlpath + an, save_parh+an)
        #
        #             shutil.move(old_xmlpath + an.split('.xml')[0] + '.jpg',save_parh+an.split('.xml')[0] + '.jpg')
        #         except:
        #             continue
        #
        #         incorrect +=1

            # cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
            # cv2.imshow('face', img)
            # cv2.waitKey(1)
            #print(incorrect)
        # else:
        #     shutil.copyfile(old_xmlpath + an, new_xmlpath + an)
        #     shutil.copy(old_imgpath + an.split('.xml')[0] + '.jpg', new_facepath + an.split('.xml')[0] + '.jpg')



        # if w=='0' or h =='0':
        #     shutil.move(path+an,move_path+an)


            # cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
            # cv2.imshow('face',img)
            # cv2.waitKey(10)
# print(incorrect)