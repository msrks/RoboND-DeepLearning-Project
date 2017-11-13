import os
import numpy as np
import cv2

for fname in os.listdir("train/images/"):
    im = cv2.imread("train/images/"+fname)
    im = np.fliplr(im)
    print (fname)
    cv2.imwrite("train/images/"+"fliplr_"+fname, im)

for fname in os.listdir("train/masks/"):
    im = cv2.imread("train/masks/"+fname)
    im = np.fliplr(im)
    print (fname)
    cv2.imwrite("train/masks/"+"fliplr_"+fname, im)
