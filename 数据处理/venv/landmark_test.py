import os,re,linecache,argparse
MSE, MSE_X, MSE_y = 0, 0, 0
FACE=0
eyes2eyes=0
def cal_iou(box1, box2):
    """
    :param box1: = [xmin1, ymin1, xmax1, ymax1]
    :param box2: = [xmin2, ymin2, xmax2, ymax2]
    :return:
    """

    xmin1, ymin1, xmax1, ymax1 = box1[0], box1[1], box1[2], box1[3]

    xmin2, ymin2, xmax2, ymax2 = box2[0], box2[1], box2[2], box2[3]
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

def parse_args():
    '''parse args'''
    parser = argparse.ArgumentParser()
    # parser.add_argument('--gpu_id', type=int, default=0, help='gpu id')
    parser.add_argument('--pre_txt',
                        default='/Users/chenchaocun/Downloads/fddb_landmark_test/caffe_1920x1080_0.4/landmark_caffe.txt')
    parser.add_argument('--IOU',
                        default= 0.5)
    parser.add_argument('--pre_torch_txt',
                        default='/Users/chenchaocun/Downloads/fddb_landmark_test/onnx_960x480_0.4/landmark_onnx.txt')
    parser.add_argument('--gt_txt',
                        default='/Users/chenchaocun/Downloads/gt_label.txt')

    return parser.parse_args()

args = parse_args()
pre_txt = open(args.pre_txt, 'r+')
gt_txt = open(args.gt_txt, 'r+')
pre_torch_txt=open(args.pre_torch_txt,'r+')

pre_land,pre_torch_land,gt_land =[],[],[]
gt_mystr = ""
dict1={}
dict2={}




for gt_line in gt_txt.readlines():
    gt_mystr += gt_line.strip() + "&"

gt_iglist = gt_mystr.split('# ')[1:]

