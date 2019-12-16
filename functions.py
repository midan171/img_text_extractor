import cv2 
import numpy as np 
import os


dir_path = os.path.dirname(os.path.abspath(__file__))

fname = "C:\\Users\\midan\\Desktop\\Gerakinis\\app\\app\\data\\imgs\\test4.png"


def to_black_white(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black white img", img)
    cv2.waitKey(0)
    return img

def img_thresh_binary(img):
    #Transform into black n white, for simple thresholding functions
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black white img", img)
    cv2.waitKey(0)
    #threshold function
    ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("black", img)
    cv2.waitKey(0)
    return img

def img_thresh_adative(img):
    #Transform into black n white, for simple thresholding functions
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black white img", img)
    cv2.waitKey(0)
    #threshold function
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    cv2.imshow("black", th2)
    cv2.waitKey(0)
    return img

def img_thresh_adative_gaus(img):
    #Transform into black n white, for simple thresholding functions
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black white img", img)
    cv2.waitKey(0)
    #threshold function
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)

    cv2.imshow("black", th3)
    cv2.waitKey(0)
    return img



