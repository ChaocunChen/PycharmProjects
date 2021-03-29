import os
import json


label_txt = open('/Users/chenchaocun/Downloads/label.txt','a+')



landlist=[]
bboxlist=[]
landdict={}
bboxdict={}


for root_dir,dir,json_filename in os.walk('/Users/chenchaocun/Downloads/json'):

    for json_file in json_filename:

        print(json_file)
        file_name= json_file.split('.')[0]
        print(file_name)

        with open('/Users/chenchaocun/Downloads/json/'+json_file) as f:
            pop_data = json.load(f)


            print(pop_data)
            label_landmarks=pop_data['shapes']

            print(label_landmarks)
            bboxlist.clear()
            landlist.clear()
            for i in range(len(label_landmarks)):
                if label_landmarks[i]['label']=='bbox':
                    bboxlist.append(label_landmarks[i]['points'])
                elif label_landmarks[i]['label']=='landmark':
                    landlist.append(label_landmarks[i]['points'])

            label_txt.write('# ' + str(file_name) +'.jpg'+'\n')
            temp=' '
            print(len(landlist))
            for j in range(len(landlist)):
                # print(file_name,"dfddfdd")
                temp = str(int(bboxlist[j][0][0])) + ' ' + str(int(bboxlist[j][0][1])) + ' ' + str(int(bboxlist[j][1][0])) + ' ' + str(
                    int(bboxlist[j][1][1])) + ' ' + str(int(landlist[j][0][0])) + ' ' + str(int(landlist[j][0][1])) + ' ' + str(
                    int(landlist[j][1][0])) + ' ' + str(int(landlist[j][1][1])) + ' ' + str(int(landlist[j][2][0])) + ' ' + str(
                    int(landlist[j][2][1])) + ' ' + str(int(landlist[j][3][0])) + ' ' + str(
                    int(landlist[j][3][1])) + ' ' + str(int(landlist[j][4][0])) + ' ' + str(
                    int(landlist[j][4][1])) +'\n'
                #temp =str(bboxlist[j][0][0])+' '+str(bboxlist[j][0][1])+' '+str(bboxlist[j][1][0])+' '+str(bboxlist[j][1][1])+' '+str(landlist[j][0][0])+' '+str(landlist[j][0][1])+' 0.0 '+str(landlist[j][1][0])+' '+str(landlist[j][1][1])+' 0.0 '+str(landlist[j][2][0])+' '+str(landlist[j][2][1])+' 0.0 '+str(landlist[j][3][0])+' '+str(landlist[j][3][1])+' 0.0 '+str(landlist[j][4][0])+' '+str(landlist[j][4][1])+ ' 0.0 '+'0.8'+'\n'
                label_txt.write(temp)
            #label_txt.write('\n')
            # label_txt.writelines('# '+str(file_name)+'.jpg'+'\n'+temp+'\n')

            #temp=''
            #label_txt.write(str(file_name)+'.jpg'+'\n'+temp+'\n')


            # for label_landmark in label_landmarks:
            #     landmark_points = label_landmark['points']
            #
            #     landlist.append()
            #
            #     print(landmark_points)
            #     print(len(landmark_points))
            #     if len(landmark_points)==2:
            #         xmin = landmark_points[0][0]
            #         ymin = landmark_points[0][1]
            #         xmax = landmark_points[1][0]
            #         ymax= landmark_points[1][1]
            #     else:
            #         left_eye=landmark_points[0]
            #         right_eye=landmark_points[1]
            #         nose = landmark_points[2]
            #         left_mouth_corner = landmark_points[3]
            #         right_mouth_corner = landmark_points[4]



            #temp = str(xmin) + ' ' + str(ymin)+' 0.0 '+str(xmax) + ' ' + str(ymax)+' 0.0 '+str(left_eye[0]) + ' ' + str(left_eye[1])+' 0.0 '+str(right_eye[0]) + ' ' + str(right_eye[1])+' 0.0 '+str(nose[0]) + ' ' + str(nose[1])+' 0.0 '+str(left_mouth_corner[0]) + ' ' + str(left_eye[1])+' 0.0 '+str(right_mouth_corner[0]) + ' ' + str(right_mouth_corner[1])+' 0.0 '+'0.8'
            #print(temp)
            #label_txt.write(temp + '\n')
        #label_txt.close()


