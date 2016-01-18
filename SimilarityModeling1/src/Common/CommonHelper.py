'''
Created on Nov 22, 2015

@author: soroosh
'''
fannou = None

def openAnnounce(outputdir):
    global fannou 
    fannou = open(outputdir + '/Output.txt', 'w+')
    
def closeAnnounce():
    global fannou 
    fannou.close()

def Announce(text):
    global fannou 
    print text
    fannou.write(str(text) + '\r\n')
    fannou.flush()
    
def Percent(final):
    print '.'
    
    
def LogIt(text):
    pass