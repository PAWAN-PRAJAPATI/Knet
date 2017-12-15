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


def grab():
    img = ImageGrab.grab(bbox=(30, 380, 680,680))  # x, y, w, h
    img_np = np.array(img)
    return img_np


file_name0 ='new_training_data-s0-r1.npy'
file_name1 ='new_training_data-s1-r1.npy'
file_name2 ='new_training_data-s2-r1.npy'
file_name3 ='new_training_data-s3-r1.npy'
black_file = 'new_training_data-black.npy'


print('File exists, loading previous data!')
training_data_0 = list(np.load(file_name3))+ list(np.load(file_name2))+ list(np.load(file_name1))+ list(np.load(file_name0))
shuffle(training_data_0)

training_data_1 = list(np.load(file_name3))+ list(np.load(file_name2))+ list(np.load(file_name1))+ list(np.load(file_name0))
shuffle(training_data_1)


des_file_0='final_r0.npy'
des_file_1='final_r1.npy'
final_file = 'final_dataset.npy'

des_data_1 = list(np.load(des_file_1))
des_data_0 = list(np.load(des_file_0))
final_shuffle = 'final_shuffled_data.npy'

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
            training_data.append([frame_array,[0,1,0]])
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

training_data=0
def connect_data():
    for data in training_data:
        cv2.imshow('Test',data[0])
        cv2.waitKey(2)
    print(len(training_data))
    cv2.destroyAllWindows()

def read():
    for data in final:
        if(data[1]==[1,0,0]):
            data[1]=[1,0]
        elif(data[1]==[0,1,0]):
            data[1]=[0,1]
        cv2.imshow('Test', data[0])
        print(data[1])
        cv2.waitKey(50)
    print(len(final))
    np.save(final_file,final)
    shuffle(final)
    np.save(final_shuffle,final)
    cv2.destroyAllWindows()


def read_final():
    i=0
    final_data = list(np.load('final_black_r0_r1.npy'))
    for data in final_data:
        cv2.imshow('Test',data[0])
        #np.save('sample_data.npy',data)
        print(data[1])
        cv2.waitKey(100)
    print(len(final_data))
    cv2.destroyAllWindows()

read_final()
def read_sample():
    i=0
    i=i+1
    s_data=[]
    sample = list(np.load('shuffled.npy'))
    shuffle(sample)
    for data in sample:
        i=i+1
        if(i==100):
            break
        cv2.imshow('Test',data[0])
        s_data.append(data)
        print(data[1])
        cv2.waitKey(1000)
    np.save('sample.npy',s_data)
