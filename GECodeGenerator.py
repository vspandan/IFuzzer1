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
from random import randint

FILECOUNT = 0

Population_size=10
Timeout = 5
Generations=3


#Author: Spandan Veggalam
def runFuzzer(TestCases,targetDirectory,interpreter,options,excludeFiles,nTInvlvdGenProcess):
    def selectGrammarFIle():
        Tk().withdraw()        
        e.set(askopenfilename())   
    
    #Author: Spandan Veggalam
    def initialize():
        FileList=[]
        def process(fil,filecount):
                bnf=""
                ges = GrammaticalEvolution()
                ges.setGrammarFile(abspath("grammarFiles/JavaScript.g4"))
                ges.set_bnf(bnf)
                ges.set_genotype_length(20, 5000)
                ges.set_population_size(Population_size)
                ges.set_wrap(True)
                ges.set_max_generations(Generations)
                ges.set_fitness_type("min".lower(), float(-1000))
                
                ges.set_max_program_length(500)
                ges.set_timeouts(20, 3600)
                ges.set_fitness_fail(float(1000))
                
                ges.set_execution_timeout(Timeout)
                
                ges.set_fitness_selections(
                    FitnessElites(ges.fitness_list, 0.4))
                
                ges.set_crossover_rate(float(0.4))
                ges.set_mutation_rate(float(0.8))

                ges.set_max_depth(2)
                ges.set_generative_mutation_rate(0.2)

                ges.set_children_per_crossover(2)
                
                ges.set_mutation_type('s')

                ges.set_mutation_count(1);
                ges.set_crossover_count(1);
                #ges.set_multiple_rate(float(0.4))

                ges.set_max_fitness_rate(float(1.0))
                
                ges.set_replacement_selections(
                        ReplacementTournament(ges.fitness_list, tournament_size=3))
                
                ges.set_maintain_history(True)
                ges.set_extend_genotype(True)
                
                ges.dynamic_mutation_rate(1)
                ges.dynamic_crossover_rate(1)
                
                # print fil
                

                if ges.create_genotypes(fil,interpreter,options,nTInvlvdGenProcess):
                    ges.run()
                    # index=ges.run()
                    # print index
                    # gene = ges.population[index]
                    for gene in ges.population:
                        print gene.get_program()
                        if gene.get_fitness() != gene.get_fitness_fail() :
                            generatedPrg= gene.get_program()
                            newFile=targetDirectory+"/"+str(filecount)+".js"
                            filecount+=1
                            FileList.append(newFile)
                            f=open(newFile,'w')
                            f.write(generatedPrg)
                            f.close
            
        count=0
        total=len(TestCases)-1
        while True:
            tempList=[]
            FILECOUNT = len(listdir(targetDirectory))+1 
            if FILECOUNT > 2000:
                print FileList
                return FileList
            while len(tempList)<Population_size:
                t=TestCases[randint(0,total)]
                if t not in tempList:
                    tempList.append(t)
            from multiprocessing import Process
            print "File Set - "+str(count)
            count+=1
            p=Process(target=process, kwargs={'fil':tempList,'filecount':FILECOUNT})
            p.start()
            p.join(Timeout * Generations * Population_size / 2)
            if p.is_alive():
                p.terminate()
    return initialize()