for gt_ig in gt_iglist:

    gt_plist = gt_ig.split('&')
    #print(pre_plist)

    #print(len(pre_plist))
    # bl = len(pre_plist) -2  # 人脸个数
    # face_count += bl
    name = gt_plist[0]    #pre_plist is one jpg all face

    pre_mystr = ""
    for pre_line in pre_txt.readlines():

        pre_mystr += pre_line.strip() + "&"
        #print(gt_mystr)

        pre_iglist = pre_mystr.split('# ')[1:]



    for pre_ig in pre_iglist:
        pre_plist = pre_ig.split('&')
        #print(gt_plist)

        #print(len(gt_plist))

        if gt_plist[0] == pre_plist[0]:
            gt_land,pre_land=gt_plist[1:-1],pre_plist[1:-1]
            bbox1,bbox2=[],[]
            gt_landmark, gt_bbox,pre_landmark, pre_bbox = [],[],[],[]
            for i in range(len(gt_land)):
                gt_landmark.append(gt_land[j].split(' ')[4])
                gt_landmark.append(gt_land[j].split(' ')[5])
                gt_landmark.append(gt_land[j].split(' ')[7])
                gt_landmark.append(gt_land[j].split(' ')[8])
                gt_landmark.append(gt_land[j].split(' ')[10])
                gt_landmark.append(gt_land[j].split(' ')[11])
                gt_landmark.append(gt_land[j].split(' ')[13])
                gt_landmark.append(gt_land[j].split(' ')[14])
                gt_landmark.append(gt_land[j].split(' ')[16])
                gt_landmark.append(gt_land[j].split(' ')[17])

                gt_bbox.append(gt_land[j].split(' ')[0])
                gt_bbox.append(gt_land[j].split(' ')[1])
                gt_bbox.append(float(gt_land[j].split(' ')[0]) + float(gt_land[j].split(' ')[2]))
                gt_bbox.append(float(gt_land[j].split(' ')[1]) + float(gt_land[j].split(' ')[3]))

                #print(pre_bbox)
                #pre_bbox.append(float(pre_land[i].split(' ')[0]) + float(pre_land[i].split(' ')[2]))
                #pre_bbox.append(float(pre_land[i].split(' ')[1]) + float(pre_land[i].split(' ')[3]))
                for j in range(len(pre_land)):
                    pre_landmark.append(pre_land[i].split(' ')[5])
                    pre_landmark.append(pre_land[i].split(' ')[6])
                    pre_landmark.append(pre_land[i].split(' ')[8])
                    pre_landmark.append(pre_land[i].split(' ')[9])
                    pre_landmark.append(pre_land[i].split(' ')[11])
                    pre_landmark.append(pre_land[i].split(' ')[12])
                    pre_landmark.append(pre_land[i].split(' ')[14])
                    pre_landmark.append(pre_land[i].split(' ')[15])
                    pre_landmark.append(pre_land[i].split(' ')[17])
                    pre_landmark.append(pre_land[i].split(' ')[18])

                    pre_bbox.append(pre_land[i].split(' ')[0])
                    pre_bbox.append(pre_land[i].split(' ')[1])
                    pre_bbox.append(float(pre_land[i].split(' ')[2]))
                    pre_bbox.append(float(pre_land[i].split(' ')[3]))





                    IOU = cal_iou(gt_bbox, pre_bbox)

                    if IOU>=args.IOU and float(gt_landmark[0])!= float(gt_landmark[2]) and float(gt_landmark[1])!= float(gt_landmark[3]):     #iou >0.7
                        FACE+=1
                        print('pre_landmark={}'.format(pre_landmark))
                        print('gt_landmark={}'.format(gt_landmark))


                        eyes2eyes+=((((float(gt_landmark[2]) - float(gt_landmark[0])) ** 2 + (
                                float(gt_landmark[3]) - float(gt_landmark[1])) ** 2)) ** 0.5)
                        print(eyes2eyes)

                        MSE += (((((float(pre_landmark[0]) - float(gt_landmark[0])) ** 2) + (
                                    (float(pre_landmark[1]) - float(gt_landmark[1])) ** 2)) ** 0.5 + (
                                            ((float(pre_landmark[2]) - float(gt_landmark[2])) ** 2) + (
                                                (float(pre_landmark[3]) - float(gt_landmark[3])) ** 2)) ** 0.5 + (
                                            ((float(pre_landmark[4]) - float(gt_landmark[4])) ** 2) + (
                                                (float(pre_landmark[5]) - float(gt_landmark[5])) ** 2)) ** 0.5 + (
                                            ((float(pre_landmark[6]) - float(gt_landmark[6])) ** 2) + (
                                                (float(pre_landmark[7]) - float(gt_landmark[7])) ** 2)) ** 0.5 + (
                                            ((float(pre_landmark[8]) - float(gt_landmark[8])) ** 2) + (
                                                (float(pre_landmark[9]) - float(gt_landmark[9])) ** 2)) ** 0.5) / (((
                                    (float(gt_landmark[2]) - float(gt_landmark[0])) ** 2 + (
                                        float(gt_landmark[3]) - float(gt_landmark[1])) ** 2)) ** 0.5))
                        print(FACE)


                        print(MSE)

                    gt_bbox.clear()
                    gt_landmark.clear()


                pre_bbox.clear()
                pre_landmark.clear()

    '''pre_torch_mystr = ""
    for pre_torch_line in pre_torch_txt.readlines():

        pre_torch_mystr += pre_torch_line.strip() + "&"
        #print(gt_mystr)

        pre_torch_iglist = pre_torch_mystr.split('# ')[1:]



    for pre_torch_ig in pre_torch_iglist:
        pre_torch_plist = pre_torch_ig.split('&')
        #print(gt_plist)

        #print(len(gt_plist))

        if gt_plist[0] == pre_torch_plist[0]:
            gt_land,pre_torch_land=gt_plist[1:-1],pre_torch_plist[1:-1]
            bbox1,bbox2=[],[]
            gt_landmark, gt_bbox,pre_torch_landmark, pre_torch_bbox = [],[],[],[]
            for i in range(len(gt_land)):
                gt_landmark.append(gt_land[j].split(' ')[4])
                gt_landmark.append(gt_land[j].split(' ')[5])
                gt_landmark.append(gt_land[j].split(' ')[7])
                gt_landmark.append(gt_land[j].split(' ')[8])
                gt_landmark.append(gt_land[j].split(' ')[10])
                gt_landmark.append(gt_land[j].split(' ')[11])
                gt_landmark.append(gt_land[j].split(' ')[13])
                gt_landmark.append(gt_land[j].split(' ')[14])
                gt_landmark.append(gt_land[j].split(' ')[16])
                gt_landmark.append(gt_land[j].split(' ')[17])

                gt_bbox.append(gt_land[j].split(' ')[0])
                gt_bbox.append(gt_land[j].split(' ')[1])
                gt_bbox.append(float(gt_land[j].split(' ')[0]) + float(gt_land[j].split(' ')[2]))
                gt_bbox.append(float(gt_land[j].split(' ')[1]) + float(gt_land[j].split(' ')[3]))
                
                #print(pre_torch_bbox)
                #pre_torch_bbox.append(float(pre_torch_land[i].split(' ')[0]) + float(pre_torch_land[i].split(' ')[2]))
                #pre_torch_bbox.append(float(pre_torch_land[i].split(' ')[1]) + float(pre_torch_land[i].split(' ')[3]))
                for j in range(len(pre_torch_land)):
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[5])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[6])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[8])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[9])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[11])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[12])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[14])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[15])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[17])
                    pre_torch_landmark.append(pre_torch_land[i].split(' ')[18])

                    pre_torch_bbox.append(pre_torch_land[i].split(' ')[0])
                    pre_torch_bbox.append(pre_torch_land[i].split(' ')[1])
                    pre_torch_bbox.append(float(pre_torch_land[i].split(' ')[2]))
                    pre_torch_bbox.append(float(pre_torch_land[i].split(' ')[3]))
                    



                    
                    IOU = cal_iou(gt_bbox, pre_torch_bbox)

                    if IOU>=args.IOU and float(gt_landmark[0])!= float(gt_landmark[2]) and float(gt_landmark[1])!= float(gt_landmark[3]):     #iou >0.7
                        FACE+=1
                        print('pre_torch_landmark={}'.format(pre_torch_landmark))
                        print('gt_landmark={}'.format(gt_landmark))


                        eyes2eyes+=((((float(gt_landmark[2]) - float(gt_landmark[0])) ** 2 + (
                                float(gt_landmark[3]) - float(gt_landmark[1])) ** 2)) ** 0.5)
                        print(eyes2eyes)

                        MSE += (((((float(pre_torch_landmark[0]) - float(gt_landmark[0])) ** 2) + (
                                    (float(pre_torch_landmark[1]) - float(gt_landmark[1])) ** 2)) ** 0.5 + (
                                            ((float(pre_torch_landmark[2]) - float(gt_landmark[2])) ** 2) + (
                                                (float(pre_torch_landmark[3]) - float(gt_landmark[3])) ** 2)) ** 0.5 + (
                                            ((float(pre_torch_landmark[4]) - float(gt_landmark[4])) ** 2) + (
                                                (float(pre_torch_landmark[5]) - float(gt_landmark[5])) ** 2)) ** 0.5 + (
                                            ((float(pre_torch_landmark[6]) - float(gt_landmark[6])) ** 2) + (
                                                (float(pre_torch_landmark[7]) - float(gt_landmark[7])) ** 2)) ** 0.5 + (
                                            ((float(pre_torch_landmark[8]) - float(gt_landmark[8])) ** 2) + (
                                                (float(pre_torch_landmark[9]) - float(gt_landmark[9])) ** 2)) ** 0.5) / (((
                                    (float(gt_landmark[2]) - float(gt_landmark[0])) ** 2 + (
                                        float(gt_landmark[3]) - float(gt_landmark[1])) ** 2)) ** 0.5))
                        print(FACE)


                        print(MSE)'''


eyes2eyes=eyes2eyes/FACE
MSE=MSE/5
MSE_mean=MSE/FACE
MSE_mean_pix=MSE_mean*eyes2eyes
print('MSE_all={}'.format(MSE_mean*FACE))
print('FACE_count={}'.format(FACE))
print('MSE_mean={}'.format(MSE_mean))
print('eyes2eyes={}'.format(eyes2eyes))
print(MSE_mean_pix)

