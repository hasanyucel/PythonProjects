import cv2

cap = cv2.VideoCapture('test.mp4')
ret, frame = cap.read()
ret, frame1 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame,frame1)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur,50,255,0)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 600:
            continue
        cv2.rectangle(frame,(x,y),(x+y,w+h),(0,255,0),2)
        cv2.putText(frame,"status {}".format("movement"),(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    
    cv2.imshow('inter',frame)
    frame = frame1
    ret,frame1 = cap.read()

    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()