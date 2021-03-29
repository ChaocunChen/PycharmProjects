#coding=utf-8
import requests
from aip import AipFace
import cv2,base64,os,shutil

import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=y4hEzcUTDTcG0Q97BvZLMRLN&client_secret=bZK0igVGcOYsuRmq3j4xh97fvpkEIdjb'
response = requests.get(host)
if response:
    print(response.json())
    c=1



# """ 你的 APPID AK SK """
APP_ID = '03297e991dbf4b979234bb7e9fdd683c'
API_KEY = '082e9a5d8f154dd1aa2e701aff790665'
SECRET_KEY = '2f1f815288664a859df1e6ec8b2bafb8'
dit_face={}


def image_to_base64(image_np):
    image = cv2.imencode('.jpg', image_np)[1]
    image_code = str(base64.b64encode(image))[2:-1]
    return image_code


client = AipFace(APP_ID, API_KEY, SECRET_KEY)
imageType = "BASE64"

""" 如果有可选参数 """
options = {}
options["face_field"] = "age"
options["max_face_num"] = 2
options["face_type"] = "LIVE"
options["liveness_control"] = "LOW"


imgpath= '/Users/chenchaocun/Downloads/test/'
for img in os.listdir(imgpath):


    im=cv2.imread(imgpath+img)


    try:
        image = image_to_base64(im)
        """ 调用人脸检测 """
        client.detect(image, imageType)



        """ 带参数调用人脸检测 """
        result_dict=client.detect(image, imageType, options)


        Age = result_dict['result']['face_list']
    except:
        continue
    print(Age[0]['location']['left'])
    xmin= int(Age[0]['location']['left'])
    ymin=int(Age[0]['location']['top'])
    xmax=int(Age[0]['location']['left']) +int(Age[0]['location']['width'])
    ymax=int(Age[0]['location']['top']) + int(Age[0]['location']['height'])
    cv2.rectangle(im,(xmin,ymin),(xmax,ymax),(0,0,255),thickness=2)
    cv2.putText(im, str(Age[0]['age']), (xmin, ymin), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    #cv2.rectangle(im,(float(Age[0]['location']['left']),float(Age[0]['location']['top'])),(float(Age[0]['location']['left'])+float(Age[0]['location']['width']),float(Age[0]['location']['top'])+float(Age[0]['location']['height'])),(0,0,255))
    cv2.imshow('美女',im)
    cv2.waitKey(1)

    # if Age >0 and Age <=5:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/0-5/')
    # elif Age >5 and Age<=10:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/5-10/')
    # elif Age >10 and Age <=15:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/10-15/')
    # elif Age >15 and Age<=20:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/15-20/')
    # elif Age >20 and Age<=25:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/20-25/')
    # elif Age >25 and Age<=30:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/25-30/')
    #
    # elif Age >30 and Age<=35:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/30-35/')
    # elif Age >35 and Age<=40:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/35-40/')
    # elif Age >40 and Age<=45:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/40-45/')
    # elif Age >45 and Age<=50:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/45-50/')
    # elif Age >50 and Age<=55:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/50-55/')
    # elif Age >55 and Age<=60:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/55-60/')
    # elif Age >60 and Age<=65:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/60-65/')
    # elif Age >65 and Age<=70:
    #     shutil.copy(imgpath+img,'/Users/chenchaocun/Downloads/65-70/')
    # else:
    #     shutil.copy(imgpath + img, '/Users/chenchaocun/Downloads/70+/')

    #print('Age={}'.format(result_dict['result']['face_list'][0]['age']))
    print(Age)

