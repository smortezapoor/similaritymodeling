# Similarity Modeling
Project of the similarity modeling course

This project intends to detect the moment of jumping in a sky diving simulator, called "[TU Jump Into The Future]". 

### How to run

In order to be able to run this application, there are some prerequisits to be met. Following is the list of required softwares and packages to be installed before running this application.

#### Requirements

* [Python 2.7]
* [OpenCV]
* [OpenCV-Python]
* [scikit-learn]
* [NumPy]
* [matplotlib]

After installing mentioned softwares and packages, the application can be run as following:
 

```sh
user@workstation:~/SimilarityModeling1/src$ python sm1run.py
```

however, a configuration file should be edited in order to set the access locations properly.

#### Configuration

The configuration of the application can be found in "/src/config.txt". The config file looks like a key-value collection with following options:

* inputdir: This is the path to the folder containing the video files.
* inputfeatures: This is the path to the folder containing the feature files.
* features: the type of features to use. {*} means all features.
* frametoskip: # of frames to skip when scanning the video files.
* ground-truth: This is the path to the ground truth file.
* outputdir: This is the path to the folder which is intended to be used as the output folder.
* mode: The mode in which the application works. {-1, 0, 1} for 
   * -1: Only creating the intermediary dataset
   * 0: Creating the intermediary dataset as well as training the classifiers
   * 1: Using the intermediary dataset to train the classifiers.


### Architecture 

The architecture of the program is as following:

There are three different stages to compute features for a particular frame.

#### 1. Similarity measurement

In the first stage of gathering features, each frame is inspected for similarity to three particular parts, called "stand-window", "mid-window" and "high-window", of the frames at which a jump happens. There are 10 features, extracted and stored to be compared to the other frames and they can be found in Data section. From these features, called reference windows hereafter, 5 reference windows correspond to "high-window", 4 reference windows correspond to "mid-window" and 1 to the "stand-window". These reference windows are the places where the operator stands before a jump as "stand-window", the operator will be located during a jump as "mid-window" and the operator will be hanged after a jump as "high-window". In all cases, these reference windows are blured and in all but one case they are gray-scaled.

In each frame, three different windows, matched to the features in size are extracted and the distance to the reference windows are calculated with "Taxicab geometry" and summed up. Thus per each frame, 10 different similarity measurement features are calculated and added to the feature vector.

##### Stand-window
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_stand.png)
##### Mid-windows
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_mid_01.png)
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_mid_02.png)
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_mid_03.png)
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_mid_04.png)
##### High-windows
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_high_01.png)
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_high_02.png)
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_high_03.png)
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_high_04.png)
![alt feature](http://smortezapoor.com/share/SM/SM1/features/feature_high_05_color.png)






#### 2. Statistical features

In addition to the similarity measurement features, some statistical features are gathered such as the color information of each reference window in a frame as different values for different channels.

#### 3. Sequence combination features

An important stage in forming the feature vector for this problem is by combining the features which are calculated for each frame with neighbor frames. As the operation is offline and needn't be a realtime system, this stage is allowed. Therefore for each feature vector in the dataset list, the feature vectors which belong to i to i+5 frames are appended to the feature vector of i-th frame. Furthermore, a linear combination of these 6 vectors are added at end of the i-th frame feature vector. This stage helps impove the results considerably.

Note: A circular queue is used to make sure that next frames are always available. 

### Data

The [Data] used for this experiment can be downloaded from following path:

[http://smortezapoor.com/share/SM/SM1/Data.zip]

The [Data] contains all video files along with required csv groundtruth file and reference windows images.



### Results

The results of the experiment can be found [HERE]. The results contain the information of the metrics from trained classifiers such as Decision Tree, kNN, SVM and SGD with different parameters. What's more, "Receiver Operating Charactristic" diagrams can be found in the results folder as well below.

#### Decision Tree

DecisionTree

     # Instances: 7060 
     # Cross-validation folds: 5
     # Training set: 5648 
     # Test set: 1412 
     
     Precision: 0.758719134073 
     Recall: 0.739797747056 
     Accuracy: 0.901698192896 
     F1-score: 0.748981308261 



     Learner parameters: 

![alt Decision Tree](http://smortezapoor.com/share/SM/SM1/Final%20Results%20(offline)/DecisionTree.png)

#### kNN (n=1)

    # Instances: 7060 
     # Cross-validation folds: 5 
     # Training set: 5648 
     # Test set: 1412 
 
     Precision: 0.852281990212 
     Recall: 0.724086021505 
     Accuracy: 0.920397687466 
     F1-score: 0.782794093737 

     Learner parameters: #N = 1

![alt kNN-1](http://smortezapoor.com/share/SM/SM1/Final%20Results%20(offline)/knn1.png)

#### kNN (n=3)

     # Instances: 7060 
     # Cross-validation folds: 5 
     # Training set: 5648 
     # Test set: 1412 
 
     Precision: 0.859116720568 
     Recall: 0.643297491039 
     Accuracy: 0.908357323294 
     F1-score: 0.735159140642 

     Learner parameters: #N = 3
 
![alt kNN-3](http://smortezapoor.com/share/SM/SM1/Final%20Results%20(offline)/knn3.png)

#### kNN (n=5)

     # Instances: 7060 
     # Cross-validation folds: 5 
     # Training set: 5648 
     # Test set: 1412 
 
     Precision: 0.844674234802 
     Recall: 0.566095750128 
     Accuracy: 0.893200009729 
     F1-score: 0.676878946081 

     Learner parameters: #N = 5

![alt kNN-5](http://smortezapoor.com/share/SM/SM1/Final%20Results%20(offline)/knn5.png)

#### SGD-1

     # Instances: 7060 
     # Cross-validation folds: 5 
     # Training set: 5648 
     # Test set: 1412 
 
     Precision: 0.223368451879 
     Recall: 0.392158218126 
     Accuracy: 0.605664878806 
     F1-score: 0.174710216223 

     Learner parameters: loss: log, penalty: elasticnet
 
![alt SGD-1](http://smortezapoor.com/share/SM/SM1/Final%20Results%20(offline)/sgd-1.png)

#### SGD-1

     # Instances: 7060 
     # Cross-validation folds: 5 
     # Training set: 5648 
     # Test set: 1412 
 
     Precision: 0.321637899887 
     Recall: 0.435570916539 
     Accuracy: 0.690193651789 
     F1-score: 0.33393417591 

     Learner parameters: loss: modified_huber, penalty: elasticnet
 
![alt SGD-2](http://smortezapoor.com/share/SM/SM1/Final%20Results%20(offline)/sgd-2.png)

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Data]: <http://smortezapoor.com/share/SM/SM1/Data.zip>
   [HERE]: <http://smortezapoor.com/share/SM/SM1/Final%20Results%20(offline)/>
   [http://smortezapoor.com/share/SM/SM1/Data.zip]: <http://smortezapoor.com/share/SM/SM1/Data.zip>
   [TU Jump Into The Future]: <https://www.ims.tuwien.ac.at/projects/virtualjumpsimulator>
   [Python 2.7]: <https://www.python.org/download/releases/2.7/>
   [scikit-learn]: <http://scikit-learn.org/stable/>
   [OpenCV]: <http://opencv.org/>
   [NumPy]: <http://www.numpy.org/>
   [matplotlib]: <http://matplotlib.org/>
   [OpenCV-Python]: <http://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html#gsc.tab=0>
   
   
  
