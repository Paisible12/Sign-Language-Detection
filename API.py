from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import numpy as np
import uvicorn
from Inference_On_Picture import pred
import os
from pydantic import BaseModel

app = FastAPI()


def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.get("/")
def hello_world():
    return "Hello World"

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not os.path.exists("./images"):
        os.makedirs("./images")
    image = await file.read()
    with open("./images/0.jpg", "wb") as f:
        f.write(image)
    return {"filename":file.filename}

@app.get("/predict")
async def predict():
    path = "./images/0.jpg"
    prediction = pred(path)
    # return FileResponse(path)
    return {"Prediction" : prediction[0]}
            
    
    
    
    # contents = await file.read()
    # img = cv.imdecode(nparr, cv.IMREAD_COLOR)

    # img_dimensions = str(img.shape)

    # # line that fixed it
    # _, encoded_img = cv.imencode('.PNG', img)

    # encoded_img = base64.b64encode(encoded_img)
    # imgdata = base64.b64decode(encoded_img)
    
    # image = Image.open(BytesIO(imgdata)).show()

    # return{
    #     'filename': file.filename,
    #     'dimensions': img_dimensions,
    #     'encoded_img': imgdata,
    # }
    
    
    
    
    # np_array = np.reshape(np_array, (480, 640, 3))
    
    # cv.imshow("Hello World", image)
    # print(type(image))
    
    # image = np.array(image)
    
    # image_array = cv.imread(image)
    # print(image_array)
    # print(something(image))

uvicorn.run(app)