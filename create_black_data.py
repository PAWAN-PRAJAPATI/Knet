import pyscreenshot as ImageGrab
import cv2
import numpy as np
import os
import pyxhook
from random import shuffle


def kbevent(event):
    global running
    if event.Ascii == 32:
        running = False
    if event.Ascii == 8:
        running = True

hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()
running = True

file='Whole_data.npy'

print('finished!!!')
def read_():
    i=0
    sample=[]
    training=list(np.load(file))
    shuffle(training)
    shuffle(training)
    for data in training:
        cv2.imshow('black',data[0])
        cv2.waitKey(300)
        print(data[1])
    print(len(training))
read_()

def grab():
    img = ImageGrab.grab(bbox=(30, 380, 680,680))  # x, y, w, h
    img_np = np.array(img)
    return img_np


def remove_frame(n):
     data_=[]
     training = list(np.load())
     shuffle(training)
     i=0
     for data in training:
         if(i>n):
             break
         i=i+1
         data_.append(data)
     np.save(black_file,data)
     print('Completed')





def create():
    i=0
    while 1:
        try:
            i=i+1
            frame=grab()
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (160, 160))
            cv2.imshow('frame',frame)
            frame_array = np.array(frame)
            training_data.append([frame_array,[0,0]])
            if(i%100==0):
                print(i)
                np.save(black_file,training_data)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            if(running==False):
                while not running:
                    print("not running!!!")
                    pass
        except Exception as e:
            print(e)
            pass
    cv2.destroyAllWindows()

