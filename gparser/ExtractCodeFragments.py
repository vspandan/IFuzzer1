from os import listdir
from os.path import isfile, join
from AntlrParser import AntlrParser

class ExtractCodeFragments(AntlrParser):
    def __init__(self):
        self.parser=AntlrParser()
        self.parser.__init__()
        
        mypath="/home/spandan/"
        files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
        for f in files:
            print f
    def extractCodeFragments (self,directoryName):
        print self.parser.parseTree("var a=function (x,y){x=10000+this.y;};")
        print directoryName
    def extractSubCodeFrag(self,nonTerminal,position):
        print nonTerminal
        
if __name__=='__main__':
    e=ExtractCodeFragments()
    