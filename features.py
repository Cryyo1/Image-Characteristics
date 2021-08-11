import cv2 as cv
import math 
import numpy as np


'''
 * These functions  return a certain feature that describe sahpe in an image
 * @param: img is source image that contains the a shape to calculate its features
 * Each one of these features are explained in readme.md 
'''

'''**********************************************************************************'''
def area(img):
      return cv.countNonZero(img)
'''**********************************************************************************'''  
def Perimeter(img):
    contours,hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    max_area = 0
    for i in range(len(contours)):
        area = cv.contourArea(contours[i])
        if(area > max_area):
            max_area = area
            big_contour = i

    return cv.arcLength(contours[big_contour],True)
'''**********************************************************************************'''
def centroide(img):
    moments=cv.moments(img)
    cx = int(moments["m10"] / moments["m00"])
    cy = int(moments["m01"] / moments["m00"])
    return cx,cy
'''**********************************************************************************'''
def circularity(img):
    perimeter=Perimeter(img)
    area=area(img)
    return 4*math.pi*(area/perimeter**2)
'''**********************************************************************************'''
def eccentricity(img):
    ret,img = cv.threshold(img,11,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    contours,hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    max_area = 0
    for i in range(len(contours)):
        area = cv.contourArea(contours[i])
        if(area > max_area):
            max_area = area
            big_contour = i 
    elipse=cv.fitEllipse(contours[big_contour])
    aremc=math.pi*elipse[1][0]*elipse[1][1]
    area=area(img)
    return area/aremc
'''**********************************************************************************'''
def rectangularity(img):
    ret,img = cv.threshold(img,11,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    contours,hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    max_area = 0
    for i in range(len(contours)):
        area = cv.contourArea(contours[i])
        if(area > max_area):
            max_area = area
            big_contour = i
        
    rect = cv.minAreaRect(contours[big_contour])
    area=area(img)
    return area/(rect[1][0]*rect[1][1])
    
'''**********************************************************************************'''
def compacity(img):
    perimeter=Perimeter(img)
    area=area(img)
    return 1-(4*math.pi*(area/perimeter**2))
'''**********************************************************************************'''
