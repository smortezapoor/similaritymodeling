'''
Created on Nov 22, 2015

@author: soroosh
'''
import os

GroundTruthHolder = []

def readAllFileNames(destdir, extension):
    return [f for f in os.listdir(destdir) if (extension == '*' or f.endswith('.' + extension))]


def groundTruthValue(configObject ,filename, req_millisecond):
    '''
    Returns the label of a frame based on ground truth
    
    
    :param configObject:
    :param filename:
    :param req_millisecond:
    '''
    if len(GroundTruthHolder) == 0:
        readGroundTruth(configObject)
        
    fileobject = [x for x in GroundTruthHolder if x['Filename'] == filename]
    
    if len(fileobject) == 0:
        raise Exception('groundtruth data not found')
    
    if fileobject[0]['Jump #1'] == '' and fileobject[0]['Jump #2'] == '':
        return 0;
    
    
    min1 = fileobject[0]['Jump #1'].split(':')[0]
    sec1 = fileobject[0]['Jump #1'].split(':')[1]
    #check if it is in the first jump
    _jump1_msecs = (int(min1) * 60 + int(sec1)) * 1000
    
    if req_millisecond >= _jump1_msecs and req_millisecond <=_jump1_msecs + 2000:
        return 1
    
    
    if fileobject[0]['Jump #2'] is not '':
        min2 = fileobject[0]['Jump #2'].split(':')[0]
        sec2 = fileobject[0]['Jump #2'].split(':')[1]
        _jump2_msecs = (int(min2) * 60 + int(sec2)) * 1000
        if req_millisecond >= _jump2_msecs and req_millisecond <=_jump2_msecs + 2000:
            return 1
    
    return 0

def readGroundTruth(configObject):
    '''
    Reads Ground Truth File
    
    
    :param configObject:
    '''
    f = open(configObject['ground-truth'], 'r')
    
    for line in f.readlines():
        _splitted = line.strip().split(',')
        
        if len(_splitted) < 7:
            continue
        
        GroundTruthHolder.append({'#' : _splitted[0], 'Filename' : _splitted[1], 'Hands' : _splitted[2], 'Feet' : _splitted[3], 'Empty' : _splitted[4], 'Jump #1' : _splitted[5], 'Jump #2' : _splitted[6]})
        
    
    f.close()