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

f = open('.Properties2',WRITE)
f.write(filename)
f.close()


