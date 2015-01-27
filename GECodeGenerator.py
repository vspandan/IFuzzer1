#!/usr/bin/env python

from Tix import ROW
from Tkconstants import DISABLED, NORMAL
from Tkinter import BooleanVar, Checkbutton, IntVar
from Tkinter import Button
from Tkinter import Entry
from Tkinter import Frame
from Tkinter import Label
from Tkinter import OptionMenu
from Tkinter import Radiobutton
from Tkinter import StringVar
from Tkinter import Tk
from Tkinter import W
from os import listdir
from os import system
from os.path import isfile, join, abspath, sys
from posix import mkdir
from tkFileDialog import askdirectory
from tkFileDialog import askopenfilename
from tkMessageBox import showerror

from codegen.fitness import FitnessElites, FitnessTournament
from codegen.fitness import ReplacementTournament, MAX, MIN, CENTER
from codegen.GrammaticalEvolution import GrammaticalEvolution
import threading
from datetime import datetime
import multiprocessing
import os

FILECOUNT = 0
EXCLUDED = set(('browser.js', 'shell.js', 'jsref.js', 'template.js',
                    'user.js', 'sta.js',
                    'test262-browser.js', 'test262-shell.js',
                    'test402-browser.js', 'test402-shell.js',
                    'testBuiltInObject.js', 'testIntl.js',
                    'js-test-driver-begin.js', 'js-test-driver-end.js'))

