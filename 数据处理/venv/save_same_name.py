# #-*- coding: UTF-8 -*-
#
# #语言：Python
# #功能：将文件名相同，后缀名不同的文件保持在same文件夹下
# #使用：代码放在图片和xml文件中，运行
# import os, shutil
# #img_path = '/Volumes/程序/openimage_faces/face1/ig'
# #xml_path = '/Volumes/程序/openimage_faces/face1/xml'
#
# img_path = '/Volumes/生活+资料/vehicle_new_all/'
# #xml_path = '/Volumes/生活+资料/yolov5_Vehicle_detection/'
# xml_path = '/Volumes/生活+资料/vehicle_new_all/'
#
# save_path = '/Volumes/生活+资料/ccc'
# jpg_list = [x.split('.')[0] for x in os.listdir(img_path) if x.endswith('.jpg')]
# xml_list = [x.split('.')[0] for x in os.listdir(xml_path) if x.endswith('.xml')]
# a = [x for x in jpg_list if x in xml_list]
# b= [x for x in xml_list if x in jpg_list]
# print(len(a),len(b))
#
# print(a,b)
#
# goal_path = save_path
# if not os.path.exists(goal_path):
#     os.mkdir(goal_path)
#
# for num, i in enumerate(a):
#     if i =='':
#         continue
#     jpg_file = i + '.jpg'
#     jpg_path = os.path.join(img_path, jpg_file)
#     despath = os.path.join(goal_path, jpg_file)
#     print(jpg_path)
#     shutil.move(jpg_path, despath)
# for cc, ccc in enumerate(b):
#     if ccc =='':
#         continue
#     xml_file = ccc + '.xml'
#     xmlfile_path = os.path.join(xml_path, xml_file)
#     despath = os.path.join(goal_path, xml_file)
#     print(xmlfile_path)
#     shutil.move(xmlfile_path, despath)



# import os,shutil
# img_path='/Users/chenchaocun/Downloads/lvdi_result1/'
# resut_path='/Users/chenchaocun/Downloads/lvdi_result/'
# save_path = '/Users/chenchaocun/Downloads/121/'
# jpg_list = [x.strip() for x in os.listdir(img_path) if x.endswith('.jpg')]
# print(jpg_list)
# resut_list= [x.strip() for x in os.listdir(resut_path) if x.endswith('.jpg')]
# print(resut_path)
# a = [x for x in jpg_list if x  in resut_list]
#
#
#
# for jpg_name in a:
#     print(jpg_name)
#     shutil.copy(img_path+jpg_name,save_path+jpg_name)




# import os
# i=1
# f3=open('/Users/chenchaocun/Downloads/openimages_lvdi.txt','r')
# lines = f3.readlines()
# for line in lines:
#     if '#' in line:
#         i+=1
# print(i)


# #删掉图片不存在的标签
# import os
# txt_path = "/Users/chenchaocun/Downloads/label_openimages_20_8_0.99_all.txt"
# jpg_list=os.listdir('/Users/chenchaocun/Downloads/openimgaes_partial/')
# f3=open('/Users/chenchaocun/Downloads/label_openimages_20_8_0.99_partial_1218.txt','w')
# #txt_path = "/home/chenchaocun/Pytorch_Retinaface-master/label_openimages.txt"
# f2 = open(txt_path, "r")
#
# # lines = f.readlines() + f2.readlines()
# lines = f2.readlines()
#
# isFirst = True
# labels = []
# words = []
# imgs_path = []
# flag=0
# for line in lines:
#    line = line.rstrip()
#    #if line.startswith('#'):
#    if '#' in line and line.split('/')[-1] in jpg_list:
#        f3.write(line)
#        f3.write('\n')
#        flag = 1
#    elif '#' in line and not line.split('/')[-1] in jpg_list:
#        flag=0
#    elif flag==1:
#        f3.write(line)
#        f3.write('\n')
#
# f3.close()



# # #找出标签存在的图片
# import os,shutil
# txt_path = "/Users/chenchaocun/Downloads/label_lvdi_1216_done.txt"
# jpg_list=os.listdir('/Users/chenchaocun/Downloads/lvdi_result/')
# f2=open(txt_path,'r')
# lines = f2.readlines()
# img_name=[]
# for line in lines:
#    line = line.rstrip()
#    #if line.startswith('#'):
#    if '#' in line:
#        img_name.append(line.split('/')[-1])
# a=[x for x in jpg_list if x not in img_name]
# print(a)
# for jpg in a:
#     shutil.move('/Users/chenchaocun/Downloads/lvdi_result/'+jpg,'/Users/chenchaocun/Downloads/laji/'+jpg)


#去掉# jpg 后面不代标签的行

# txt_path = "/home/chenchaocun/Pytorch_Retinaface-master/data/widerface/train/label_openimages_20_8_0.99.txt"
# f4=open(txt_path,'r')
# f5 = open("/home/chenchaocun/Pytorch_Retinaface-master/data/widerface/train/label_openimages_20_8_0.99_1029_done.txt",'a')
# lines = f4.readlines()
# i=1
# allface=""
# prstr=""
# for line in lines:
#     line=line.strip()
#     if prstr=="":
#         prstr=line
#     else:
#         if '#' in line and '#' in prstr:
#             prstr=line
#             print(prstr)
#             continue
#
#         else:
#             f5.write(prstr)
#             f5.write('\n')
#             prstr = line
# if not '#' in prstr:
#     f5.write(prstr)
#     f5.write('\n')
# f5.close()


import os
i=0
f3=open('/Users/chenchaocun/Downloads/label_lvdi_1214_done_bedone.txt','r')
lines = f3.readlines()
for line in lines:
    if '#' in line:
        i+=1
print(i)