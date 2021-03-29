import os ,cv2
#face_Dir='/home/chenchaocun/Glint360k/output/'
face_Dir='/Users/chenchaocun/Downloads/1122/'
face_path = os.listdir(face_Dir)

f= open('/Users/chenchaocun/Downloads/glint360k.txt', 'w+')
for name in face_path:
    for jpg in os.listdir(face_Dir+name):
        print(face_Dir+name+'/'+jpg)
        line_txt= name+'/'+jpg +' '+ name.split('_')[1]+'\n'

        f.write(line_txt)
f.close()


