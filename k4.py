import cv2

vidcap = cv2.VideoCapture(0)
vidcap.set(cv2.CAP_PROP_POS_MSEC,20000)     # just cue to 20 sec. position
success,image = vidcap.read()
if success:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY )
    cv2.imwrite("fram20sec1.jpg", im_bw)     # save frame as JPEG file
    cv2.imshow("20sec",gray)
    cv2.waitKey()                    

