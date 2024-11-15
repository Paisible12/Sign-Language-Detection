import os

import cv2 as cv
import mediapipe as mp
import matplotlib.pyplot as plt
import pickle
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.5)

DIR = "./data"


data = []
labels = []
g=0
for foldername in os.listdir(DIR):
    for images in os.listdir(os.path.join(DIR, foldername)):
        data_coordinates = []
        img = cv.imread(os.path.join(DIR, foldername, images))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        
        res = hands.process(img)
        
        if res.multi_hand_landmarks:
            for hand_landmarks in res.multi_hand_landmarks:
                for i in hand_landmarks.landmark:
                    x = i.x
                    y = i.y
                    data_coordinates.append(x)
                    data_coordinates.append(y)
            data.append(data_coordinates)
            labels.append(foldername)

f = open("data.pickle", "wb")
print(len(data))
pickle.dump({"data" : data, "labels" : labels}, f)
f.close()