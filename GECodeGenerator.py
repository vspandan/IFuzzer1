#!/usr/bin/env python

from Tkconstants import DISABLED, NORMAL
from Tkinter import BooleanVar, Checkbutton, IntVar, Button, Entry, Frame, Label, OptionMenu, Radiobutton, StringVar, Tk, W
from os import listdir, system
from os.path import isfile, join, abspath, sys
from tkFileDialog import askdirectory, askopenfilename
from tkMessageBox import showerror

from codegen.fitness import FitnessElites, FitnessTournament
from codegen.fitness import ReplacementTournament, MAX, MIN, CENTER
from codegen.GrammaticalEvolution import GrammaticalEvolution

from langparser.AntlrParser import AntlrParser
from marshal import load,dump

FILECOUNT = 0

TestCaseSubDirs=[]
#Author: Spandan Veggalam
def runFuzzer(testCasesDir,targetDirectory,interpreter,options,excludeFiles,nTInvlvdGenProcess):
    listAllTestCasesDir(testCasesDir)   
    def selectGrammarFIle():
        Tk().withdraw()        
        e.set(askopenfilename())   
    
    #Author: Spandan Veggalam
    def initialize():
        def process(fil):
                bnf=""
                ges = GrammaticalEvolution()
                ges.setGrammarFile(abspath("grammarFiles/JavaScript.g4"))
                ges.set_bnf(bnf)
                ges.set_genotype_length(20, 5000)
                ges.set_population_size(10)
                ges.set_wrap(True)
                ges.set_max_generations(3)
                ges.set_fitness_type("min".lower(), float(-1000))
                
                ges.set_max_program_length(500)
                ges.set_timeouts(20, 3600)
                ges.set_fitness_fail(float(1000))
                
                ges.set_mutation_rate(float(0.5))
                
                ges.set_fitness_selections(
                    FitnessElites(ges.fitness_list, .05),
                    FitnessTournament(ges.fitness_list, tournament_size=2))
                ges.set_max_fitness_rate(float(0.2))
                
                ges.set_crossover_rate(float(0.4))
                ges.set_children_per_crossover(2)
                
                ges.set_mutation_type('s')
                
                ges.set_max_fitness_rate(float(0.5))
                
                ges.set_replacement_selections(
                        ReplacementTournament(ges.fitness_list, tournament_size=3))
                
                ges.set_maintain_history(True)
                ges.set_extend_genotype(True)
                
                ges.dynamic_mutation_rate(1)
                ges.dynamic_crossover_rate(1)
                
                print "Processing ::" + fil
                if ges.create_genotypes(fil,interpreter,options,nTInvlvdGenProcess):
                    gene = ges.population[ges.run()]
                    if gene.get_fitness() != gene.get_fitness_fail() :
                        FILECOUNT = len(listdir(targetDirectory))+1 
                        generatedPrg= gene.get_program()
                        print generatedPrg
                        newFile=targetDirectory+"/"+str(FILECOUNT)+".js"
                        f=open(newFile,'w')
                        f.write(generatedPrg)
                        f.close
                        """
                        a=AntlrParser()
                        codeFrags2 = a.extractCodeFrag_(generatedPrg)
                        for key in codeFrags2.keys():
                        	if key != 'arguments':
        						fileN = "database" + "/" + key
        						temp=[]
        						if isfile(fileN):
            						f2 = open(fileN, 'r')
            						temp=load(f2)
            						f2.close()
        						temp = temp + codeFrags2.get(key)
        						f1 = open(fileN, 'wb')
        						dump(temp, f1)
        						f1.close()
                        """
            
        #count=0
        for subDir in TestCaseSubDirs :
            for f in listdir(subDir) :
                fi=join(subDir,f)
                if isfile(fi) and f.endswith(".js") and f not in excludeFiles :
                    from multiprocessing import Process
                    f111=open("spandan.l","a+")
                    f111.write("\n\n\n\n\n"+f+"\n")
                    f111.close()
                    #count+=1
                    p=Process(target=process, kwargs={'fil':fi})
                    p.start()
                    p.join(10)
                    if p.is_alive():
                        p.terminate()
                #if count==10:
                    #sys.exit()
                    #print fi
    initialize()
    

def listAllTestCasesDir(testCasesDir):
        for f in listdir(testCasesDir):
            fi=join(testCasesDir,f)
            if not isfile(fi):
                TestCaseSubDirs.append(fi)
                listAllTestCasesDir(fi)