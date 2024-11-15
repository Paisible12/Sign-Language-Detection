from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import numpy as np
import uvicorn
import pickle
import os

app = FastAPI()

@app.get("/")
def hello_world():
    return "Hello World"




with open("model.pickle", "rb") as f:
    model_dict = pickle.load(f)

model = model_dict["model"]

def model_pred(data_coordinates_array):
    pred = model.predict([np.asarray(data_coordinates_array)])
    return pred




class ImageJSON(BaseModel):
    dc : list

@app.post("/predict")
def predict(itemJSON:ImageJSON):
    data_coordinates_array = itemJSON.model_dump()["dc"]
    prediction = model_pred(data_coordinates_array)
    # return FileResponse(path)
    return {"Prediction" : prediction[0]}

uvicorn.run(app)