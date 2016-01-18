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


### Data


### Results


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Data]: <https://github.com/joemccann/dillinger>
   [TU Jump Into The Future]: <https://www.ims.tuwien.ac.at/projects/virtualjumpsimulator>
   [Python 2.7]: <https://www.python.org/download/releases/2.7/>
   [scikit-learn]: <http://scikit-learn.org/stable/>
   [OpenCV]: <http://opencv.org/>
   [NumPy]: <http://www.numpy.org/>
   [matplotlib]: <http://matplotlib.org/>
   [OpenCV-Python]: <http://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html#gsc.tab=0>
   
   
  
