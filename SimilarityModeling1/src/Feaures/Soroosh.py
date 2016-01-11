'''
Created on Nov 22, 2015

@author: soroosh
'''
from Feaures.Helper import readAllFileNames
from Common.CommonHelper import Announce
from numpy import array, uint8

'''
frame2 = ReadHighWindow(frame)
frame3 = ApplyBlurImage(frame2)

# Our operations on the frame come here
#frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)

cv2.imshow('image',frame)
cv2.imshow('image2',frame2)
cv2.imshow('image3',frame3)

cv2.imwrite(self.configObject['outputdir'] + 'messigray.png',frame3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
                
                
from numpy.random.mtrand import np
import cv2

so_features = {}

def AddMyFeatures_Soroosh(filename, cap, frame, configObject):
    
    my_results = []
    
    if len(so_features) == 0:
        ReadFeatures(configObject['inputfeatures'])
    
    _frame_blur = ApplyBlurImage(frame)
    _frame_blur_gray = cv2.cvtColor(_frame_blur, cv2.COLOR_BGR2GRAY)
    
    _standwindow = ReadStandWindow(frame)
    _midwindow = ReadMidWindow(frame)
    _highwindow = ReadHighWindow(frame)
    
    _standwindow_blur = ReadStandWindow(_frame_blur)
    _midwindow_blur = ReadMidWindow(_frame_blur)
    _highwindow_blur = ReadHighWindow(_frame_blur)
    
    _standwindow_blur_gray = ReadStandWindow(_frame_blur_gray)
    _midwindow_blur_gray = ReadMidWindow(_frame_blur_gray)
    _highwindow_blur_gray = ReadHighWindow(_frame_blur_gray)
    
    _keys = so_features.keys()
    
    for _key in sorted(_keys):
        if 'feature_stand' in _key:
            if 'color' in _key:
                my_results.append(MeasureSimilarity(so_features[_key],_standwindow_blur))
            else:
                my_results.append(MeasureSimilarity(so_features[_key],_standwindow_blur_gray))
                
        if 'feature_mid' in _key:
            if 'color' in _key:
                my_results.append(MeasureSimilarity(so_features[_key],_midwindow_blur))
            else:
                my_results.append(MeasureSimilarity(so_features[_key],_midwindow_blur_gray))
                
        if 'feature_high' in _key:
            if 'color' in _key:
                my_results.append(MeasureSimilarity(so_features[_key],_highwindow_blur))
            else:
                my_results.append(MeasureSimilarity(so_features[_key],_highwindow_blur_gray))
    
    
    return my_results


def MeasureSimilarity(img1, img2):
    
    if len(img1) != len(img2):
        Announce('Wrong measurement')
    
    if len(img1[0]) != len(img2[0]):
        Announce('Wrong measurement')
        
    img1_is_grayscale = isinstance(img1[0][0], uint8)
    img2_is_grayscale = isinstance(img2[0][0], uint8)
    
    _amount = 0.0
    
    for i in range(0, len(img1)):
        for j in range(0, len(img1[i])):
            _r_1 = int(img1[i][j] if img1_is_grayscale else img1[i][j][0])
            _g_1 = int(img1[i][j] if img1_is_grayscale else img1[i][j][1])
            _b_1 = int(img1[i][j] if img1_is_grayscale else img1[i][j][2])
            
            _r_2 = int(img2[i][j] if img2_is_grayscale else img2[i][j][0])
            _g_2 = int(img2[i][j] if img2_is_grayscale else img2[i][j][1])
            _b_2 = int(img2[i][j] if img2_is_grayscale else img2[i][j][2])
            
            _dot_product = _r_1 * _r_2 + _g_1 * _g_2 + _b_1 * _b_2
            
            _amount += _dot_product
    
    return _amount

def ReadFeatures(inputfeatures_address):
    _filenames = readAllFileNames(inputfeatures_address, 'png')
    for _file in _filenames:
        _fileaddress  = inputfeatures_address + '/' + _file
        retval = cv2.imread(_fileaddress)
        so_features[_file] = retval

def ReadStandWindow(frame):
    frame2 = frame[300:480, 270:450]
    return frame2
    
def ReadMidWindow(frame):
    frame2 = frame[150:350, 260:460]
    return frame2

def ReadHighWindow(frame):
    frame2 = frame[0:200, 260:460]
    return frame2
    

def ApplyBlurImage(frame):
    dst = cv2.blur(frame,(20,20))
    return dst