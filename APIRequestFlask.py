import mediapipe as mp
import cv2 as cv
import json
import requests

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)

data_coordinates = []
def model_pred(image_path):
    image = cv.imread(image_path)
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    
    output = hands.process(image_rgb)
    data_coordinates = []
    if output.multi_hand_landmarks:
        for hand_landmarks in output.multi_hand_landmarks:
                for i in hand_landmarks.landmark:
                    x = i.x
                    y = i.y
                    data_coordinates.append(x)
                    data_coordinates.append(y)
        return data_coordinates

# url = "http://127.0.0.1:5000/predict"
url = "https://sign-language-hosting-production.up.railway.app/predict"
path = "./images/5.jpg"
data_coordinates = model_pred(path)

data_to_send = {
    "dc" : data_coordinates
}
input_json = json.dumps(data_to_send)
response = requests.post(url, json=input_json)
print(json.loads(response.text)["Prediction"])