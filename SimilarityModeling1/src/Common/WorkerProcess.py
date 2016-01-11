'''
Created on Nov 22, 2015

@author: soroosh
'''
from Feaures.FeatureExtraction import FeatureExtractor
from Learning.LearningModule import Learner


def Process(configObject):
    
    #Creating an object of FeatureExtractor
    _featureExtractor = FeatureExtractor(configObject)
    

    
    dataset = []
    
    if configObject['mode'] == '0':
        #reading video files
        _featureExtractor.CreateAllFeatureValues()
    
        #obtaining a final vector of features with a label at the beginning
        dataset = _featureExtractor.returnLearningList()
        
        _featureExtractor.SaveDataset(dataset)
    else :
        dataset = _featureExtractor.ReadDataset()
    
    #Creatung an object of learner class
    _learner = Learner(configObject)
    
    #Learning from the data gathered in the previous phase
    _learner.learn(dataset)
    
    #Showing output
    _learner.showOutput()