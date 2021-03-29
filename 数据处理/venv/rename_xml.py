import os,shutil
#imagepath='/Users/chenchaocun/Downloads/TTT/'
# for img in os.listdir(imagepath):
#     if img.endswith('.jpg'):
#         name=img.split('.jpg')[0]
#         shutil.copy(imagepath+'ccc.xml',imagepath+name+'.xml')


# imagepath='/Users/chenchaocun/Downloads/CCC/'
# save_path = '/Users/chenchaocun/Downloads/4s/'
# for img in os.listdir(imagepath):
#     if img.endswith('.jpg.xml'):
#         name=img.split('.jpg.xml')[0]
#         shutil.move(imagepath+img,save_path+name+'.xml')
#     elif img.endswith('.jpg.jpg'):
#         name = img.split('.jpg.jpg')[0]
#         shutil.move(imagepath + img, save_path + name + '.jpg')

imagepath='/Users/chenchaocun/Downloads/CLA/'
save_path = '/Users/chenchaocun/Downloads/123/'
for img in os.listdir(imagepath):
    for i in range(6540,6545):


        name= imagepath+'6540_CLA_ccc.xml'
        if not os.path.exists(imagepath+str(i)+'_CLA.jpg'):
            continue
        shutil.copy(name,imagepath+str(i)+'_CLA.xml')

        name_img = imagepath+str(i)+'_CLA.jpg'

        print(str(i))

        #shutil.copy(name_img, save_path + str(i)+'_CLA.jpg')
