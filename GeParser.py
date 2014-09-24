from gparser.GenerateLexInput import *
from gparser.GenerateBisonInput import *

from Tkinter import Tk
from tkFileDialog import askopenfilename


Tk().withdraw()
filename = askopenfilename() 

genLexInput =  GenerateLexInput()
genLexInput.setSelectedGrammar(filename)
genLexInput.createLexInput()

genBisonInput = GenerateBisonInput()
genBisonInput.createBisonInput(filename)


