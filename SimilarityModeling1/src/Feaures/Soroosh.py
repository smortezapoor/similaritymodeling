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
    _frame_blur_gray = cv2.cvtColor(cv2.cvtColor(_frame_blur, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    
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
                my_results.append(MeasureSimilarity(cv2.cvtColor(cv2.cvtColor(so_features[_key], cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR),_standwindow_blur_gray))
            else:
                my_results.append(MeasureSimilarity(so_features[_key],_standwindow_blur_gray))
                
        if 'feature_mid' in _key:
            if 'color' in _key:
                my_results.append(MeasureSimilarity(cv2.cvtColor(cv2.cvtColor(so_features[_key], cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR),_midwindow_blur_gray))
            else:
                my_results.append(MeasureSimilarity(so_features[_key],_midwindow_blur_gray))
                
        if 'feature_high' in _key:
            if 'color' in _key:
                my_results.append(MeasureSimilarity(cv2.cvtColor(cv2.cvtColor(so_features[_key], cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR),_highwindow_blur_gray))
            else:
                my_results.append(MeasureSimilarity(so_features[_key],_highwindow_blur_gray))
    
        #Announce('Filter: {0} : Applied. {1}'.format(_key, my_results))
    
    
    reshaped_1 = _standwindow.reshape(_standwindow.size).astype(float)
    
    
    #RGB of stand
    ss_1_1 = reshaped_1[0:_standwindow.size:3]
    ss_1_2 = reshaped_1[1:_standwindow.size:3]
    ss_1_3 = reshaped_1[2:_standwindow.size:3]
    
    ones1_1 = np.ones(ss_1_1.size)
    ones1_2 = np.ones(ss_1_2.size)
    ones1_3 = np.ones(ss_1_3.size)
    
    sum1_1 = np.dot(ss_1_1, ones1_1)
    sum1_2 = np.dot(ss_1_2, ones1_2)
    sum1_3 = np.dot(ss_1_3, ones1_3)
    
    my_results.append(sum1_1)
    my_results.append(sum1_2)
    my_results.append(sum1_3)
    
    #RGB of mid
    ss_2_1 = reshaped_1[0:_midwindow.size:3]
    ss_2_2 = reshaped_1[1:_midwindow.size:3]
    ss_2_3 = reshaped_1[2:_midwindow.size:3]
    
    ones2_1 = np.ones(ss_2_1.size)
    ones2_2 = np.ones(ss_2_2.size)
    ones2_3 = np.ones(ss_2_3.size)
    
    sum2_1 = np.dot(ss_2_1, ones2_1)
    sum2_2 = np.dot(ss_2_2, ones2_2)
    sum2_3 = np.dot(ss_2_3, ones2_3)
    
    my_results.append(sum2_1)
    my_results.append(sum2_2)
    my_results.append(sum2_3)
    
    #RGB of high
    ss_3_1 = reshaped_1[0:_midwindow.size:3]
    ss_3_2 = reshaped_1[1:_midwindow.size:3]
    ss_3_3 = reshaped_1[2:_midwindow.size:3]
    
    ones3_1 = np.ones(ss_3_1.size)
    ones3_2 = np.ones(ss_3_2.size)
    ones3_3 = np.ones(ss_3_3.size)
    
    sum3_1 = np.dot(ss_3_1, ones3_1)
    sum3_2 = np.dot(ss_3_2, ones3_2)
    sum3_3 = np.dot(ss_3_3, ones3_3)
    
    my_results.append(sum3_1)
    my_results.append(sum3_2)
    my_results.append(sum3_3)
    
    return my_results


def MeasureSimilarity(img1, img2):
    
    if img1.size != img2.size:
        Announce('Wrong measurement')
    
    _img1_reshaped = img1.reshape(img1.size).astype(float)
    _img2_reshaped = img2.reshape(img2.size).astype(float)
    sub =  np.subtract(_img1_reshaped, _img2_reshaped)
    ones = np.ones(sub.size)
    result = np.dot(sub, ones)
    
    return result

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