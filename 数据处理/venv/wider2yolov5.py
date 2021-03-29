import os ,cv2
txt_path = "/home/chenchaocun/Pytorch_Retinaface-master/data/widerface/val/label.txt"
save_path = "./wider_yolov5_val/"
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
        print(path)
        # path = txt_path.replace('label.txt','images/') + path
        path = os.path.join(txt_path.replace(txt_path.split("/")[-1], "images"), path)

        imgs_path.append(path)
        #print(imgs_path)
    else:
        line = line.split(' ')
        #print(line)
        label = [float(x) for x in line]
        labels.append(label)

words.append(labels)
image_count = 0

flag=0
for path,word in zip(imgs_path,words):
    if flag==1:
      break
    img = cv2.imread(path)
    img_height = img.shape[0]
    img_width = img.shape[1]
    rel_bbox_list = []

    for anno in word:

        landmark =  []
        xmin, ymin, w, h = anno[:4]
        if xmin <= 0 or ymin <= 0 or w <= 10 or h <= 10:
            continue

        xmax = xmin + w

        ymax = ymin + h
        x_center = (float(xmax) + float(xmin)) / 2 - 1
        y_center = (float(ymax) + float(ymin)) / 2 - 1

        x_center_ = x_center / float(img_width)
        y_center_ = y_center / float(img_height)
        w_ = (int(xmax) - int(xmin)) / (float(img_width))
        h_ = (int(ymax) - int(ymin)) / (float(img_height))
        '''if w_ >1:
            w_=1
        if h_ >1:
            h_=1'''
        if x_center_ >= 1 or y_center_ >= 1 or w_ >= 1 or h_ >= 1 or x_center_ < 0 or y_center_ < 0 or w_ < 0 or h_ < 0:
            print(path, xmin, ymin, w, h, img_width, img_height)
            flag = 1
            break
        w_ = str(w_)
        h_ = str(h_)

        writ_txt = '0' + ' ' + str(x_center_) + ' ' + str(y_center_) + ' ' + w_ + ' ' + h_
        rel_bbox_list.append(writ_txt)
    image_count += 1
    # print(image_count)

    save_image_name = "wider_" + str(image_count)

    cv2.imwrite(save_path + save_image_name + ".jpg", img)
    with open(save_path + save_image_name + ".txt", "w") as f:
        for i in rel_bbox_list:
            f.write(i + "\n")

# import os ,cv2
# txt_path = "/Users/chenchaocun/Downloads/label_wider.txt"
# save_path = "/Users/chenchaocun/Downloads/1212/"
# #os.makedirs(save_path)
#
#
# f2 = open(txt_path, "r")
#
# # lines = f.readlines() + f2.readlines()
# lines = f2.readlines()
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
#
#         imgs_path.append(path)
#         print(imgs_path)
#     else:
#         line = line.split(' ')
#         label = [float(x) for x in line]
#         labels.append(label)
#
# words.append(labels)
# print(words)
# image_count = 0
# for path,word in zip(imgs_path,words):
#     img = cv2.imread(path)
#     img_height = img.shape[0]
#     img_width = img.shape[1]
#     rel_bbox_list = []
#
#     # for anno in word:
#     #
#     #     landmark =  []
#     #     for zu in [[4,5],[7,8],[10,11],[13,14],[16,17]]:
#     #         if anno[zu[0]] == -1:
#     #             landmark.append("-1")
#     #             landmark.append("-1")
#     #         else:
#     #             landmark.append(str(float(anno[zu[0]] * 1.0  / img_width)))
#     #             landmark.append(str(float(anno[zu[1]] * 1.0  / img_height)))
#
#         # for i in range(5):
#         #     x1,y1,w,h = landmark[2*i],landmark[2*i+1],0.001,0.001
#         #     if x1 == -1 or y1 == -1 :
#         #         continue
#         #
#         #     if x1 <= 0 or x1 >= img_width:
#         #         continue
#         #     if y1 <= 0 or y1 >= img_height:
#         #         continue
#         #
#         #
#         #     rel_cx = str(float(x1 * 1.0  / img_width))
#         #     rel_cy = str(float(y1 * 1.0  / img_height))
#         #     rel_w = str(float(w / img_width))
#         #     rel_h = str(float(h / img_height))
#         #
#         #
#         #     string_bbox = str(i+1) +  " " + rel_cx + " " + rel_cy + " " + rel_w + " " + rel_h
#         #     rel_bbox_list.append(string_bbox)
#
#
#         xmin, ymin, w, h = anno[:4]
#
#         xmax = xmin+w
#
#         ymax = ymin+h
#         x_center = (float(xmax) + float(xmin)) / 2
#         y_center = (float(ymax) + float(ymin)) / 2
#
#
#         x_center_ = x_center / float(img_width)
#         y_center_ = y_center / float(img_height)
#         w_ = str((int(xmax) - int(xmin)) / (float(img_width)))
#         h_ = str((int(ymax) - int(ymin)) / (float(img_height)))
#         writ_txt = '0' + ' ' + str(x_center_) + ' ' + str(y_center_) + ' ' + w_ + ' ' + h_ + '\n'
#
# # if label_name=='sleep':
#         # cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)
#         # rel_cx = str(float((x1 + int(w/2)) / img_width))
#         # rel_cy = str(float((y1 + int(h/2)) / img_height))
#         # rel_w = str(float(w / img_width))
#         # rel_h = str(float(h / img_height))
#
#         #string_bbox = "0 " + rel_cx + " " + rel_cy + " " + rel_w + " " + rel_h + " " + " ".join(landmark)
#         rel_bbox_list.append(writ_txt)
#     image_count += 1
#     print(image_count)
#
#     save_image_name = "wider_" + str(image_count)
#
#     cv2.imwrite( save_path + save_image_name + ".jpg", img)
#     with open(save_path + save_image_name + ".txt", "w") as f:
#         for i in rel_bbox_list:
#             f.write(i + "\n")