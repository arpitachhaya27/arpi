# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:08:37 2021

@author: cttc
"""


import cv2
import urllib
import numpy as np

URL = "http://10.37.49.117:8080/shot.jpg"
face_data = "haarcascade_frontalface_default.xml"
classifiar = cv2.CascadeClassifier(face_data)

data=[]
ret = True

while ret:
    img_url = urllib.request.urlopen(URL)
    image = np.array(bytearray(img_url.read()),np.uint8)
    frame =cv2.imdecode(image,-1)
    
    faces = classifiar.detectMultiScale(frame,1.5,5)
    if faces is not None:
        for x,w,y,h in faces:
            
            
            face_image = frame[y:y+h,x:x+w]
            face_image = frame[y:y+h,x:x+w].copy()
            
            
            if len(data)<=100:
                data.append(face_image)
            else:
                cv2.putText(frame,'comlete',(200,200),
                            cv2.FONT_HERSHEY_COMPLEX,1,
                            (255,0,0),2)
    
    cv2.imshow('capture',frame)
    if cv2.waitKey(30)==ord('q'):
            break
        
        
cv2.destroyAllWindows()

name = input("enter name : ")
c = 0
for i in data:
    cv2.imwrite("image/"+name+'_'+str(c)+'.jpg',i)
    
    c=c+1
    
