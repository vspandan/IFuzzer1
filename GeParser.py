from gparser.GenerateLexInput import *
from gparser.GenerateBisonInput import *

from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory


Tk().withdraw()
filename = askopenfilename() 

genLexInput =  GenerateLexInput()
genLexInput.setSelectedGrammar(filename)
genLexInput.createLexInput()

genBisonInput = GenerateBisonInput()
genBisonInput.createBisonInput(filename)


Tk().withdraw()
INPUT_FOLDER = askdirectory()


f = open('.Properties1',WRITE)
f.write(INPUT_FOLDER)
f.close()

f = open('.Properties2',WRITE)
f.write(filename)
f.close()


