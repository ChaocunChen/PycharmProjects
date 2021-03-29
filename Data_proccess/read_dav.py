#coding=utf-8
import cv2,os

mp4_list=os.listdir('/Volumes/录像拷贝/20201024-1')
for mp4 in mp4_list:
    print(mp4.split('.mp4')[0])
    if mp4.split('_')[0] == 'ch05' or mp4.split('_')[ 0] == 'ch06':
    #if mp4.split('_')[0] == 'ch03' or mp4.split('_')[0] == 'ch04' or mp4.split('_')[0] == 'ch05' or mp4.split('_')[0] == 'ch06':
        print(mp4)
        cap = cv2.VideoCapture('/Volumes/录像拷贝/20201024-1/'+mp4)
#cap=cv2.VideoCapture('/Volumes/录像拷贝/20201025-1/ch06_20201025133031.mp4')
        fps = cap.get(cv2.CAP_PROP_FPS)
        print(fps)
# fps = 25 #保存视频的帧率
# size = (1920,1080) #保存视频的大小
# videoWriter =cv2.VideoWriter('/Users/chenchaocun/Desktop/c/vehicle3.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),fps,size)
# cap.set(3,1920) #设置分辨率
# cap.set(4,1080)
#cap=cv2.VideoCapture('/Users/chenchaocun/Desktop/20200819.mov')
        i =0
        flag =0
        cc=0
        while(cap.isOpened()):
            ret,frame=cap.read()
            flag+=1
            cc+=1


            if ret==True:

        # frame = cv2.transpose(frame)
        # frame = cv2.flip(frame, 1)
        #frame[:100, :] = (0, 0, 0)
        #frame = frame[600:, :]
        #frame[:250, :] = (0, 0, 0)
        #frame[:800, :] = (128, 128, 128)
        #frame[0:150, 1860:] = (0, 0, 0)
        # frame[0:160, 1405:] = (0, 0, 0)
        # frame[0:200, 1605:] = (0, 0, 0)
        # frame[0:150, 0:100] = (0, 0, 0)

        # if cc < 2000:
        #     frame=frame[600:, :]
        # if cc > 2001:
        #     frame = frame[900:, :]


        # if cc < 200:
        #     frame[:135, :] = (0, 0, 0)
        #     frame[0:180, 1125:] = (0, 0, 0)
        #     frame[0:220, 1212:] = (0, 0, 0)
        #     frame[0:291, 1307:] = (0, 0, 0)
        #     frame[0:329, 1411:] = (0, 0, 0)
        #     frame[0:427, 1527:] = (0, 0, 0)
        #     frame[0:434, 1543:] = (0, 0, 0)
        #     frame[0:544, 1778:] = (0, 0, 0)
        # if cc >201:
        #
        #     frame[:135, :] = (0, 0, 0)
        #     frame[0:180, 1200:] = (0, 0, 0)
        #     frame[0:220, 1300:] = (0, 0, 0)
        #     frame[0:291, 1400:] = (0, 0, 0)
        #     frame[0:329, 1510:] = (0, 0, 0)
        #     frame[0:427, 1620:] = (0, 0, 0)
        #     frame[0:434, 1655:] = (0, 0, 0)
        #     frame[0:544, 1860:] = (0, 0, 0)





                if flag==25:
                    print('/Volumes/程序/绿地商圈图片1/'+mp4.split('.mp4')[0]+'_'+str(i)+'.jpg')
                    cv2.imwrite('/Volumes/程序/绿地商圈图片1/'+mp4.split('.mp4')[0]+'_'+str(i)+'.jpg',frame)

                    i+=1
                    print(i)
                    flag=0

                cv2.imshow('dav',frame)

                cv2.waitKey(1)
            else:
                break

        cap.release()
