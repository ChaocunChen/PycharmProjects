from lxml import etree
import  os,shutil
import cv2
import xml.etree.ElementTree as ET

path = '/Users/chenchaocun/Downloads/CLA_CCC/'
move_path = '/Users/chenchaocun/Downloads/2333/'
text_list=os.listdir(path)
#print(text_list)


for an in text_list:
    #print(an)
    if an.endswith('.xml'):

        myin_file = open(path + an)
        mytree = ET.parse(myin_file)
        myrootsrc = mytree.getroot()
        for obj in myrootsrc.iter('size'):
            w = obj.find('width').text
            h = obj.find('height').text
            if w=='0' or h =='0':
                print(an)
                #shutil.move(path+an,move_path+an)