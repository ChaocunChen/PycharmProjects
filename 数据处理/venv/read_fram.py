#coding=utf-8

import cv2,os
#Video = '/Users/chenchaocun/Desktop/car.h264'

cap=cv2.VideoCapture(1)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
#fps = 25 #保存视频的帧率
size = (1920,1080) #保存视频的大小
flag =0
cc =0
videoWriter =cv2.VideoWriter('/Users/chenchaocun/Desktop/Head.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),15,size)


while True:

    ret,frame=cap.read()
    flag+=1
    cc+=1

    if ret==True:
        videoWriter.write(frame)

        # cv2.imshow('ccc',frame)
        # cv2.waitKey(1)

        # if flag ==5:
        # #     videoWriter.write(frame)
        #     cv2.imwrite('/Users/chenchaocun/Desktop/ccc/' + str(cc) + 'fuck.jpg', frame)
        #     flag =0
    else:
        videoWriter.write(frame)
        print('end')
        break


    #        cv2.imwrite('/Volumes/生活+资料/CLA/'+str(i)+'_CLA.jpg',frame)
    #        i+=1
    #        flag=0
    # else:
    #     break
cap.release()
videoWriter.release()