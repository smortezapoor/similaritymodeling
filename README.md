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

In the first stage of gathering features, each frame is inspected for similarity to three particular parts, called "stand-window", "mid-window" and "high-window", of the frames at which a jump happens. There are 10 features, extracted and stored to be compared to the other frames and they can be found in Data section. From these features, called reference windows hereafter, 5 reference windows correspond to "high-window", 4 reference windows correspond to "mid-window" and 1 to the "stand-window". These reference windows is the place where the operator stands before a jump as "stand-window", the place where the operator will be located during a jump, referred to as "mid-window" and the place where the operator will be hanged after a jump.

In each frame, three different windows, matched to the features in size are extracted and the distance to the reference windows are calculated with "Taxicab geometry" and summed up. Thus per each frame, 10 different similarity measurement features are calculated and added to the feature vector.

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

The results of the experiment can be found [HERE]. The results contain the information of the metrics from trained classifiers such as Decision Tree, kNN, SVM and SGD with different parameters. What's more, "Receiver Operating Charactristic" diagrams can be found in the results folder.


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
   
   
  
