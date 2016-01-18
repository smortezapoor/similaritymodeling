'''
Created on Nov 22, 2015

@author: soroosh
'''
from Feaures.FeatureExtraction import FeatureExtractor
from Learning.LearningModule import Learner
from Common.CommonHelper import Announce, openAnnounce, closeAnnounce


def Process(configObject):
    
    #Creating an object of FeatureExtractor
    _featureExtractor = FeatureExtractor(configObject)
    

    
    dataset = []
    openAnnounce(configObject['outputdir'])
    
    if configObject['mode'] == '0' or configObject['mode'] == '-1':
        #reading video files
        _featureExtractor.CreateAllFeatureValues()
    
        #obtaining a final vector of features with a label at the beginning
        dataset = _featureExtractor.returnLearningList()
        
        dataset = _featureExtractor.PrepareDataset(dataset)
        
        _featureExtractor.SaveDataset(dataset)
    else :
        dataset = _featureExtractor.ReadDataset()
    
    if not configObject['mode'] == '-1':
        #Creatung an object of learner class
        _learner = Learner(configObject)
        #Learning from the data gathered in the previous phase
        _learner.learn(dataset)
        
    Announce('Finished')  
    closeAnnounce()