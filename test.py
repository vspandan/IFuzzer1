from posix import listdir
from pickle import load
from os.path import abspath
if __name__=='__main__':
    print 
    st='database'
    for fil in listdir(st):
        f = open(st+"/"+fil, 'r')
        dictOfDict1 = load(f)
        print fil+":"+str(len(dictOfDict1))
        raw_input("Press any key to continue")
        print dictOfDict1

      
