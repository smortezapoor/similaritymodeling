class ResultObject(object):

    def __init__(self, number_of_instances, portion_of_test_set, number_of_training_set, number_of_test_set, precision, recall, accuracy, fscore, confusion_matrix, learner_parameters, learner_name):
        '''
        Constructor
        '''
        self.number_of_instances = number_of_instances
        self.portion_of_test_set = portion_of_test_set
        self.number_of_training_set = number_of_training_set
        self.number_of_test_set = number_of_test_set
        self.precision = precision
        self.recall = recall
        self.fscore = fscore
        self.accuracy = accuracy
        self.confusion_matrix = confusion_matrix
        self.learner_parameters = learner_parameters
        self.learner_name = learner_name
        
        
    def __str__(self):
        _out = '--------------------------------------\r\n'
        _out = _out + self.learner_name + '\r\n\r\n'
        _out = _out + ' # Instances: {0} \r\n     # Cross-validation folds: {1} \r\n     # Training set: {2} \r\n     # Test set: {3} \r\n \r\n Precision: {4} \r\n Recall: {5} \r\n Accuracy: {6} \r\n F1-score: {7} \r\n\r\n Confusion Matrix: \r\n {8}'.format(self.number_of_instances,self.portion_of_test_set, self.number_of_training_set, self.number_of_test_set, self.precision, self.recall,self.accuracy, self.fscore, self.confusion_matrix)
        _params = '\r\n\r\n Learner parameters: ' + self.learner_parameters
        
        _out = _out + _params
            
        return _out