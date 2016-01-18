'''
Created on Nov 22, 2015

@author: soroosh
'''
from Feaures.Helper import *
import numpy as np
import cv2
from Feaures.Soroosh import *
from Feaures.Andreas import AddMyFeatures_Andreas
from Common.CommonHelper import Announce, LogIt
import operator

class FeatureExtractor(object):
    
    def __init__(self, configObject):
        self.configObject = configObject
        self.files = []
        self.output = []
        self.currentOutputRow = []
    
    def CreateAllFeatureValues(self):
        self.readVideoFileNames()
        
        frametoskip = int(self.configObject['frametoskip'])
        
        for video_filename in self.files:
            LogIt('-#Data: {0}'.format(len(self.output)))
            Announce('-File opened: {0}'.format(video_filename))
            
            
            cap = self.openVideo(video_filename)
            
            cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 14000)
                        
            fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
            framecount = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
            frameresolution_width = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
            frameresolution_height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
            

            
            
            
            framecount_int = int(framecount)
            
            Announce('----File contains {0} frames with rate {1} fps in {2}x{3}'.format(framecount_int, fps, frameresolution_width, frameresolution_height))
            
            for i in range (0, framecount_int):
                
                #read a frame
                ret , frame = cap.read()
                LogIt('Read')
                
                #cv2.imshow('image',frame)
                
                #cv2.imwrite(self.configObject['outputdir'] + 'messigray.png',frame)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()

                
                #check if the frame is readable
                if ret == False:
                    LogIt('False')
                    break
                
                #######skip as many frames as needed here
                if i % (frametoskip + 1) is not 0:
                    continue
                
                if i < framecount_int:
                    LogIt('Create new')
                    #flush all data in a output row
                    self.createOutputRow()
                    
                    #add a label for the new frame
                    self.addLabel(video_filename, cap.get(cv2.cv.CV_CAP_PROP_POS_MSEC))
                    
                    if self.configObject['features'] == '*' or  self.configObject['features'] == 'soroosh':
                        #add features from Soroosh
                        self.addFeatures_Soroosh(video_filename, cap, frame, self.configObject)
                        LogIt('Features Created')
                        
                    
                    if self.configObject['features'] == '*' or  self.configObject['features'] == 'andreas':
                        #add feature from Andreas
                        self.addFeatures_Andreas(video_filename, cap, frame,  self.configObject)
                        
                    #add the output row to the output matrix
                    self.submitOutputRow()
                    LogIt('Output added {0}'.format(i))
            
            self.closeVideo(cap)
            Announce('-File closed: {0}'.format(video_filename))
    
    def createOutputRow(self):
        self.currentOutputRow = []
    
    def submitOutputRow(self):
        self.output.append(self.currentOutputRow)
    
    def readVideoFileNames(self):
        self.files = readAllFileNames(self.configObject['inputdir'], 'mp4')
    
    
    def openVideo(self, video_filename):
        #open the video file
        LogIt(self.configObject['inputdir'] + '/' +  video_filename)
        cap = cv2.VideoCapture(self.configObject['inputdir'] + '/' +  video_filename)
        return cap
    
    def closeVideo(self, cap):
        cv2.destroyAllWindows()
        cap.release()
    
    def addLabel(self, filename, req_millisecond):
        #self.currentOutputRow.append('{0}:{1}'.format(int(req_millisecond/(1000*60)), (req_millisecond/1000) - (int(req_millisecond/(1000*60))*60)))
        self.currentOutputRow.append(groundTruthValue(self.configObject, filename, req_millisecond))
    
    def addFeatures_Soroosh(self, filename, cap, frame, confobj):
        new_features = AddMyFeatures_Soroosh(filename, cap, frame, confobj)
        
        for i in range(0, len(new_features)):
            self.currentOutputRow.append(new_features[i])
        
        
    def addFeatures_Andreas(self, filename, cap, frame, confobj):
        new_features = AddMyFeatures_Andreas(filename, cap, frame, confobj)
        
        for i in range(0, len(new_features)):
            self.currentOutputRow.append(new_features[i])
    
    def returnLearningList(self):
        return self.output
    
    def SaveDataset(self, dataset):
        Announce('Writing the result to the intermediary dataset')
        _outputdir = self.configObject['outputdir']
        _writer = open(self.configObject['outputdir'] + '/dataset.dat', 'w+')
        for _line in dataset:
            _outline=''
            for i in range(0, len(_line)):
                _outline+= str(_line[i])+ ('\n' if i == len(_line)-1 else ',')
            _writer.write(_outline)
        
        _writer.flush()
        _writer.close()
        Announce('Data is written successfully')

    
    def ReadDataset(self):
        _reader = open(self.configObject['outputdir'] + '/dataset.dat', 'r')
        Announce('Reading out the intermediary dataset')
        _dataset = []
        for _line in _reader.readlines():
            _splitted = _line.split(',')
            _row = []
            for i in range(0, len(_splitted)):
                _row.append(float(_splitted[i]))
            _dataset.append(_row)
        
        _reader.close()
        Announce('Successfully read {0} line of data'.format(len(_dataset)))
        return _dataset

    
    def PrepareDataset(self, dataset):
        _outputLabels = [x[0] for x in dataset]
        _first_class_count = np.count_nonzero(_outputLabels)
        _second_class_count = len(_outputLabels) - _first_class_count
        
        OutX_train = []
        
        ratio = int(_second_class_count/_first_class_count)
        
        ratio = int( ratio/4)
        
        _ratio_counter = 0
        
        for i in range(0, len(_outputLabels)):
            if i%ratio == 0 or _outputLabels[i] == 1:
                currentRow = dataset[i]
                nextRow1 = dataset[(i+1) % len(_outputLabels)][1:]
                nextRow2 = dataset[(i+2) % len(_outputLabels)][1:]
                nextRow3 = dataset[(i+3) % len(_outputLabels)][1:]
                nextRow4 = dataset[(i+4) % len(_outputLabels)][1:]
                nextRow5 = dataset[(i+5) % len(_outputLabels)][1:]
                smn = map(operator.add, currentRow[1:], nextRow1)
                smn = map(operator.add, smn, nextRow2)
                smn = map(operator.add, smn, nextRow3)
                smn = map(operator.add, smn, nextRow4)
                smn = map(operator.add, smn, nextRow5)
                currentRow = currentRow + nextRow1 + nextRow2 + nextRow3 + nextRow4 + nextRow5 + smn
                OutX_train.append(currentRow)
        
        return ShakeData(OutX_train)
    
    
