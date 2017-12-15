import numpy as np
from alexnet import alexnet
import cv2
import time
import cv2
import pyscreenshot as ImageGrab
import numpy as np
import os
WIDTH = 160
HEIGHT = 160
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'WhiteNet-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.09

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)
def grab():
    test=list(np.load('.npy'))
    test=test[0]
    return np.array(test)

def test_model():
    i=0
    test = list(np.load('testData.npy'))
    for data in test:
        i=i+1
        print(data[1])
        data=data[0]
        np.array(data)
        #data=cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
        data=cv2.resize(data, (160, 160))
        # 800x600 windowed mode
        cv2.imshow('Test',data)
        screen=np.array(data)
        # screen =  np.array(ImageGr
        # ab.grab(bbox=(0,40,800,640))
        print(data[1])
        prediction = model.predict([screen.reshape(160, 160, 1)])[0]
        print(float(prediction[0]),float(prediction[1]),float(prediction[2]))
        cv2.waitKey(10000)

test_model()

