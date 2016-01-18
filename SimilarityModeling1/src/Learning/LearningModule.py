'''
Created on Nov 22, 2015

@author: soroosh
'''
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.tree.tree import DecisionTreeClassifier
from sklearn import preprocessing, cross_validation, svm
import numpy as np
from math import floor
from sklearn.metrics.classification import precision_score, accuracy_score,\
    f1_score, recall_score
from Common.Result import ResultObject
from Common.CommonHelper import Announce
import sklearn
from sklearn.linear_model.stochastic_gradient import SGDClassifier
from Feaures.Helper import SplitToSetLabel
from sklearn.neighbors.classification import KNeighborsClassifier
from sklearn.metrics.ranking import roc_curve, auc
from numpy import interp
import matplotlib.pyplot as plt

class Learner(object):
    


    def __init__(self, configObject):
        self.configObject = configObject
    
    
    def learn(self, dataset):
        
        _scaler = preprocessing.Normalizer()
        _folds = 5
        
        X_train, _inputLabels = SplitToSetLabel(dataset)
        _inputInstances = _scaler.fit_transform(X_train)
        
        X = X_train
        y = _inputLabels
        
        #Decision Tree
        classifier = DecisionTreeClassifier(random_state=0)
        self.Predict( X,y, classifier, _folds, 'DecisionTree', '')
        
        

        #kNN
        classifier = KNeighborsClassifier(n_neighbors=1)
        self.Predict( X,y, classifier, _folds, 'kNN1', '#N = 1')
        
        #kNN
        classifier = KNeighborsClassifier(n_neighbors=3)
        self.Predict( X,y, classifier, _folds, 'kNN3', '#N = 3')
        
        #kNN
        classifier = KNeighborsClassifier(n_neighbors=5)
        self.Predict( X,y, classifier, _folds, 'kNN5', '#N = 5')
        

        
        #SGD
        classifier = SGDClassifier(loss="log", penalty="elasticnet")
        self.Predict( X,y, classifier, _folds, 'SGD-1', 'loss: log, penalty: elasticnet')
        
        
        #SGD
        classifier = SGDClassifier(loss="modified_huber", penalty="elasticnet")
        self.Predict( X,y, classifier, _folds, 'SGD-2', 'loss: modified_huber, penalty: elasticnet')

        #SVM
        classifier = svm.SVC(
                        kernel=       'linear', 
                        C=            1.0,
                        max_iter=     -1,
                        class_weight= {0 : 1.0, 1: 200.0 }
                     )
        self.Predict( X,y, classifier, _folds, 'SVM - Linear', 'linear - C=1.0 - class weight 1:200')
        
        
        #SVM
        classifier = svm.SVC(
                        kernel=       'rbf', 
                        C=            1.0,
                        max_iter=     -1,
                        class_weight= {0 : 1.0, 1: 200.0 }
                     )
        self.Predict( X,y, classifier, _folds, 'SVM - RBF', 'rbf - C=1.0 - class weight 1:200')
        
    def Predict(self, inp, labels, classifier, folds, name, paramdesc):
        X= inp
        y = labels
        X, y = X[y != 2], y[y != 2]
        n_samples, n_features = X.shape
        
        ###############################################################################
        # Classification and ROC analysis
        
        # Run classifier with cross-validation and plot ROC curves
        cv = StratifiedKFold(y, n_folds=folds)
        
        mean_tpr = 0.0
        mean_fpr = np.linspace(0, 1, 100)
        all_tpr = []
        
        _precision = 0.0
        _recall = 0.0
        _accuracy = 0.0
        _f1 = 0.0
        
        for i, (train, test) in enumerate(cv):
            probas_ = classifier.fit(X[train], y[train]).predict_proba(X[test])
            pred_ = classifier.predict(X[test])
            _precision += precision_score(y[test], pred_)
            _recall += recall_score(y[test], pred_)
            _accuracy += accuracy_score(y[test], pred_)
            _f1 += f1_score(y[test], pred_)
            # Compute ROC curve and area the curve
            fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
            mean_tpr += interp(mean_fpr, fpr, tpr)
            mean_tpr[0] = 0.0
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
        
        _precision /= folds
        _recall /= folds
        _accuracy /= folds
        _f1 /= folds
        
        
        plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
        
        mean_tpr /= len(cv)
        mean_tpr[-1] = 1.0
        mean_auc = auc(mean_fpr, mean_tpr)
        plt.plot(mean_fpr, mean_tpr, 'k--',
                 label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)
        
        plt.xlim([-0.05, 1.05])
        plt.ylim([-0.05, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic - {0}'.format(name))
        plt.legend(loc="lower right")
        plt.savefig(self.configObject['outputdir'] + '/' + name + '.png')
        plt.close()
        
        result = self.OutputResult(name, paramdesc, len(inp), floor(labels.size / folds), _precision, _recall, _accuracy, _f1) 
        Announce(result)
        
        
    
    def OutputResult(self, learner_name, params, instance_size ,test_instance_size, precision, recall, accuracy, f1score):
        return ResultObject(
            number_of_instances = int(instance_size),
            portion_of_test_set = int(5),
            number_of_training_set = int(instance_size - test_instance_size),
            number_of_test_set = int(test_instance_size),
            precision = precision ,
            recall = recall ,
            fscore = f1score ,
            accuracy = accuracy,
            confusion_matrix = None,
            learner_parameters = params,
            learner_name = learner_name
        )