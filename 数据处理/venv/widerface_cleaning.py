import os ,cv2
txt_path = "/Users/chenchaocun/Downloads/wider_val.txt"



#save_path = "./wider_yolov5_val/"
#os.makedirs(save_path)


# f2 = open(txt_path, "r")
#
# # lines = f.readlines() + f2.readlines()
# lines = f2.readlines()
#
# isFirst = True
# labels = []
# words = []
# imgs_path = []
# for line in lines:
#     line = line.rstrip()
#     if line.startswith('#'):
#         if isFirst is True:
#             isFirst = False
#         else:
#             labels_copy = labels.copy()
#             words.append(labels_copy)
#             labels.clear()
#         path = line[1:].strip()
#         print(path)
#         # path = txt_path.replace('label.txt','images/') + path
#         path = os.path.join(txt_path.replace(txt_path.split("/")[-1], "images"), path)
#     else:
#
#         imgs_path.append(path)
#         #print(imgs_path)
#         #print(line)
#
# f3 = open(txt_path, "w")
# for line in lines:
#
#     if line.rstrip().startswith('#'):
#         f3.write(line)
#     else:
#         if float(line.split(' ')[0]) <= 0 or float(line.split(' ')[1]) <= 0 or float(line.split(' ')[2]) <= 10 or float(line.split(' ')[3]) <= 10:
#             continue
#         f3.write(line)

f4=open(txt_path,'r')
f5 = open("/Users/chenchaocun/Downloads/wider_val1.txt",'a')
lines = f4.readlines()

allface=""
prstr=""
for line in lines:
    line=line.strip()
    if prstr=="":
        prstr=line
    else:
        if '#' in line and '#' in prstr:
            prstr=line
            continue
        else:
            f5.write(prstr)
            f5.write('\n')
            prstr = line
if not '#' in prstr:
    f5.write(prstr)
    f5.write('\n')
f5.close()
