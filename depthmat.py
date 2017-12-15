import numpy as np
import cv2
import cv
import freenect
import numpy as np
import time
range_dic=((400,677,50),(677,724,100),(724,834,150),(834,890,200))

def getDepthMat(lower,higher,color):
    depth,timestamp = freenect.sync_get_depth()
    depth = 255 * np.logical_and(depth > lower, depth < higher)
    depth = depth.astype(np.uint8)
    c1=200
    r1=0
    depth = depth[c1:c1+640,r1:r1+480]
    depth=depth*color
    return depth
'''
while True:
    depth = getDepthMat()
    print(depth)
    cv2.imshow('Depth', depth)
    cv2.waitKey(10)
'''
data_=[]
for rang in range_dic:
    print('%d < depth < %d' % (rang[0], rang[1]))
    image=getDepthMat(rang[0],  rang[1],rang[2])
    cv2.imshow('Depth',image)
    data_.append(image)
    cv2.waitKey(1000)
    time.sleep(.1)
np.save('/home/pawan/PycharmProjects/Knet/live.npy',data_)


