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

from pyneurgen.fitness import FitnessElites, FitnessTournament
from pyneurgen.fitness import ReplacementTournament, MAX, MIN, CENTER
from pyneurgen.grammatical_evolution import GrammaticalEvolution


#Author: Spandan Veggalam
class GECodeGen(object):
    
    #Author: Spandan Veggalam
    def __init__(self):
        root = Tk()
        root.title("Interpreter Fuzzer")
        root.geometry("800x400+30+30")
        self.frame = Frame(root)        
        self.frame.pack(side="top", fill="both", expand=True)
        
        label1= Label(self.frame,text="Grammar File", width=20).grid(row = 0,column=0)
        self.e = StringVar()
        self.inputFile = Entry(self.frame, textvariable=self.e,width=30)
        self.inputFile.insert(0, "grammarFiles/JavaScript1.g4")
        self.inputFile.config(state=DISABLED)
        self.inputFile.grid(row=0, column=1)
        browseBtn=Button(self.frame, text='Browse', command=self.selectGrammarFIle,width=10,state=DISABLED).grid(row=0, column=3)
        
        
        label= Label(self.frame,text="GENOTYPE PARAMETERS")
        label.grid(row = 3)       
        
        
        label2= Label(self.frame,text="Start Gene Length",width=15).grid(row = 5)
        self.start_gene_length=Entry(self.frame,width=20)
        self.start_gene_length.insert(0,"20")
        self.start_gene_length.grid(row=5,column=1)
        
        label3= Label(self.frame,text="Max Gene Length",width=15).grid(row = 6)
        self.max_gene_length=Entry(self.frame,width=20)
        self.max_gene_length.insert(0,"5000")
        self.max_gene_length.grid(row=6,column=1)
        
        label4= Label(self.frame,text="Population Size",width=15).grid(row = 7)
        self.population_size=Entry(self.frame,width=20)
        self.population_size.insert(0,"5")
        self.population_size.grid(row=7,column=1)
        
        label5= Label(self.frame,text="Wrap",width=15).grid(row = 5,column =2)
        self.wrap=BooleanVar()
        self.wrapRB1=Radiobutton(self.frame,text="True",variable=self.wrap, value="True", width=5,anchor=W)
        self.wrapRB2=Radiobutton(self.frame,text="False",variable=self.wrap,value="False", width=5,anchor=W)        
        self.wrapRB1.grid(row=5,column=3)
        self.wrapRB2.grid(row=5,column=4)
        self.wrapRB1.select()
        
        
        label6= Label(self.frame,text="Generations",width=15).grid(row = 6,column=2)
        self.set_max_generations=Entry(self.frame,width=20)
        self.set_max_generations.insert(0,"10")
        self.set_max_generations.grid(row=6,column=3)
        
        label7= Label(self.frame,text="Max Program Length",width=15).grid(row = 7,column=2)
        self.set_max_program_length=Entry(self.frame,width=20)
        self.set_max_program_length.insert(0,"500")
        self.set_max_program_length.grid(row=7,column=3)
        
        label8= Label(self.frame,text="Fitness Type",width=15).grid(row = 8,column=0)
        OPTIONS = ["MIN",    "MAX",    "CENTER"]
        self.variable = StringVar()
        self.variable.set(OPTIONS[0])
        self.fitness_type = OptionMenu(self.frame, self.variable,*OPTIONS)
        self.fitness_type.grid(row=8, column=1)
        
        label9= Label(self.frame,text="Fitness Target",width=15).grid(row = 8,column=2)
        self.set_fitness_traget_val=Entry(self.frame,width=20)
        self.set_fitness_traget_val.insert(0,"0.0001")
        self.set_fitness_traget_val.grid(row=8,column=3)
        
        label10= Label(self.frame,text="Min Time Out",width=15).grid(row = 9,column=0)
        self.set_min_timeout=Entry(self.frame,width=20)
        self.set_min_timeout.insert(0,"20")
        self.set_min_timeout.grid(row=9,column=1)
        
        label11= Label(self.frame,text="Max Time Out",width=15).grid(row = 9,column=2)
        self.set_max_timeout=Entry(self.frame,width=20)
        self.set_max_timeout.insert(0,"3600")
        self.set_max_timeout.grid(row=9,column=3)
        
        label12= Label(self.frame,text="Fitness Fail",width=15).grid(row = 10,column=0)
        self.set_fitness_failvalue=Entry(self.frame,width=20)
        self.set_fitness_failvalue.insert(0,"1000")
        self.set_fitness_failvalue.grid(row=10,column=1)
        
        label13= Label(self.frame,text="Max Fitness Rate",width=15).grid(row = 10,column=2)
        self.set_max_fitness_rate=Entry(self.frame,width=20)
        self.set_max_fitness_rate.insert(0,"0.5")
        self.set_max_fitness_rate.grid(row=10,column=3)

        label14= Label(self.frame,text="Mutation Rate",width=15).grid(row = 11,column=0)
        self.set_mutation_rate=Entry(self.frame,width=20)
        self.set_mutation_rate.insert(0,"0.02")
        self.set_mutation_rate.grid(row=11,column=1)
        
        label15= Label(self.frame,text="Crossover Rate",width=15).grid(row = 11,column=2)
        self.set_crossover_rate=Entry(self.frame,width=20)
        self.set_crossover_rate.insert(0,"0.2")
        self.set_crossover_rate.grid(row=11,column=3)
        
        label16= Label(self.frame,text="Mutation Type",width=15).grid(row = 12,column=0)
        OPTIONS = ["SINGLE",    "MULTIPLE"]
        self.variable1 = StringVar()
        self.variable1.set(OPTIONS[0])
        self.set_mutation_type = OptionMenu(self.frame, self.variable1,*OPTIONS)        
        self.set_mutation_type.grid(row=12,column=1)
        
        label17= Label(self.frame,text="Child(per Crossover)",width=15).grid(row = 12,column=2)
        self.set_children_per_crossover=Entry(self.frame,width=20)
        self.set_children_per_crossover.insert(0,"2")
        self.set_children_per_crossover.grid(row=12,column=3)
        
        label18= Label(self.frame,text="Fitness Selections",width=15).grid(row = 13,column=0)
        OPTIONSF = ["None"]
        self.variable2 = StringVar()
        self.variable2.set(OPTIONSF[0])
        self.set_fitness_selections= OptionMenu(self.frame, self.variable1,*OPTIONSF)
        self.set_fitness_selections.grid(row=13,column=1)        
        
        label19= Label(self.frame,text="Tournament Size(F)",width=15).grid(row = 13,column=2)
        self.set_fitness_tournmant_size=Entry(self.frame,width=20)
        self.set_fitness_tournmant_size.insert(0,"2")
        self.set_fitness_tournmant_size.grid(row=13,column=3)
        
        label20= Label(self.frame,text="Replacement Selections",width=15).grid(row = 14,column=0)
        OPTIONSR = ["None"]
        self.variable3 = StringVar()
        self.variable3.set(OPTIONSR[0])
        
        self.set_replacement_selections= OptionMenu(self.frame, self.variable1,*OPTIONSR)
        self.set_replacement_selections.grid(row=14,column=1)        
                
        label21= Label(self.frame,text="Tournament Size(R)",width=15).grid(row = 14,column=2)
        self.set_replacement_tournmant_size=Entry(self.frame,width=20)
        self.set_replacement_tournmant_size.insert(0,"3")
        self.set_replacement_tournmant_size.grid(row=14,column=3)
        
        
        frame1=Frame(self.frame)
        frame1.grid(row = 15,column =0, columnspan=2)
        label22= Label(frame1,text="Maintain History",width=15).grid(row = 0,column =0)
        self.maintain_history=BooleanVar()
        self.wrapRB1=Radiobutton(frame1,text="True",variable=self.maintain_history, value="True", width=5,anchor=W)
        self.wrapRB2=Radiobutton(frame1,text="False",variable=self.maintain_history,value="False", width=5,anchor=W)        
        self.wrapRB1.grid(row=0,column=1)
        self.wrapRB2.grid(row=0,column=2)
        self.wrapRB1.select()
        
        frame2=Frame(self.frame)
        frame2.grid(row = 15,column =2,columnspan=2)
        label23= Label(frame2,text="Extend Genotype",width=15).grid(row = 0,column =0)
        self.extend_genotype=BooleanVar()
        self.wrapRB1=Radiobutton(frame2,text="True",variable=self.extend_genotype, value="True", width=5,anchor=W)
        self.wrapRB2=Radiobutton(frame2,text="False",variable=self.extend_genotype,value="False", width=5,anchor=W)        
        self.wrapRB1.grid(row=0,column=1)
        self.wrapRB2.grid(row=0,column=2)
        self.wrapRB1.select()
        
        startBtn=Button(self.frame, text='START', command=self.initialize).grid(row=18, column=1)
        closeBtn=Button(self.frame, text='EXIT', command=self.frame.quit).grid(row=18, column=2)
        self.frame.mainloop()        
    
    #Author: Spandan Veggalam
    def selectGrammarFIle(self):
        Tk().withdraw()        
        self.e.set(askopenfilename())        
    
    #Author: Spandan Veggalam
    def initialize(self):
        
        try:
            bnf=""
            fileName=self.inputFile.get()
            if len(fileName.strip()) <=0:
                raise StandardError("Input Grammar File");
            else:
                ges = GrammaticalEvolution()
                ges.setGrammarFile(fileName)
                ges.set_bnf(bnf)
                ges.set_genotype_length(int(self.start_gene_length.get()), int(self.max_gene_length.get()))
                ges.set_population_size(long(self.population_size.get()))
                ges.set_wrap(bool(self.wrap.get()))
                ges.set_max_generations(int(self.set_max_generations.get()))
                ges.set_fitness_type(self.variable.get().lower(), float(self.set_fitness_traget_val.get()))
                
                ges.set_max_program_length(int(self.set_max_program_length.get()))
                ges.set_timeouts(int(self.set_min_timeout.get()), int(self.set_max_timeout.get()))
                ges.set_fitness_fail(float(self.set_fitness_failvalue.get()))
                
                ges.set_mutation_rate(float(self.set_mutation_rate.get()))
                
                ges.set_fitness_selections(
                    FitnessElites(ges.fitness_list, .05),
                    FitnessTournament(ges.fitness_list, tournament_size=int(self.set_fitness_tournmant_size.get())))
                ges.set_max_fitness_rate(float(self.set_max_fitness_rate.get()))
                
                ges.set_crossover_rate(float(self.set_crossover_rate.get()))
                ges.set_children_per_crossover(int(self.set_children_per_crossover.get()))
                
                if self.variable1.get() == "SINGLE":           
                    ges.set_mutation_type('s')
                if self.variable1.get() == "MULTIPLE":           
                    ges.set_mutation_type('m')
                
                ges.set_max_fitness_rate(float(self.set_max_fitness_rate.get()))
                
                ges.set_replacement_selections(
                        ReplacementTournament(ges.fitness_list, tournament_size=int(self.set_replacement_tournmant_size.get())))
                
                ges.set_maintain_history(self.maintain_history.get())
                ges.set_extend_genotype(self.extend_genotype.get())
                
                if ges.create_genotypes():
                    ges.run()
                    print ges.fitness_list.sorted()
                    gene = ges.population[ges.fitness_list.best_member()]
                    print gene.get_program()
                self.frame.quit()
                
            
        except AttributeError as e:
            print e

#Author: Spandan Veggalam 
if __name__ == "__main__":
    GECodeGen()
        
    
    
