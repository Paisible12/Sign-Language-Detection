import os

import cv2 as cv
import mediapipe as mp
import pickle
import numpy as np


data = []
labels = []

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)


f = open("model.pickle", "rb")
model_dict = pickle.load(f)
model = model_dict["model"]
f.close()

def model_pred(image):
    
    # print(type(image))
    image = cv.imread(image)
    # print(image.shape)
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    
    output = hands.process(image_rgb)
    data_coordinates = []
    if output.multi_hand_landmarks:
        for hand_landmarks in output.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
            
        for hand_landmarks in output.multi_hand_landmarks:
                for i in hand_landmarks.landmark:
                    x = i.x
                    y = i.y
                    data_coordinates.append(x)
                    data_coordinates.append(y)
        
        pred = model.predict([np.asarray(data_coordinates)])
        # cv.imshow("Video", image)
        # k = cv.waitKey(10000)
        # if k == ord("q"):
        #     cv.destroyWindow("Video")
        # cv.destroyAllWindows()
        return pred

def pred(file):
    prediction = model_pred(file)
    return prediction

print(pred("./images/3.jpg"))

# image = Image.open("./data/0/1.jpg").convert("RGB")
# print(model_pred())