#coding=utf-8
import os,re,linecache,argparse
torch_MSE,caffe_MSE=0,0
FACE=0
eyes_L=0

def parse_args():
    '''parse args'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--pre_txt',
                        default='/Users/chenchaocun/Downloads/label.txt')
    parser.add_argument('--IOU',
                        default= 0.7)
    parser.add_argument('--gt_txt',
                        default='/Users/chenchaocun/Downloads/gt_label.txt')

    return parser.parse_args()

def cal_iou(box1, box2):
    """
    :param box1: = [xmin1, ymin1, xmax1, ymax1]
    :param box2: = [xmin2, ymin2, xmax2, ymax2]
    :return:
    """

    xmin1, ymin1, xmax1, ymax1 = float(box1[0]), float(box1[1]), float(box1[2]), float(box1[3])

    xmin2, ymin2, xmax2, ymax2 = float(box2[0]), float(box2[1]), float(box2[0])+float(box2[2]), float(box2[1])+float(box2[3])
    # 计算每个矩形的面积
    s1 = (float(xmax1) - float(xmin1)) * (float(ymax1) - float(ymin1))  # C的面积
    s2 = (float(xmax2) - float(xmin2)) * (float(ymax2) - float(ymin2))  # G的面积

    # 计算相交矩形
    xmin = max(float(xmin1), float(xmin2))
    ymin = max(float(ymin1), float(ymin2))
    xmax = min(float(xmax1), float(xmax2))
    ymax = min(float(ymax1), float(ymax2))

    w = max(0, xmax - xmin)
    h = max(0, ymax - ymin)
    area = w * h  # C∩G的面积
    iou = area / (s1 + s2 - area)
    return iou

def cal_MSE(box1, box2):#box2 为gt
    x1, y1, x2, y2,x3,y3,x4,y4,x5,y5 = float(box1[5]), float(box1[6]), float(box1[8]), float(box1[9]),float(box1[11]), float(box1[12]), float(box1[14]), float(box1[15]),float(box1[17]), float(box1[18])

    x11, y11, x12, y12,x13,y13,x14,y14,x15,y15  = float(box2[4]), float(box2[5]), float(box2[7]), float(box2[8]),float(box2[10]), float(box2[11]), float(box2[13]), float(box2[14]),float(box2[16]), float(box2[17])

    MSE=(((x11-x1)**2+(y11-y2)**2)**0.5+((x12-x2)**2+(y12-y2)**2)**0.5+((x13-x3)**2+(y13-y3)**2)**0.5+((x14-x4)**2+(y14-y4)**2)**0.5+((x15-x5)**2+(y15-y5)**2)**0.5)/(((x12-x11)**2+(y12-y11)**2)**0.5)
    eyes2eyes=(((x12 - x11) ** 2 + (y12 - y11) ** 2) ** 0.5)
    return MSE/5,eyes2eyes

def relist(p):
    with open(p, encoding='utf-8') as f:
        ans = f.readlines()
    gt_mystr = ''
    for an in ans:
        gt_mystr += an.strip() + "&"
    iglist = gt_mystr.split('# ')[1:]
    return  iglist


gt_iglist=relist('/Users/chenchaocun/Downloads/gt_label.txt')
gt_dit={}
for jpg in gt_iglist:
    jpglist=jpg.split('&')
    name=jpglist[0]
    boxlist=jpglist[1:-1]
    gt_dit[name]=boxlist

pre_caffe_iglist = relist('/Users/chenchaocun/Downloads/fddb_landmark_test_int8/retinaface_caffe_int8_1920x1080_0.4/landmark_caffe.txt')
pre_caffe_dit = {}
for jpg in pre_caffe_iglist:
   jpglist = jpg.split('&')
   name = jpglist[0]
   boxlist = jpglist[1:-1]
   pre_caffe_dit[name] = boxlist

pre_torch_iglist = relist('/Users/chenchaocun/Downloads/fddb_landmark_test_int8/retinaface_onnx_int8_960x480_0.4/landmark_onnx.txt')
pre_torch_dit = {}
for jpg in pre_torch_iglist:
    jpglist = jpg.split('&')
    name = jpglist[0]
    boxlist = jpglist[1:-1]
    pre_torch_dit[name] = boxlist


for key in gt_dit.keys():
    #print(key)
    if (key in pre_caffe_dit.keys()) and (key in pre_torch_dit.keys()):
        list1 = {}
        list2 = {}
        for i in range(len(gt_dit[key])):
            list1[i] = []
            list2[i] = []

        for caffe_box in pre_caffe_dit[key]:
            for i in range(len(gt_dit[key])):
                #print(caffe_box)
                caffebox=caffe_box.split(' ')
                gtbox=gt_dit[key][i].split(' ')

                #print(cal_iou(caffebox, gtbox))
                if cal_iou(caffebox, gtbox) > 0.7:
                    list1[i].append(caffebox)

        for torch_box in pre_torch_dit[key]:
            for i in range(len(gt_dit[key])):
                torchbox = torch_box.split(' ')
                gtbox = gt_dit[key][i].split(' ')
                if cal_iou(torchbox, gtbox) > 0.7:
                    list2[i].append(torchbox)



        for i in range(len(gt_dit[key])):
            if len(list1[i]) == 0:
                print('you no')
            if len(list2[i]) == 0:
                print('other no')

            if len(list1[i]) != 0 and len(list2[i]) != 0:

                gtbbox = gt_dit[key][i]
                gtbbox=gtbbox.split(' ')
                torchbbox = list2[i][0]
                caffebbox = list1[i][0]
                if float(gtbbox[4]) != -1.0 and (float(gtbbox[7]) != float(gtbbox[4])):
                    FACE += 1
                    a,L=cal_MSE(torchbbox,gtbbox)
                    b,_=cal_MSE(caffebbox,gtbbox)
                    torch_MSE+=a
                    caffe_MSE+=b
                    eyes_L+=L
                    print(torch_MSE,caffe_MSE)
eyes_L_mean=eyes_L/FACE
print('同时检测到到人脸总个数={}'.format(FACE))
print('pytorch 改进版本量化误差={}'.format(torch_MSE/FACE))
print('caffe_retinaface版本量化误差={}'.format(caffe_MSE/FACE))
print('pytorch非量化误差={}'.format(torch_MSE/FACE*eyes_L_mean))
print('caffe非量化误差={}'.format(caffe_MSE/FACE*eyes_L_mean))






























