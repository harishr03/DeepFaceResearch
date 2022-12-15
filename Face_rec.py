import cv2 as cv
from playsound import playsound
from PIL import Image, ImageDraw

capture = cv.VideoCapture(0)

pretrained_model = cv.CascadeClassifier("face_detector.xml")

while True:
    bool, frame = capture.read()
    if bool == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        for(x,y,w,h) in coordinate_list:
            cv.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 2)

        cv.imshow("Live Face Detection", frame)

        #if frame != coordinate_list:
           # playsound('Beep Sound Effect.wav')

        if cv.waitKey(20) == ord('x'):
            break
    
capture.release()
cv.destroyAllWindows()