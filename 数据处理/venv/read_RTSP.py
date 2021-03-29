import cv2

cap = cv2.VideoCapture('/Users/chenchaocun/Downloads/output.avi')
#cap = cv2.VideoCapture("rtsp://192.168.144.101:554/user=admin&password=123456&channel=1&stream=0.sdp?")
#cap = cv2.VideoCapture("rtsp://192.168.144.103:554/user=admin&password=123456&channel=1&stream=0.sdp?")#走廊
#cap = cv2.VideoCapture("rtsp://admin:hk123456@192.168.22.167:554/h264/ch1/main/av_stream")
ret,frame = cap.read()
while ret:
    ret,frame = cap.read()
    print(frame.shape)
    cv2.imshow("frame",frame)
    #cv2.imwrite()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()