TestCaseSubDirs=[]
GENERATEDFILELIST=[]
#Author: Spandan Veggalam
def runFuzzer(testCasesDir,targetDirectory):
    listAllTestCasesDir(testCasesDir)
    FILECOUNT = len(os.listdir(targetDirectory))    
    def selectGrammarFIle():
        Tk().withdraw()        
        e.set(askopenfilename())   
    
    
    
    #Author: Spandan Veggalam
    def initialize():
        FILECOUNT = len(os.listdir(targetDirectory))
        def process(file,filName):
            try:
                bnf=""
                fileName=inputFile.get()
                if len(fileName.strip()) <=0:
                    raise StandardError("Input Grammar File");
                else:
                    ges = GrammaticalEvolution()
                    ges.setGrammarFile(fileName)
                    ges.set_bnf(bnf)
                    ges.set_genotype_length(int(start_gene_length.get()), int(max_gene_length.get()))
                    ges.set_population_size(long(population_size.get()))
                    ges.set_wrap(bool(wrap.get()))
                    ges.set_max_generations(int(set_max_generations.get()))
                    ges.set_fitness_type(variable.get().lower(), float(set_fitness_traget_val.get()))
                    
                    ges.set_max_program_length(int(set_max_program_length.get()))
                    ges.set_timeouts(int(set_min_timeout.get()), int(set_max_timeout.get()))
                    ges.set_fitness_fail(float(set_fitness_failvalue.get()))
                    
                    ges.set_mutation_rate(float(set_mutation_rate.get()))
                    
                    ges.set_fitness_selections(
                        FitnessElites(ges.fitness_list, .05),
                        FitnessTournament(ges.fitness_list, tournament_size=int(set_fitness_tournmant_size.get())))
                    ges.set_max_fitness_rate(float(set_max_fitness_rate.get()))
                    
                    ges.set_crossover_rate(float(set_crossover_rate.get()))
                    ges.set_children_per_crossover(int(set_children_per_crossover.get()))
                    
                    if variable1.get() == "SINGLE":           
                        ges.set_mutation_type('s')
                    if variable1.get() == "MULTIPLE":           
                        ges.set_mutation_type('m')
                    
                    ges.set_max_fitness_rate(float(set_max_fitness_rate.get()))
                    
                    ges.set_replacement_selections(
                            ReplacementTournament(ges.fitness_list, tournament_size=int(set_replacement_tournmant_size.get())))
                    
                    ges.set_maintain_history(maintain_history.get())
                    ges.set_extend_genotype(extend_genotype.get())
                    
                    ges.dynamic_mutation_rate(dynM.get())
                    ges.dynamic_crossover_rate(dynM1.get())
                    
                       
                    try:  
                        print "Processing ::" + file
                        if ges.create_genotypes(file):
                            ges.run()
                            ges.fitness_list.sorted()
                            gene = ges.population[ges.fitness_list.best_member()]
                            generatedPrg= gene.get_program()
                            newFile=targetDirectory+"/"+str(filName)
                            GENERATEDFILELIST.append(newFile)
                            f=open(newFile,'w')
                            f.write(generatedPrg)
                            f.close
                            
                    except Exception as e:
                        print "Skipping "+file+" due to exception while processing"
                        print e
    
            except AttributeError as e:
                print e
                
        for subDir in TestCaseSubDirs :
            PROCESSLIST=[]
            for f in listdir(subDir) :
                fi=join(subDir,f)
                if isfile(fi):
                    if f.endswith(".js") and f not in EXCLUDED :
                        process(fi,FILECOUNT)
                        #p=multiprocessing.Process(target=process,args=(fi, f))
                        #p=threading.Thread(target=process,args=(fi, f))
                        #PROCESSLIST.append(p)
                        #frame.quit()
                        #return             
        frame.quit()
        return GENERATEDFILELIST
        
    root = Tk()
    root.title("Interpreter Fuzzer")
    root.geometry("900x400+30+30")
    frame = Frame(root)        
    frame.pack(side="top", fill="both", expand=True)
    
    label1= Label(frame,text="Grammar File", width=20).grid(row = 0,column=0)
    e = StringVar()
    inputFile = Entry(frame, textvariable=e,width=30)
    inputFile.insert(0, abspath("../grammarFiles/JavaScript.g4"))
    inputFile.config(state=DISABLED)
    inputFile.grid(row=0, column=1)
    browseBtn=Button(frame, text='Browse', command=selectGrammarFIle,width=10,state=DISABLED).grid(row=0, column=3)
    
    
    label= Label(frame,text="GENOTYPE PARAMETERS")
    label.grid(row = 3)       
    
    
    label2= Label(frame,text="Start Gene Length",width=25).grid(row = 5)
    start_gene_length=Entry(frame,width=20)
    start_gene_length.insert(0,"20")
    start_gene_length.grid(row=5,column=1)
    
    label3= Label(frame,text="Max Gene Length",width=25).grid(row = 6)
    max_gene_length=Entry(frame,width=20)
    max_gene_length.insert(0,"5000")
    max_gene_length.grid(row=6,column=1)
    
    label4= Label(frame,text="Population Size",width=25).grid(row = 7)
    population_size=Entry(frame,width=20)
    population_size.insert(0,"5")
    population_size.grid(row=7,column=1)
    
    label5= Label(frame,text="Wrap",width=25).grid(row = 5,column =2)
    wrap=BooleanVar()
    wrapRB1=Radiobutton(frame,text="True",variable=wrap, value="True", width=5,anchor=W)
    wrapRB2=Radiobutton(frame,text="False",variable=wrap,value="False", width=5,anchor=W)        
    wrapRB1.grid(row=5,column=3)
    wrapRB2.grid(row=5,column=4)
    wrapRB1.select()
    
    
    label6= Label(frame,text="Generations",width=25).grid(row = 6,column=2)
    set_max_generations=Entry(frame,width=20)
    set_max_generations.insert(0,"2")
    set_max_generations.grid(row=6,column=3)
    
    label7= Label(frame,text="Max Program Length",width=25).grid(row = 7,column=2)
    set_max_program_length=Entry(frame,width=20)
    set_max_program_length.insert(0,"500")
    set_max_program_length.grid(row=7,column=3)
    set_max_program_length.config(state=DISABLED)
    
    label8= Label(frame,text="Fitness Type",width=25).grid(row = 8,column=0)
    OPTIONS = ["MIN",    "MAX",    "CENTER"]
    variable = StringVar()
    variable.set(OPTIONS[0])
    fitness_type = OptionMenu(frame, variable,*OPTIONS)
    fitness_type.grid(row=8, column=1)
    
    label9= Label(frame,text="Fitness Target",width=25).grid(row = 8,column=2)
    set_fitness_traget_val=Entry(frame,width=20)
    set_fitness_traget_val.insert(0,"0.0001")
    set_fitness_traget_val.grid(row=8,column=3)
    
    label10= Label(frame,text="Min Time Out",width=25).grid(row = 9,column=0)
    set_min_timeout=Entry(frame,width=20)
    set_min_timeout.insert(0,"20")
    set_min_timeout.grid(row=9,column=1)
    
    label11= Label(frame,text="Max Time Out",width=25).grid(row = 9,column=2)
    set_max_timeout=Entry(frame,width=20)
    set_max_timeout.insert(0,"3600")
    set_max_timeout.grid(row=9,column=3)
    
    label12= Label(frame,text="Fitness Fail",width=25).grid(row = 10,column=0)
    set_fitness_failvalue=Entry(frame,width=20)
    set_fitness_failvalue.insert(0,"1000")
    set_fitness_failvalue.grid(row=10,column=1)
    
    label13= Label(frame,text="Max Fitness Rate",width=25).grid(row = 10,column=2)
    set_max_fitness_rate=Entry(frame,width=20)
    set_max_fitness_rate.insert(0,"0.5")
    set_max_fitness_rate.grid(row=10,column=3)

    def disableMutationRateEntry():
        if set_mutation_rate.cget('state') == 'disabled':
            set_mutation_rate.config(state=NORMAL)
        else:
            set_mutation_rate.config(state=DISABLED)
            
    label14_1 = Label(frame,text="Dynamic Mutation Rate",width=25).grid(row = 11,column=0)
    dynM=IntVar()
    c1 = Checkbutton(frame, text="",command=disableMutationRateEntry,variable=dynM,onvalue=1, offvalue=0)
    c1.grid(row=11,column=1)
    c1.select()
    
    label14_2 = Label(frame,text="Mutation Rate",width=25).grid(row = 12,column=0)
    set_mutation_rate=Entry(frame,width=20)
    set_mutation_rate.insert(0,"0.02")
    set_mutation_rate.grid(row=12,column=1)
    set_mutation_rate.config(state=DISABLED)
    
    def disableCrossoverRateEntry():
        if set_crossover_rate.cget('state') == 'disabled':
            set_crossover_rate.config(state=NORMAL)
        else:
            set_crossover_rate.config(state=DISABLED)
        
    label15_1= Label(frame,text="Dynamic Crossover Rate",width=25).grid(row = 11,column=2)
    dynM1=IntVar()
    c2 = Checkbutton(frame, text="",command=disableCrossoverRateEntry,variable=dynM1)
    c2.grid(row=11,column=3)
    c2.select()
    
    label15_2= Label(frame,text="Crossover Rate",width=25).grid(row = 12,column=2)
    set_crossover_rate=Entry(frame,width=20)
    set_crossover_rate.insert(0,"0.2")
    set_crossover_rate.grid(row=12,column=3)
    set_crossover_rate.config(state=DISABLED)
    
    label16= Label(frame,text="Mutation Type",width=25).grid(row = 13,column=0)
    OPTIONS = ["SINGLE",    "MULTIPLE"]
    variable1 = StringVar()
    variable1.set(OPTIONS[0])
    set_mutation_type = OptionMenu(frame, variable1,*OPTIONS)        
    set_mutation_type.grid(row=13,column=1)
    
    label17= Label(frame,text="Child(per Crossover)",width=25).grid(row = 13,column=2)
    set_children_per_crossover=Entry(frame,width=20)
    set_children_per_crossover.insert(0,"2")
    set_children_per_crossover.grid(row=13,column=3)
    
    label18= Label(frame,text="Fitness Selections",width=25).grid(row = 14,column=0)
    OPTIONSF = ["None"]
    variable2 = StringVar()
    variable2.set(OPTIONSF[0])
    set_fitness_selections= OptionMenu(frame, variable1,*OPTIONSF)
    set_fitness_selections.grid(row=14,column=1)        
    
    label19= Label(frame,text="Tournament Size(F)",width=25).grid(row = 14,column=2)
    set_fitness_tournmant_size=Entry(frame,width=20)
    set_fitness_tournmant_size.insert(0,"2")
    set_fitness_tournmant_size.grid(row=14,column=3)
    
    label20= Label(frame,text="Replacement Selections",width=25).grid(row = 15,column=0)
    OPTIONSR = ["None"]
    variable3 = StringVar()
    variable3.set(OPTIONSR[0])
    
    set_replacement_selections= OptionMenu(frame, variable1,*OPTIONSR)
    set_replacement_selections.grid(row=15,column=1)        
            
    label21= Label(frame,text="Tournament Size(R)",width=25).grid(row = 15,column=2)
    set_replacement_tournmant_size=Entry(frame,width=20)
    set_replacement_tournmant_size.insert(0,"3")
    set_replacement_tournmant_size.grid(row=15,column=3)
    
    
    frame1=Frame(frame)
    frame1.grid(row = 16,column =0, columnspan=2)
    label22= Label(frame1,text="Maintain History",width=25).grid(row = 0,column =0)
    maintain_history=BooleanVar()
    wrapRB1=Radiobutton(frame1,text="True",variable=maintain_history, value="True", width=5,anchor=W)
    wrapRB2=Radiobutton(frame1,text="False",variable=maintain_history,value="False", width=5,anchor=W)        
    wrapRB1.grid(row=0,column=1)
    wrapRB2.grid(row=0,column=2)
    wrapRB1.select()
    
    frame2=Frame(frame)
    frame2.grid(row = 16,column =2,columnspan=2)
    label23= Label(frame2,text="Extend Genotype",width=25).grid(row = 0,column =0)
    extend_genotype=BooleanVar()
    wrapRB1=Radiobutton(frame2,text="True",variable=extend_genotype, value="True", width=5,anchor=W)
    wrapRB2=Radiobutton(frame2,text="False",variable=extend_genotype,value="False", width=5,anchor=W)        
    wrapRB1.grid(row=0,column=1)
    wrapRB2.grid(row=0,column=2)
    wrapRB1.select()
    
    startBtn=Button(frame, text='START', command=initialize).grid(row=18, column=1)
    closeBtn=Button(frame, text='EXIT', command=frame.quit).grid(row=18, column=2)
    frame.mainloop()    
    return GENERATEDFILELIST    
def listAllTestCasesDir(testCasesDir):
        for f in listdir(testCasesDir):
            fi=join(testCasesDir,f)
            if not isfile(fi):
                TestCaseSubDirs.append(fi)
                listAllTestCasesDir(fi)
        
        
        