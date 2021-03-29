import os
import cv2
import numpy as np


# self.img = cv2.imread(self.line[0])
# self.landmark = np.asarray(self.line[1:197], dtype=np.float32)
# self.attribute = np.asarray(self.line[197:203], dtype=np.int32)
# self.euler_angle = np.asarray(self.line[203:206], dtype=np.float32)

def groberect(points, ww, hh):
    x1 = points[0]
    y1 = points[1]
    x2 = points[2]
    y2 = points[3]

    w = x2 - x1 + 1
    h = y2 - y1 + 1
    px = float(x1 + x2) / 2
    py = float(y1 + y2) / 2

    w = w * 1.2
    h = h * 1.2

    l = max(0, px - w / 2)
    r = min(ww - 1, px + w / 2)
    t = max(0, py - h / 2)
    b = min(hh - 1, py + h / 2)

    # x1 y1 x2 y2
    return [int(l), int(t), int(r), int(b)]


file_ynh = open("/Users/chenchaocun/Downloads/WFLW_annotations/list_98pt_rect_attr_train_test/list_98pt_rect_attr_train.txt", 'r')
lines = file_ynh.readlines()
count = len(lines)
num = 1
for line in lines:
    print(num, "/", count)
    num += 1
    line = line.strip().split()
    landmark = line[0:196]
    detection = line[196:200]
    attributes = line[200:206]
    name = line[206:207]
    img = cv2.imread("/Users/chenchaocun/Downloads/WFLW_images/" + str(name[0]))
    if img is None:
        exit()
        continue
    h, w = img.shape[0:2]

    cv2.rectangle(img, (int(detection[0]),int(detection[1])), (int(detection[2]),int(detection[3])), (0, 255, 0), 2, 8)
    for index in range(0, len(landmark), 2):
        cv2.circle(img, (int(float(landmark[index])), int(float(landmark[index+1]))), 1, (255, 0, 0), -1)
    cv2.imshow("img.jpg", img)
    cv2.waitKey(500)

#     landmark = list(map(float, landmark))
#     new_landmark = []
#     for index in range(0, len(landmark), 2):
#         new_landmark.append([landmark[index], landmark[index + 1]])
#
#     landmark_array = np.asarray(new_landmark)
#     xmax, ymax = landmark_array.max(axis=0)
#     xmin, ymin = landmark_array.min(axis=0)
#     # 坐标中有负数，为了crop，应该判断
#     xmin = xmin if xmin > 0 else 0
#     ymin = ymin if ymin > 0 else 0
#     xmax = xmax if xmax < w - 1 else w - 1
#     ymax = ymax if ymax < h - 1 else h - 1
#
#     detection = list(map(int, detection))
#     new_detection = []
#     new_detection.append(detection[0] if detection[0] < int(xmin + 0.5) else int(xmin + 0.5))
#     new_detection.append(detection[1] if detection[1] < int(ymin + 0.5) else int(ymin + 0.5))
#     new_detection.append(detection[2] if detection[2] > int(xmax + 0.5) else int(xmax + 0.5))
#     new_detection.append(detection[3] if detection[3] > int(ymax + 0.5) else int(ymax + 0.5))
#     # new_detection = [detection[x] if detection[x] > landList[x] else landList[x] for x in range(len(detection))]
#
#     rect = groberect(new_detection, w, h)
#     rectimg = img[rect[1]:rect[3], rect[0]:rect[2], :]
#
#     for index in range(0, len(landmark), 2):
#         x, y = landmark[index], landmark[index + 1]
#         x = x if x > 0 else 0
#         y = y if y > 0 else 0
#         x = x if x < w - 1 else w - 1
#         y = y if y < h - 1 else h - 1
#
#         if ((x - rect[0]) < 0 or (y - rect[1]) < 0):
#             print("特征点超出扩展框，应该改变策略，使用特征点和原始框的最小外接矩形做扩展框")
#             print(x - rect[0], "\n")
#             print(y - rect[1], "\n")
#
#         cv2.circle(img, (int(x - rect[0]), int(y - rect[1])), 1, (255, 0, 0), -1)
#     #cv2.imwrite("./result/" + "img_%s.jpg" % (str(num)), rectimg)
#     cv2.imshow("rectimg.jpg", img)
#     cv2.waitKey(500)
#
# file_ynh.close()