from posix import listdir
from marshal import load
from os.path import abspath
if __name__=='__main__':
    print 
    st='database'
    f = open(st+"/argumentList", 'r')
    dictOfDict1 = load(f)
    for i in dictOfDict1:
    	print i
    
      
