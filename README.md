# DeepFaceResearch
# Mission: 
Using an open source facial recognition model, Build an application that helps people with visual impairments
recognize facial attribution and gestures on online conference platforms. 

# Process:
This project uses a open source facial recognition model called "DeepFace". This model allows us recognize faces and conduct a Facial Attribute Analysis. 
We chose this model because this model becaue it offers many useful features for our case such as 'Real Time Analysis', 'Face Detectors' and more. We are going to be using this model to analyze the users face and give them live feedback about thier current camera positioniong as well as facial expressions and gestures through an audible tone. 

# Main Code:
```
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
```
The above lines of code are for accessing the front facing camera, analyzing the image captured through the camera and detecting actions such as age, race and emotion captured. 

