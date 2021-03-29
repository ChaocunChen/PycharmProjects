import os,re,linecache
content_list = []
count =0

file = open('/Users/chenchaocun/Downloads/retinaface_gt_v1/val/label.txt')
#file.readlines()
file1=open('/Users/chenchaocun/Downloads/wider_val.txt','w+')
mystr=""
for line in file.readlines():
    print(line)
    mystr+=line.strip() + "&"
iglist=mystr.split('# ')
print(iglist)
for ig in iglist:
    plist=ig.split('&')
    name=plist[0]
    bl=len(plist)-2
    write_name = str(name)+'\n'
    file1.write(write_name)


    # for boxs in plist[1:-2]:
    #     box=boxs.split(' ')
    #     xmin,ymin,xmax,ymax= box[0],box[1],int(box[2])+int(box[0]),int(box[3])+int(box[1])



