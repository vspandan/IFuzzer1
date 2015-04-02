#!/usr/bin/env python
from Tkconstants import INSERT
from Tkinter import Button, Frame, Tk, Text
from copy import deepcopy
from datetime import datetime
from os import path, system
from random import choice, randint, random
from re import sub
from tkFileDialog import askopenfilename
from tkMessageBox import askyesno, showwarning, showinfo, showerror

from langparser.AntlrParser import *
from codegen.fitness import CENTER, MAX, MIN
from codegen.fitness import FitnessList, Fitness, Replacement
from codegen.Genotypes import Genotype


STOPPING_MAX_GEN = 'max_generations'

class GrammaticalEvolution(object):

    def __init__(self):
        self._pre_selected = []
        self.history = []
        self.population = []
        self.parser = AntlrParser()
        self.initial_Population = []
        self.identifiers = []
        self.non_Terminals=[]
        self.stopping_criteria = {
                STOPPING_MAX_GEN: None
                }
        self.fitness_selections = []
        self.replacement_selections = []        
        
        self._crossover_rate = 0.4
        self._children_per_crossover = 2
        self._mutation_type = 's'
        self._mutation_rate = 0.02
        self._max_fitness_rate = 0.5

        self._wrap = True
        self._extend_genotype = True
        self._start_gene_length = None
        self._max_gene_length = None
        self._max_program_length = None

        self.fitness_list = FitnessList(CENTER)
        
        self._generation = 0
        self._fitness_fail = -1000
        self._maintain_history = True
        self._timeouts = [20,3600]

        self._bnf = {}
        self._population_size = 0
        
        self.dynamic_mutation = 0
        self.dynamic_crossover = 0

        self.mutationCount = 1
        self.crossoverCount = 1
        self.multiple_rate = 0
        self.fitness_list_history = []
        self._max_depth = 0
        self._generative_mutation_rate=0.5

    def set_max_depth(self,depth):
        self._max_depth=depth

    def set_generative_mutation_rate(self,rate):
        self._generative_mutation_rate=rate

	def set_multiple_rate(self, rate):
		self.multiple_rate = rate

    def set_crossover_count(self, count):
        self.crossoverCount=count

    def set_mutation_count(self, count):
        self.mutationCount=count

    def set_execution_timeout(self, timeout):
        self.execution_timeout = timeout

    def dynamic_mutation_rate(self, ind ):
        self.dynamic_mutation = ind
    
    def dynamic_crossover_rate(self, ind):
        self.dynamic_crossover = ind
    
    def setGrammarFile(self,fileName):
        self.grammarFile=fileName
    
    def _extractProductions(self):
        bnf=""        
        f = open(self.grammarFile,'r')
        for line in f:
            bnf+=line;
        f.close()        
        self.set_bnf(bnf)
    
    def parseCode(self,codeFragment):
        from time import time
        fi="/tmp/"+str(int(time()*1000))
        f=open(fi,"a")
        f.write(codeFragment)
        f.close()
        remove(fi)
        return self.parser.parseTree(codeFragment,True)
    
    def _prepareInitial_Population (self,fileList):
            self.identifiers=[]
            self.initial_Population=[]
            count=0
            for fileName in fileList:
                f=open(path.abspath(fileName),"r")
                self.initial_Population.append(f.read())

    def set_population_size(self, size):
        size = long(size)
        if isinstance(size, long) and size > 0:
            self._population_size = size
            i = len(self.fitness_list)
            while i < size:
                self.fitness_list.append([0.0, i])
                i += 1
        else:
            raise ValueError("""
                population size, %s, must be a long above 0""" % (size))

    def get_population_size(self):
        return self._population_size

    def set_genotype_length(self, start_gene_length,
                                    max_gene_length=None):
        if max_gene_length is None:
            max_gene_length = start_gene_length

        start_gene_length = long(start_gene_length)
        max_gene_length = long(max_gene_length)
        self._start_gene_length = start_gene_length
        self._max_gene_length = max_gene_length

    def get_genotype_length(self):
        return (self._start_gene_length, self._max_gene_length)

    def set_extend_genotype(self, true_false):
            self._extend_genotype = true_false

    def get_extend_genotype(self):
        return self._extend_genotype

    def set_wrap(self, true_false):
            self._wrap = true_false

    def get_wrap(self):
        return self._wrap
    
    def set_bnf(self, bnf):
        def strip_spaces(key, values):
            values = [value.strip()
                for value in values.split('|') if value]
            return values

        non_Terminals=[]

        bnf_dict = {}
        for item in bnf.split('\n'):
                if item.find(':') >= 0:
                    key, values = item.split(':',1)
                    key = key.strip()
                    bnf_dict[key] = strip_spaces(key, values)
                    non_Terminals.append(key)
                elif item:
                    values = bnf_dict[key]
                    values.extend(strip_spaces(key, item))
                    bnf_dict[key] = values
                else:
                    pass
        self.non_Terminals = non_Terminals        
        self._bnf = bnf_dict

    def get_bnf(self):
        return self._bnf

    def set_maintain_history(self, true_false):
            self._maintain_history = true_false

    def get_maintain_history(self):
        return self._maintain_history

    def set_max_program_length(self, max_program_length):
        max_program_length = long(max_program_length)
        self._max_program_length = max_program_length

    def get_max_program_length(self):
        return self._max_program_length

    def set_fitness_fail(self, fitness_fail):
        fitness_fail = float(fitness_fail)
        self._fitness_fail = fitness_fail

    def get_fitness_fail(self):
        return self._fitness_fail

    def set_mutation_type(self, mutation_type):
        errmsg = "The mutation type must be either '%s' or '%s'." % (
                                                    's', 'm')
        if mutation_type not in ['m', 's']:
            raise ValueError(errmsg)

        self._mutation_type = mutation_type

    def get_mutation_type(self):
        return self._mutation_type

    def set_mutation_rate(self, mutation_rate):
        errmsg = """The mutation rate, %s must be a float value
                    from 0.0 to 1.0""" % (mutation_rate)
        if not (0.0 <= mutation_rate <= 1.0):
            raise ValueError(errmsg)
        self._mutation_rate = mutation_rate

    def get_mutation_rate(self):
        return self._mutation_rate

    def set_crossover_rate(self, crossover_rate):
        errmsg = """The crossover rate, %s must be a float value
                    from 0.0 to 1.0""" % (crossover_rate)
        if not (0.0 <= crossover_rate <= 1.0):
            raise ValueError(errmsg)

        self._crossover_rate = crossover_rate

    def get_crossover_rate(self):
        return self._crossover_rate

    def set_children_per_crossover(self, children_per_crossover):
        if children_per_crossover not in [1, 2]:
            raise ValueError(
                "The children per crossovermust be either 1 or 2.")
        self._children_per_crossover = children_per_crossover

    def get_children_per_crossover(self):
        return self._children_per_crossover

    def set_max_generations(self, generations):
            self.stopping_criteria[STOPPING_MAX_GEN] = generations

    def get_max_generations(self):
        return self.stopping_criteria[STOPPING_MAX_GEN]

    def set_fitness_type(self, fitness_type, target_value=0.0):
        self.fitness_list.set_fitness_type(fitness_type)
        self.fitness_list.set_target_value(target_value)

    def get_fitness_type(self):
        return self.fitness_list.get_fitness_type()

    def set_max_fitness_rate(self, max_fitness_rate):
        errmsg = """The max fitness rate, %s must be a float value
                    from 0.0 to 1.0""" % (max_fitness_rate)
        if not (0.0 <= max_fitness_rate <= 1.0):
            raise ValueError(errmsg)

        self._max_fitness_rate = max_fitness_rate

    def get_max_fitness_rate(self):
        return self._max_fitness_rate

    def set_fitness_selections(self, *params):
        for fitness_selection in params:
            if isinstance(fitness_selection, Fitness):
                self.fitness_selections.append(fitness_selection)
            else:
                raise ValueError("Invalid fitness selection")

    def set_replacement_selections(self, *params):
        for replacement_selection in params:
            if isinstance(replacement_selection, Replacement):
                self.replacement_selections.append(replacement_selection)
            else:
                raise ValueError("Invalid replacement selection")

    def get_fitness_history(self, statistic='best_value'):
        hist_list = []
        for fitness_list in self.history:
            hist_list.append(fitness_list.__getattribute__(statistic)())
        return hist_list

    def get_best_member(self):
        return self.population[self.fitness_list.best_member()]

    def get_worst_member(self):
        return self.population[self.fitness_list.worst_member()]

    def set_timeouts(self, preprogram, program):
            self._timeouts[0] = preprogram
            self._timeouts[1] = program

    def get_timeouts(self):
        return self._timeouts

    def _compute_fitness(self):
        for gene in self.population:
            starttime = datetime.now()
            gene._generation = self._generation
            gene.starttime = starttime
            gene.set_keys (self.non_Terminals)
            if self._generation == 0 :
                gene.compute_fitness(True)
            self.population[gene.member_no]=gene
            self.fitness_list[gene.member_no][0] = gene.get_fitness()

    # def preselect(self):
    #     for fsel in self.fitness_selections:
    #         fsel.set_fitness_list(self.fitness_list)
    #         selected=fsel.select()
    #     for i in selected:
    #         self._pre_selected.append(deepcopy(self.population[i]))

    def run(self, starting_generation=0):
        self._generation = starting_generation
        self._compute_fitness()
        # self.preselect()
        while True:
            if self._maintain_history:
                self.history.append(deepcopy(self.fitness_list))
            if self._continue_processing() and self.fitness_list.best_value() != self._fitness_fail:
                self._perform_endcycle()
                self._generation+=1
                self._compute_fitness()
            else:
                break
      
    def create_genotypes(self,file,interpreter_Shell,interpreter_Options,nTInvlvdGenProcess):
        self.nT_Invld_Gen_Process=nTInvlvdGenProcess
        self._extractProductions()
        self._prepareInitial_Population(file)
        if len(self.initial_Population)<=0:
            return
        member_no = 0
        
        while member_no < self._population_size:
            gene = Genotype(self._start_gene_length,
                        self._max_gene_length,
                        member_no,interpreter_Shell,interpreter_Options)
            gene.local_bnf = deepcopy(self._bnf)
            gene.local_bnf['<member_no>'] = [gene.member_no]
            gene.keywords=self._bnf['keyword']+self._bnf['futureReservedWord']
            gene._max_program_length = self._max_program_length
            gene._fitness_fail = self._fitness_fail
            gene._extend_genotype = self._extend_genotype
            gene._timeouts = self._timeouts
            gene._wrap = self._wrap
            self.population.append(gene)
            member_no += 1
            gene.local_bnf["program"]=self.initial_Population[gene.member_no]
            gene.execution_timeout = self.execution_timeout

        return True;  

    def _perform_endcycle(self):
        self._pre_selected = self._evaluate_fitness(True)

        childList=[]
        while len(childList) + len(self._pre_selected) < self._population_size:
            print len(childList)
            ch=choice([0,1])
            fitness_pool = self._evaluate_fitness()
            if ch == 1:
                child_list = self._perform_crossovers(fitness_pool)
                childList.extend(child_list)
                child_list = self._perform_mutations(fitness_pool)
                if child_list is not None:
                    childList.extend(child_list)
            else:
                child_list = self._perform_mutations(fitness_pool)
                if child_list is not None:
                    childList.extend(child_list)
                child_list = self._perform_crossovers(fitness_pool)
                childList.extend(child_list)
        self._perform_replacements(childList)

    """
        if ind=True; certain num of indv are selected based on max fitness rate (say m). These are included in offspring list.

        remianing individuals max_pop - m are selected which includes these m indiv undergo crossover and mutation
        m+(n-m) = n (new offspring are generated which represents next generations)
    """
    def _evaluate_fitness(self,ind=False):
        flist = []
        flist1 = []
        if ind:
            total = int(round(self._max_fitness_rate * float(self._population_size)))
            count = 0
            for fsel in self.fitness_selections:
                fsel.set_fitness_list(self.fitness_list)
                selected=fsel.select()
                for i in selected:
                    if count == total:
                        break
                    flist.append(i)
                    count += 1
            for member_no in flist:
                flist1.append(deepcopy(self.population[member_no]))
        else:
            for gene in self.population:
                if gene.get_fitness()!=self._fitness_fail:
                    flist1.append(deepcopy(gene))
        return flist1

    def _perform_crossovers(self, flist):
        child_list = []
        length = int(round(self._crossover_rate * float(self._population_size)))
        """
        If no of fitness selections is less than no of indv undergoing crossover, than only no equal to no of fitness selections are allowed to undergo process.
        """
        if len(flist) < length:
            length=len(flist)
        if length % 2 == 1:
            length -= 1
        if length >= 2:
            for i in xrange(0, length, 2):
                parent1 = choice(flist)
                flist.remove(parent1)
                parent2 = choice(flist)
                flist.remove(parent2)

                if randint(0, 1):
                        child1 = deepcopy(parent1)
                        child2 = deepcopy(parent2)
                else:
                        child1 = deepcopy(parent2)
                        child2 = deepcopy(parent1)
                
                child1_binary = child1.binary_gene
                child2_binary = child2.binary_gene
                
                child1Prg=child1.get_program()
                child2Prg=child2.get_program()
                
                child1ParseTree,child1._identifiers=self.parseCode(child1Prg)
                non_term1=self.parser.extractNonTerminal(child1ParseTree)

                child2ParseTree,child2._identifiers=self.parseCode(child2Prg)
                non_term2=self.parser.extractNonTerminal(child2ParseTree)

                if self.nT_Invld_Gen_Process is not None:
                    commonNonTerm=[val for val in non_term1 if (val in set(non_term2) and val in self.nT_Invld_Gen_Process)]
                else:
                    commonNonTerm=[val for val in non_term1 if (val in set(non_term2))]

                count=1
                if round(random(),1) < self.multiple_rate:
                    count=int(self.crossoverCount*(round(random(),1)))+1        
                selectedNt=[]
                if len(commonNonTerm) > 0:
                    for i in range(count):
                        selectedNt.append(choice(commonNonTerm))
                else:
                    return child_list

                subString1,s1,selected1NTList=self.parser.genCodeFrag(child1ParseTree,non_term1,True,selectedNt,None,len(selectedNt))
                subString2,s2,selected2NTList=self.parser.genCodeFrag(child2ParseTree,non_term2,True,selectedNt,None,len(selectedNt))
                
                try:
                    for k in selected2NTList:
                        s1 = s1.replace(selected2NTList[k],subString2[k])
                    for k in selected1NTList:
                        s2 = s2.replace(selected1NTList[k],subString1[k])
                    child1Prg_=s1
                    child2Prg_=s2
                
                except:
                    return child_list
                        
                child1.local_bnf['program']=child1Prg_
                child1.generate_decimal_gene()
                child1.compute_fitness()
                child2.local_bnf['program']=child2Prg_
                child2.generate_decimal_gene()
                child2.compute_fitness()
                if child1.get_fitness()!= self._fitness_fail or child1.get_fitness()!= self._fitness_fail:
                    child1.prog_generated = 1
                    child2.prog_generated = 1
                    child1.local_bnf['CodeFrag']=""
                    child2.local_bnf['CodeFrag']=""
                    if self._children_per_crossover == 2:
                        child_list.append(child1)
                        child_list.append(child2)
                    else:
                        child_list.append(child1)
                
        return child_list

        
    def _mutatebinarygene(self, gene, position1, position2):
        newRandBGene = ""
        
        count = 0
        length = position2 - position1
        if length > 0:
            while count < length * 8 :
                newRandBGene = newRandBGene + str(randint(0, 1))
                count += 1        
            gene = ''.join([gene[:position1 * 8], newRandBGene , gene[(position1 + length) * 8:]])
        
        return gene

    #Author: Spandan Veggalam
    def _perform_mutations(self, mlist):
        mutatedList=[]
        
        for gene in mlist:
            if round(random(),1) < self._mutation_rate :
                generative=False
                incompl, gene._identifiers = self.parseCode(gene.get_program())
                non_TerminalsList=self.parser.extractNonTerminal(incompl)
                if len(non_TerminalsList) >1:
                    if round(random(),1) < self._generative_mutation_rate :
                        generative=True
                        gene._max_depth=self._max_depth
                    count=1
                    if round(random(),1) < self.multiple_rate:
                        count=int(self.mutationCount*round(random(),1))+1
                    gene.local_bnf['CodeFrag'],selectedNt=self.parser.genCodeFrag(incompl,non_TerminalsList,None,None,self.nT_Invld_Gen_Process,count)
                    if len(selectedNt) <=0 :
                        continue
                    gene._map_gene()
                    if gene.get_fitness() != self._fitness_fail :
                        gene.local_bnf['CodeFrag']=""
                        gene.prog_generated = 1
                        mutatedList.append(gene)
                    
        return mutatedList

    def _perform_replacements(self, fitness_pool):
        position=0
        self.new_pop=[]
        self.fitness_list_new=FitnessList(CENTER)

        for gene in self._pre_selected:
            
            for gene1 in self.population:
                if gene1.member_no == gene.member_no:
                    self.population.remove(gene1)
                    break
            gene.member_no=position
            self.new_pop.append(gene)
            position += 1
        
        length = len(self.population)
        new_memNo=0

        for i in range(len(fitness_pool)):
            fitness_pool[i].member_no=new_memNo
            self.fitness_list_new.append([fitness_pool[i].get_fitness(),new_memNo])
            new_memNo+=1

        self.fitness_list_new.sort()
        for i in range(self._population_size-len(self._pre_selected)):
            member=self.fitness_list_new[i]
            gene=fitness_pool[member[1]]
            gene.member_no=position
            self.new_pop.append(gene)
            position+=1

        self.population=self.new_pop

        for gene in self.population:
            self.fitness_list[gene.member_no][0]=gene.get_fitness()

        print self.fitness_list_new
        print self.fitness_list

    def _continue_processing(self):
        """
        This method analyzes the fitness list against the stopping_criteria defined over target_value and max generations
        """
        status = True
        fitl = self.fitness_list
        print "fitness values : Generation " + str(self._generation+1)
        print fitl

        if self.stopping_criteria[STOPPING_MAX_GEN] is not None:
            if self.stopping_criteria[STOPPING_MAX_GEN] <= self._generation:
                return False
        if fitl.get_target_value() is not None:
            if fitl.get_fitness_type() == MAX:
                if fitl.best_value() >= fitl.get_target_value():
                    return False
            elif fitl.get_fitness_type() == MIN:
                if fitl.best_value() <= fitl.get_target_value():
                    return False
            elif fitl.get_fitness_type() == CENTER:
                if fitl.best_value() <= fitl.get_target_value():
                    return False

        return status
