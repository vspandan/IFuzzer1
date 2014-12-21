#!/usr/bin/env python

from Tix import ROW
from Tkconstants import DISABLED
from Tkinter import BooleanVar
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
from os.path import isfile, join
from posix import mkdir
from tkFileDialog import askdirectory
from tkFileDialog import askopenfilename
from tkMessageBox import showerror

from codegen.fitness import FitnessElites, FitnessTournament
from codegen.fitness import ReplacementTournament, MAX, MIN, CENTER
from codegen.GrammaticalEvolution import GrammaticalEvolution
from mozillaJSTestSuite.jstests import main

JS_SHELL_PATH="/home/spandan/js-1.8.5/js/src/dist/bin/js"
CREATE_FRAG_POOL=False

#Author: Spandan Veggalam
def start():
    
    def selectGrammarFIle():
        Tk().withdraw()        
        e.set(askopenfilename())        
    
    #Author: Spandan Veggalam
    def initialize():
        
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
                
                if ges.create_genotypes():
                    ges.run()
                    print ges.fitness_list.sorted()
                    gene = ges.population[ges.fitness_list.best_member()]
                    print gene.get_program()
                frame.quit()
                
            
        except AttributeError as e:
            print e
    #CREATE_FRAG_POOL=True
    main(JS_SHELL_PATH,CREATE_FRAG_POOL)
    
    root = Tk()
    root.title("Interpreter Fuzzer")
    root.geometry("800x400+30+30")
    frame = Frame(root)        
    frame.pack(side="top", fill="both", expand=True)
    
    label1= Label(frame,text="Grammar File", width=20).grid(row = 0,column=0)
    e = StringVar()
    inputFile = Entry(frame, textvariable=e,width=30)
    inputFile.insert(0, "grammarFiles/JavaScript.g4")
    inputFile.config(state=DISABLED)
    inputFile.grid(row=0, column=1)
    browseBtn=Button(frame, text='Browse', command=selectGrammarFIle,width=10,state=DISABLED).grid(row=0, column=3)
    
    
    label= Label(frame,text="GENOTYPE PARAMETERS")
    label.grid(row = 3)       
    
    
    label2= Label(frame,text="Start Gene Length",width=15).grid(row = 5)
    start_gene_length=Entry(frame,width=20)
    start_gene_length.insert(0,"20")
    start_gene_length.grid(row=5,column=1)
    
    label3= Label(frame,text="Max Gene Length",width=15).grid(row = 6)
    max_gene_length=Entry(frame,width=20)
    max_gene_length.insert(0,"5000")
    max_gene_length.grid(row=6,column=1)
    
    label4= Label(frame,text="Population Size",width=15).grid(row = 7)
    population_size=Entry(frame,width=20)
    population_size.insert(0,"5")
    population_size.grid(row=7,column=1)
    
    label5= Label(frame,text="Wrap",width=15).grid(row = 5,column =2)
    wrap=BooleanVar()
    wrapRB1=Radiobutton(frame,text="True",variable=wrap, value="True", width=5,anchor=W)
    wrapRB2=Radiobutton(frame,text="False",variable=wrap,value="False", width=5,anchor=W)        
    wrapRB1.grid(row=5,column=3)
    wrapRB2.grid(row=5,column=4)
    wrapRB1.select()
    
    
    label6= Label(frame,text="Generations",width=15).grid(row = 6,column=2)
    set_max_generations=Entry(frame,width=20)
    set_max_generations.insert(0,"10")
    set_max_generations.grid(row=6,column=3)
    
    label7= Label(frame,text="Max Program Length",width=15).grid(row = 7,column=2)
    set_max_program_length=Entry(frame,width=20)
    set_max_program_length.insert(0,"500")
    set_max_program_length.grid(row=7,column=3)
    
    label8= Label(frame,text="Fitness Type",width=15).grid(row = 8,column=0)
    OPTIONS = ["MIN",    "MAX",    "CENTER"]
    variable = StringVar()
    variable.set(OPTIONS[0])
    fitness_type = OptionMenu(frame, variable,*OPTIONS)
    fitness_type.grid(row=8, column=1)
    
    label9= Label(frame,text="Fitness Target",width=15).grid(row = 8,column=2)
    set_fitness_traget_val=Entry(frame,width=20)
    set_fitness_traget_val.insert(0,"0.0001")
    set_fitness_traget_val.grid(row=8,column=3)
    
    label10= Label(frame,text="Min Time Out",width=15).grid(row = 9,column=0)
    set_min_timeout=Entry(frame,width=20)
    set_min_timeout.insert(0,"20")
    set_min_timeout.grid(row=9,column=1)
    
    label11= Label(frame,text="Max Time Out",width=15).grid(row = 9,column=2)
    set_max_timeout=Entry(frame,width=20)
    set_max_timeout.insert(0,"3600")
    set_max_timeout.grid(row=9,column=3)
    
    label12= Label(frame,text="Fitness Fail",width=15).grid(row = 10,column=0)
    set_fitness_failvalue=Entry(frame,width=20)
    set_fitness_failvalue.insert(0,"1000")
    set_fitness_failvalue.grid(row=10,column=1)
    
    label13= Label(frame,text="Max Fitness Rate",width=15).grid(row = 10,column=2)
    set_max_fitness_rate=Entry(frame,width=20)
    set_max_fitness_rate.insert(0,"0.5")
    set_max_fitness_rate.grid(row=10,column=3)

    label14= Label(frame,text="Mutation Rate",width=15).grid(row = 11,column=0)
    set_mutation_rate=Entry(frame,width=20)
    set_mutation_rate.insert(0,"0.02")
    set_mutation_rate.grid(row=11,column=1)
    
    label15= Label(frame,text="Crossover Rate",width=15).grid(row = 11,column=2)
    set_crossover_rate=Entry(frame,width=20)
    set_crossover_rate.insert(0,"0.2")
    set_crossover_rate.grid(row=11,column=3)
    
    label16= Label(frame,text="Mutation Type",width=15).grid(row = 12,column=0)
    OPTIONS = ["SINGLE",    "MULTIPLE"]
    variable1 = StringVar()
    variable1.set(OPTIONS[0])
    set_mutation_type = OptionMenu(frame, variable1,*OPTIONS)        
    set_mutation_type.grid(row=12,column=1)
    
    label17= Label(frame,text="Child(per Crossover)",width=15).grid(row = 12,column=2)
    set_children_per_crossover=Entry(frame,width=20)
    set_children_per_crossover.insert(0,"2")
    set_children_per_crossover.grid(row=12,column=3)
    
    label18= Label(frame,text="Fitness Selections",width=15).grid(row = 13,column=0)
    OPTIONSF = ["None"]
    variable2 = StringVar()
    variable2.set(OPTIONSF[0])
    set_fitness_selections= OptionMenu(frame, variable1,*OPTIONSF)
    set_fitness_selections.grid(row=13,column=1)        
    
    label19= Label(frame,text="Tournament Size(F)",width=15).grid(row = 13,column=2)
    set_fitness_tournmant_size=Entry(frame,width=20)
    set_fitness_tournmant_size.insert(0,"2")
    set_fitness_tournmant_size.grid(row=13,column=3)
    
    label20= Label(frame,text="Replacement Selections",width=15).grid(row = 14,column=0)
    OPTIONSR = ["None"]
    variable3 = StringVar()
    variable3.set(OPTIONSR[0])
    
    set_replacement_selections= OptionMenu(frame, variable1,*OPTIONSR)
    set_replacement_selections.grid(row=14,column=1)        
            
    label21= Label(frame,text="Tournament Size(R)",width=15).grid(row = 14,column=2)
    set_replacement_tournmant_size=Entry(frame,width=20)
    set_replacement_tournmant_size.insert(0,"3")
    set_replacement_tournmant_size.grid(row=14,column=3)
    
    
    frame1=Frame(frame)
    frame1.grid(row = 15,column =0, columnspan=2)
    label22= Label(frame1,text="Maintain History",width=15).grid(row = 0,column =0)
    maintain_history=BooleanVar()
    wrapRB1=Radiobutton(frame1,text="True",variable=maintain_history, value="True", width=5,anchor=W)
    wrapRB2=Radiobutton(frame1,text="False",variable=maintain_history,value="False", width=5,anchor=W)        
    wrapRB1.grid(row=0,column=1)
    wrapRB2.grid(row=0,column=2)
    wrapRB1.select()
    
    frame2=Frame(frame)
    frame2.grid(row = 15,column =2,columnspan=2)
    label23= Label(frame2,text="Extend Genotype",width=15).grid(row = 0,column =0)
    extend_genotype=BooleanVar()
    wrapRB1=Radiobutton(frame2,text="True",variable=extend_genotype, value="True", width=5,anchor=W)
    wrapRB2=Radiobutton(frame2,text="False",variable=extend_genotype,value="False", width=5,anchor=W)        
    wrapRB1.grid(row=0,column=1)
    wrapRB2.grid(row=0,column=2)
    wrapRB1.select()
    
    startBtn=Button(frame, text='START', command=initialize).grid(row=18, column=1)
    closeBtn=Button(frame, text='EXIT', command=frame.quit).grid(row=18, column=2)
    frame.mainloop()    
        
    
    
#Author: Spandan Veggalam 
if __name__ == "__main__":
    start()
        
    
    
