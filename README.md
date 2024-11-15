We need to create image data using Create_Image_Dataset.py

It will ask for folder name

Each folder will contain the images

Its good if there are 20+ images per folder in data folder

(For example, ./data/A will have the images.png stored)

Run Create_Dataset.py to create a pickle file with hand landmarks stored

This will create data.pickle

Run Train.py to train the model using the created dataset in pickle file

This will create model.pickle

Run Inference.py to get inference based on the trained model (model.pickle)
