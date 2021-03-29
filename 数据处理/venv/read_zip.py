import cv2,os,shutil
import numpy as np
import zipfile
zipfile_path = '/Users/chenchaocun/Downloads/666.zip'
save_path = '/Users/chenchaocun/Downloads/333/'
i=0
with zipfile.ZipFile(zipfile_path,mode='r') as zfile:

    for name in zfile.namelist():
        print(name)
        im_name=name.split('/')[1].split('.jpg')[0]
        print(im_name)
        if '.jpg' not in name:
            continue
        with zfile.open(name,mode='r') as image_file:
            content = image_file.read()
            image=np.asarray(bytearray(content),dtype='uint8')
            image=cv2.imdecode(image,cv2.IMREAD_COLOR)

            print(image)
            cv2.imwrite(save_path+im_name+'.jpg',image)
            #shutil.copy(image,'/Users/chenchaocun/Downloads/333/'+str(i)+'jpg')
            i+=1
            cv2.imshow('image',image)
            cv2.waitKey(1000)
    zfile.close()