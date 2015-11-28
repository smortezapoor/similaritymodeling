'''
Created on Nov 22, 2015

@author: soroosh
'''
from sys import argv
import ast
from Common import WorkerProcess


def Main(argv):
    
    _config  = open('./config.txt', 'r')
    
    _configLine = _config.readline()
    
    _config.close()
    
    _configObject =  ast.literal_eval(_configLine)
    
    
    WorkerProcess.Process(_configObject)


if __name__ == '__main__':
    Main(argv)