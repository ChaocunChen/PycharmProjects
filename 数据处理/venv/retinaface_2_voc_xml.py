import os
import cv2
from lxml import etree
import xml.etree.ElementTree as ET
txt_path = "/Volumes/程序/人脸扩增/label_wider_clean_20X20.txt"
save_path = "/Users/chenchaocun/Downloads/1212/"
#os.makedirs(save_path)


f2 = open(txt_path, "r")
# lines = f.readlines() + f2.readlines()
lines = f2.readlines()
isFirst = True
labels = []
words = []
imgs_path = []
for line in lines:
    line = line.rstrip()
    if line.startswith('#'):
        if isFirst is True:
            isFirst = False
        else:
            labels_copy = labels.copy()
            words.append(labels_copy)
            labels.clear()
        path = line[1:].strip()
        # path = txt_path.replace('label.txt','images/') + path
        path = os.path.join(txt_path.replace(txt_path.split("/")[-1], "images"), path)

        imgs_path.append(path)
    else:
        line = line.split(' ')
        label = [float(x) for x in line]
        labels.append(label)

words.append(labels)
print(words)
image_count = 0
#root = etree.Element("annotation")

for path,word in zip(imgs_path,words):
    img = cv2.imread(path)
    img_height = img.shape[0]
    img_width = img.shape[1]
    rel_bbox_list = []
    landmark = []
    xml_name=((path.split('/')[-1]).split('.jpg')[0])
    print(xml_name)
    print(word)

    root = etree.Element("annotation")
    child1 = etree.SubElement(root, "folder")
    child1.text = "JPEGImages"
    child2 = etree.SubElement(root, "filename")
    child2.text = path
    child3 = etree.SubElement(root, "path")
    child3.text = "JPEGImages/" + path
    child4 = etree.SubElement(root, "source")
    child5 = etree.SubElement(child4, 'database')
    child5.text = 'Unknown'
    child6 = etree.SubElement(root, 'size')
    child7 = etree.SubElement(child6, 'width')
    child7.text = str(img_width)
    child8 = etree.SubElement(child6, 'height')
    child8.text = str(img_height)
    child9 = etree.SubElement(child6, 'depth')
    child9.text = str(3)
    child10 = etree.SubElement(root, 'segmented')
    child10.text = '0'



    for anno in word:

        # for zu in [[4,5],[7,8],[10,11],[13,14],[16,17]]:
        #     if anno[zu[0]] == -1:
        #         landmark.append("-1")
        #         landmark.append("-1")
        #     else:
        #         landmark.append(str(float(anno[zu[0]] * 1.0  / img_width)))
        #         landmark.append(str(float(anno[zu[1]] * 1.0  / img_height)))

        x1, y1, w, h = anno[:4]
        # cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)
        x2 = x1+w
        y2= y1+h

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
    tree.write('/Users/chenchaocun/Downloads/images/'+xml_name + '.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')