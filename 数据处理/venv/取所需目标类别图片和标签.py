import os,csv,json,shutil,cv2
import zipfile
import numpy as np
from lxml import etree
from xml.dom.minidom import parseString
XMin,XMax,YMin,YMax=[],[],[],[]

zipfile_path = '/Volumes/学习/openimageV2/train_01.zip'
save_path = '/Users/chenchaocun/Downloads/openimage_face/'
with zipfile.ZipFile(zipfile_path, mode='r') as zfile:
    for name in zfile.namelist():
        print(name)
        im_name = name.split('/')[1].split('.jpg')[0]
        print(im_name)
        if '.jpg' not in name:
            continue
        with zfile.open(name, mode='r') as image_file:
            content = image_file.read()
            image = np.asarray(bytearray(content), dtype='uint8')
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

            print(image)
            if image is not None:
                cv2.imwrite(save_path + im_name + '.jpg', image)
            # shutil.copy(image,'/Users/chenchaocun/Downloads/333/'+str(i)+'jpg')

            cv2.imshow('image', image)
            cv2.waitKey(1000)
    zfile.close()
# def read_zip():
#
#
#     with zipfile.ZipFile(zipfile_path, mode='r') as zfile:
#
#         for name in zfile.namelist():
#             print(name)
#             im_name = name.split('/')[1].split('.jpg')[0]
#             print(im_name)
#             if '.jpg' not in name:
#                 continue
#             with zfile.open(name, mode='r') as image_file:
#                 content = image_file.read()
#                 image = np.asarray(bytearray(content), dtype='uint8')
#                 image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#
#                 print(image)
#                 cv2.imwrite(save_path + im_name + '.jpg', image)
#                 # shutil.copy(image,'/Users/chenchaocun/Downloads/333/'+str(i)+'jpg')
#
#                 #cv2.imshow('image', image)
#                 #cv2.waitKey(1000)
#         zfile.close()


count =0
with open('/Users/chenchaocun/Downloads/test-annotations-human-imagelabels.csv') as f:
    csv.reader(f)

    for line in csv.reader(f):
        #print(line)
        if line[2] == '/m/01th42':
            count+=1
            ImagID =line[0]
            print(ImagID)
            #iglist=os.listdir('/Users/chenchaocun/Downloads/test')
            iglist=os.listdir(save_path)
            name=ImagID+'.jpg'

            if name in iglist:
                print(ImagID)
            for img in iglist:
                if name==img:
                    shutil.copy('/Users/chenchaocun/Downloads/test/'+img,'/Users/chenchaocun/Downloads/666/'+img)


                    with open('/Users/chenchaocun/Downloads/test-annotations-bbox.csv') as f1:
                        for lines in csv.reader(f1):

                            print(lines)
                            #if len(lines)==0:
                            if lines[2] == '/m/01th42':  # '/m/0dzct'
                                Img_name = lines[0]
                                print(Img_name)
                                print(lines[4],lines[5],lines[6],lines[7])
                                image = cv2.imread('/Users/chenchaocun/Downloads/test/' + Img_name + '.jpg')
                                h, w, c = image.shape
                                #XMin.append(lines[4])
                                # XMin.append(float(lines[4])), XMax.append(
                                #     lines[5]), YMin.append(lines[6]), YMax.append(lines[7])
                                # print(XMin,XMax,YMin,YMax)
                                ok=1
                                root = etree.Element("annotation")
                                child1 = etree.SubElement(root, "folder")
                                child1.text = "JPEGImages"
                                child2 = etree.SubElement(root, "filename")
                                child2.text = Img_name + ".jpg"
                                child3 = etree.SubElement(root, "path")
                                child3.text = "JPEGImages/" + Img_name + ".jpg"
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

                                notpts = ""
                                haspts = ""
                                x1 = float(lines[4])
                                y1 = float(lines[6])
                                x2 = float(lines[5])
                                y2 = float(lines[7])
                                xmin = int(x1*w)
                                ymin = int(y1*h)
                                xmax = int(x2*w)
                                ymax = int(y2*h)
                                # 生成xml
                                child11 = etree.SubElement(root, 'object')
                                child12 = etree.SubElement(child11, 'name')
                                child12.text = 'Face'
                                child13 = etree.SubElement(child11, 'pose')
                                child13.text = 'Unspecified'
                                child14 = etree.SubElement(child11, 'truncated')
                                child14.text = '0'
                                child15 = etree.SubElement(child11, 'difficult')
                                child15.text = '0'
                                child16 = etree.SubElement(child11, 'bndbox')
                                child17 = etree.SubElement(child16, 'xmin')
                                child17.text = str((int)(xmin))
                                child18 = etree.SubElement(child16, 'ymin')
                                child18.text = str((int)(ymin))
                                child19 = etree.SubElement(child16, 'xmax')
                                child19.text = str((int)(xmax))
                                child20 = etree.SubElement(child16, 'ymax')
                                child20.text = str((int)(ymax))
                                tree = etree.ElementTree(root)
                                tree.write('/Users/chenchaocun/Downloads/666/' +Img_name + '.xml', pretty_print=True,xml_declaration=True,encoding='utf-8')


                            else:
                                continue
    print(count)
                # else:
                #     break
                #





# with open('/Users/chenchaocun/Downloads/test-annotations-bbox.csv') as f1:
#     for lines in csv.reader(f1):
#
#         print(lines)
#         if lines[2] == '/m/07j7r':#'/m/0dzct'
#                 Img_name =lines[0]
#                 print(Img_name)
#                 print(lines[4])
#                 XMin,XMax,YMin,YMax=XMin.insert(i,float(lines[4])),XMax.append(lines[5]),YMin.append(lines[6]),YMax.append(lines[7])
#
#                 print(XMin)
#                 for img in os.listdir('/Users/chenchaocun/Downloads/test'):
#                     print(img.split('.')[0])

