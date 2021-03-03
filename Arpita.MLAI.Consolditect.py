# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:41:46 2021

@author: cttc
"""


import os
import cv2
import numpy as np
import pickle

data_dir = os.path.join(os.getcwd(),'clean_data')

img_dir = os.path.join(os.getcwd(),'images')

def preprocess(image):
    image = cv2.resize(image,(100,100))
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return image
images = []
labels = []
for i in os.listdir(img_dir):
    image = cv2.imread( os.path.join(img_dir,i))
    image = preprocess(image)
    images.append(image)
    labels.append(i.split('_')[0])
    
image = np.array(image)
labels = np.array(labels)

with open(os.path.join(data_dir,'images.p'),'wb') as f:
    pickle.dump(images,f)

with open(os.path.join(data_dir,'labels.p'),'wb') as f:
    pickle.dump(labels,f)