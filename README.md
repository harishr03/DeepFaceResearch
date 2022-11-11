# DeepFaceResearch
# Mission: 
Using an open source facial recognition model, Build an application that helps people with visual impairments
recognize facial attribution and gestures on online conference platforms. 

# Process
This project uses a open source facial recognition model called "DeepFace". This model allows us recognize faces and conduct a Facial Attribute Analysis. 
We chose this model because this model becaue it offers many useful features for our case such as 'Real Time Analysis', 'Face Detectors' and more. We are going to be using this model to analyze the users face and give them live feedback about thier current camera positioniong as well as facial expressions and gestures through an audible tone. 

# Main Code
```
live = DeepFace.stream(***picture***)

obj = DeepFace.analyze(img_path = "live",
actions = ['age', 'race', 'emotion])
print(obj)
```


