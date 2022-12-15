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
In this project we used the OpenCV Python Library for our facial recognition model. The code displayed above is the the code for the main function of our program . This code is a While loop that loops as long as it gets a signal and detects a face on the camera. 

The code check if the camera detects a face using the OpenCV function '.read()' this function detect the face. Once the face is detected we switch to grayscale for an accurate reading of the facial recognition model. We then create a variable 'coordinate_list' that holds the coordinates of the position the face is detected in. 

We have a for loop that takes the x,y,w,h as parameters and as long as these are within the coordinates_list, this loop is going to try to rectangulate the frame of x,y,w,h parameters in the color green. We can display this live using the 'imshow()' function. 

Finally, we have a downloaded .wav file that contains the ligth beep audion that plays once the face is not detected within our parameter. We can shut down our fucntion by pressing the 'x'.

#Conclusion:
This program could be used by individuals with visual impairments as tool to help them center themselves on the front facing camera to make sure they are visible on the screen while in an online Conference setting. 


