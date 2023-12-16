# -*- coding: utf-8 -*-
"""Step2_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tcAdbxsm34P4FuGTTwEB4ERD6U6GNHTx
"""

!pip install ultralytics
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow
from ultralytics import YOLO
import ultralytics

from google.colab import drive
drive.mount('/content/drive')

model = YOLO('yolov8n.pt')
data_path = '/content/drive/MyDrive/Colab Notebooks/Project 3 Data/data/data.yaml'
output = model.train(data =data_path,epochs=130,imgsz=1100,batch=2,name='Project3_YOLO_model_AER850')