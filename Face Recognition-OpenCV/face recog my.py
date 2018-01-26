# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:11:22 2017

@author: Deby
"""
# Face Recognition
#Importing the libraries
import cv2

#loading the cascades
face_cascades= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascades= cv2.CascadeClassifier('haarcascade_eye.xml')

# Defining the function that will do the detections
def detect (gray, frame):
    faces = face_cascades.detectMultiScale(gray, 1.3, 5)# here 1.3 is scaling size of original image and 5 is number of neighboring zones input
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x.y),(x+w,y+h),(255,0,0), 2)
        #creating zones within the face referential rectangle, zone 1=grayscale, zone 2=orig image
        roi_gray = gray [y:y+h,x:x+w]
        roi_color = frame [y:y+h, x:x+w]
        #eye detection by applying cascades to zone 1 gray image
        eyes = eye_cascades.detectMultiScale(roi_gray, 1.1, 3)
        for(ex,ey,ew,eh)in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ex,ey+eh),(0,255,0),2)
    return frame

# Doing the face recognition using the webcam
video_capture = cv2.VideoCapture(0)
while True:
    _,frame = video_capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv2.imshow ('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
    
