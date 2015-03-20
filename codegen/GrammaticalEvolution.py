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
STOPPING_FITNESS_LANDSCAPE = 'fitness_landscape'

class GrammaticalEvolution(object):

    def __init__(self):
        self.history = []
        self.population = []
        self.parser = AntlrParser()
        self.initial_Population = []
        self.identifiers = []
        self.non_Terminals=[]
        self.stopping_criteria = {
                STOPPING_MAX_GEN: None,
                STOPPING_FITNESS_LANDSCAPE: None}
        self.current_g = None
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

    def set_crossover_count(self, count):
        self.crossoverCount=count

    def set_mutation_count(self, count):
        self.mutationCount=count

    def dynamic_mutation_rate(self, ind ):
        self.dynamic_mutation = ind
        self._mutation_rate=0.02
    
    def dynamic_crossover_rate(self, ind):
        self.dynamic_crossover = ind
        self._crossover_rate=0.4
    
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
        codeFragment= codeFragment.replace('\n', ' ')
        return self.parser.parseTree(codeFragment,True)
    
    def _prepareInitial_Population (self,fileName):
            self.parseRepr=self.parser.parseTree(path.abspath(fileName))
            if self.parseRepr is not None and len(self.parseRepr)>0 and 'missing' not in self.parseRepr:
                #Generates incomplete code fragment
                self.initial_Population,self.identifiers = self.parser.genCodeFrag(self.parseRepr,self._population_size,self.parser.extractNonTerminal(self.parseRepr),None,None,self.nT_Invld_Gen_Process,self.mutationCount)
            else:
                return

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
        if not isinstance(start_gene_length, long):
            raise ValueError("start_gene_length, %s, must be a long" % (
                                                    start_gene_length))
        if start_gene_length < 0:
            raise ValueError("start_gene_length, %s, must be above 0" % (
                                                    start_gene_length))
        if not isinstance(max_gene_length, long):
            raise ValueError("max_gene_length, %s, must be a long" % (
                                                    max_gene_length))
        if max_gene_length < 0:
            raise ValueError("max_gene_length, %s, must be above 0" % (
                                                    max_gene_length))
        if start_gene_length > max_gene_length:
            raise ValueError("""max_gene_length, %s, cannot be smaller
                than start_gene_length%s""" % (
                    max_gene_length, start_gene_length))

        self._start_gene_length = start_gene_length
        self._max_gene_length = max_gene_length

    def get_genotype_length(self):
        return (self._start_gene_length, self._max_gene_length)

    def set_extend_genotype(self, true_false):
        if isinstance(true_false, bool):
            self._extend_genotype = true_false
        else:
            raise ValueError("Extend genotype must be True or False")

    def get_extend_genotype(self):
        return self._extend_genotype

    def set_wrap(self, true_false):
        if isinstance(true_false, bool):
            self._wrap = true_false
        else:
            raise ValueError("Wrap must be True or False")

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
        if isinstance(true_false, bool):
            self._maintain_history = true_false
        else:
            raise ValueError("Maintain history must be True or False")

    def get_maintain_history(self):
        return self._maintain_history

    def set_max_program_length(self, max_program_length):
        errmsg1 = """The maximum program length, %s must be an long value
                    """ % (max_program_length)
        errmsg2 = """The maximum program length, %s must be greater than 0
                    """ % (max_program_length)
        max_program_length = long(max_program_length)
        if not isinstance(max_program_length, long):
            raise ValueError(errmsg1)
        if max_program_length < 0:
            raise ValueError(errmsg2)

        self._max_program_length = max_program_length

    def get_max_program_length(self):
        return self._max_program_length

    def set_fitness_fail(self, fitness_fail):
        errmsg = """The fitness_fail, %s must be a float value
                    """ % (fitness_fail)
        fitness_fail = float(fitness_fail)
        if not isinstance(fitness_fail, float):
            raise ValueError(errmsg)

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
        if not isinstance(mutation_rate, float):
            raise ValueError(errmsg)
        if not (0.0 <= mutation_rate <= 1.0):
            raise ValueError(errmsg)

        self._mutation_rate = mutation_rate

    def get_mutation_rate(self):
        return self._mutation_rate

    def set_crossover_rate(self, crossover_rate):
        errmsg = """The crossover rate, %s must be a float value
                    from 0.0 to 1.0""" % (crossover_rate)
        if not isinstance(crossover_rate, float):
            raise ValueError(errmsg)
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
        if isinstance(generations, int) and generations >= 0:
            self.stopping_criteria[STOPPING_MAX_GEN] = generations
        else:
            raise ValueError("""
                generations, %s, must be an int 0 or greater""" % (
                                                                generations))

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
        if not isinstance(max_fitness_rate, float):
            raise ValueError(errmsg)
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
        if isinstance(preprogram, int) and preprogram >= 0:
            self._timeouts[0] = preprogram
        else:
            raise ValueError("""
                timeout, %s, must be an int 0 or above""" % (preprogram))

        if isinstance(program, int) and program >= 0:
            self._timeouts[1] = program
        else:
            raise ValueError("""
                timeout, %s, must be an int 0 or above""" % (program))

    def get_timeouts(self):
        return self._timeouts

    def _compute_fitness(self):
        for gene in self.population:
            starttime = datetime.now()
            gene._generation = self._generation
            gene.starttime = starttime
            gene.set_keys (self.non_Terminals)
            self.current_g = gene
            gene.compute_fitness()
            self.population[gene.member_no]=gene
            self.fitness_list[gene.member_no][0] = gene.get_fitness()

    def run(self, starting_generation=0):
        self._generation = starting_generation
        while True:
            self._compute_fitness()
            if self._maintain_history:
                self.history.append(deepcopy(self.fitness_list))
            if self._continue_processing() and self.fitness_list.best_value() != self._fitness_fail:
                self._perform_endcycle()
                gene = self.population[self.fitness_list.best_member()]
                program = gene.get_program()
                self._generation += 1
            else:
                break
        print "best fitness value:"
        print self.fitness_list.best_member()
        return self.fitness_list.best_member()

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
            gene._fitness = self._fitness_fail
            gene._fitness_fail = self._fitness_fail
            gene._extend_genotype = self._extend_genotype
            gene._timeouts = self._timeouts
            gene._wrap = self._wrap
            self.population.append(gene)
            member_no += 1
            gene.local_bnf['CodeFrag'] =  self.initial_Population[member_no-1]
            gene.tracePrg2File("i::: \t"+gene.local_bnf['CodeFrag']);
            gene._identifiers=self.identifiers[member_no-1]
            gene.nTInvlvdGenProcess=nTInvlvdGenProcess
        return True;  

    def _perform_endcycle(self):
        childList= self._evaluate_fitness(True)
        while len(childList) < self._population_size:
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
        if ind:
            flist = []
            total = int(round(
                self._max_fitness_rate * float(self._population_size)))        
            count = 0
            for fsel in self.fitness_selections:
                fsel.set_fitness_list(self.fitness_list)
                for i in fsel.select():
                    flist.append(i)
                    count += 1
                    if count == total:
                        break
            flist1 = []
            for member_no in flist:
                flist1.append(deepcopy(self.population[member_no]))
            return flist1
        else:
            flist3=[]
            total = int(round(
                self._max_fitness_rate * float(self._population_size)))        
            total=self._population_size-total
            count = 0
            for fsel in self.fitness_selections:
                fsel.set_fitness_list(self.fitness_list)
                for i in fsel.select():
                    flist3.append(i)
                    count += 1
                    if count == total:
                        break
            flist2 = []
            for member_no in flist3:
                flist2.append(deepcopy(self.population[member_no]))

            return flist2

    def _perform_crossovers(self, flist):
        child_list = []
        length = int(round(self._crossover_rate * float(self._population_size)))
        if length % 2 == 1:
            length -= 1
        if length >= 2:
            for i in xrange(0, length, 2):
                parent1 = flist[i]
                parent2 = flist[i + 1]

                child1, child2 = self._crossover(parent1, parent2)
                if self._children_per_crossover == 2:
                    child_list.append(child1)
                    child_list.append(child2)
                else:
                    child_list.append(child1)

        return child_list

    def _crossover(self, parent1, parent2):
        if not isinstance(parent1, Genotype):
            raise ValueError("Parent1 is not a genotype")
        if not isinstance(parent2, Genotype):
            raise ValueError("Parent2 is not a genotype")
        
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
        
        child1ParseTree=self.parseCode(child1Prg)
        non_term1=self.parser.extractNonTerminal(child1ParseTree)
        child2ParseTree=self.parseCode(child2Prg)
        non_term2=self.parser.extractNonTerminal(child1ParseTree)

        if self.nT_Invld_Gen_Process is not None:
            commonNonTerm=[val for val in non_term1 if (val in set(non_term2) and val in self.nT_Invld_Gen_Process)]
        else:
            commonNonTerm=[val for val in non_term1 if (val in set(non_term2))]
        
        selectedNt=[]
        if len(commonNonTerm) > 0:
            for i in range(self.crossoverCount):
                selectedNt.append(choice(commonNonTerm))
        else:
            return (child1, child2)
        
        #retrieves substring under selected non-terminal from both the childs and these are used in crossover 

        subString1,s1,selected1NTList=self.parser.genCodeFrag(child1ParseTree,1,non_term1,True,selectedNt,None,self.crossoverCount)        
        subString2,s2,selected2NTList=self.parser.genCodeFrag(child2ParseTree,1,non_term2,True,selectedNt,None,self.crossoverCount)       
        
        """
        if child1Prg.find(selectedNt) <0 or child2Prg.find(selectedNt) <0:
            return (child1, child2) 
        """
        try:
            for k in selected2NTList:
                child1Prg_ = s1.replace(selected2NTList[k],subString2[k])
            for k in selected1NTList:
                child2Prg_ = s2.replace(selected1NTList[k],subString1[k])
        
        except:
            return (child1, child2) 
                
        """
        #Alternate Impl
        child1Prg_ = child1Prg[0:startPoint1]+subString2 +child1Prg[startPoint1+len(subString1):]
        child2Prg_ = child2Prg[0:startPoint2]+subString1 +child2Prg[startPoint2+len(subString2):]
        """

        """
        #Losing track of genes
        #TODOcheck the binary string against child and also parent
        child1PrgBinay_ = child1_binary[0:startPoint1*8]+ child2_binary[(startPoint2)*8:(startPoint2+len(subString2))*8] +child1Prg[(startPoint1+len(subString1))*8:]
        child2PrgBinay_ = child2_binary[0:startPoint2*8]+ child1_binary[(startPoint1)*8:(startPoint1+len(subString1))*8] +child2Prg[(startPoint2+len(subString2))*8:]
        """

        incompl1=self.parseCode(child1Prg_)
        incompl2=self.parseCode(child2Prg_)
        
        child1.local_bnf['CodeFrag'],dummy =  self.parser.genCodeFrag(incompl1,1,self.parser.extractNonTerminal(incompl1))
        child2.local_bnf['CodeFrag'],dummy =  self.parser.genCodeFrag(incompl2,1,self.parser.extractNonTerminal(incompl2))

        child1.set_binary_gene(child1_binary)
        child1.generate_decimal_gene()
        child1.calculateFitness(child1Prg_)
        child2.set_binary_gene(child2_binary)
        child2.generate_decimal_gene()
        child2.calculateFitness(child2Prg_)
        
        return (child1, child2) 
        
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
            if random() < self._mutation_rate:
                incompl=self.parseCode(gene.get_program())
                gene.set_identifiers(self.identifiers)
                if len(incompl.strip()) >0:
                    #selectedNt List
                    gene.local_bnf['CodeFrag'],selectedNt=self.parser.genCodeFrag(incompl,1,self.parser.extractNonTerminal(incompl),None,None,self.nT_Invld_Gen_Process,self.mutationCount)
                    if len(selectedNt) <=0 :
                        continue
                    gene.tracePrg2File("mutation");
                    gene._map_gene()
                    gene.tracePrg2File("after mutation");
                    """
                    #losing track of gene
                    position1=gene.local_bnf['CodeFrag'].find(selectedNt)
                    position2=position1+len(selectedNt)  
                    if position1 is not None and position2 is not None:
                        subCode = gene.local_bnf['CodeFrag'][position2:]
                        replCode = gene._map_variables(gene.local_bnf['CodeFrag'], True)
                        gene.local_bnf['program']=(gene.local_bnf['CodeFrag'][0:position1]+" "+ replCode +" "+gene.local_bnf['CodeFrag'][position2:]).replace("__id__","")
                        #gene.set_binary_gene(self._mutatebinarygene(gene.binary_gene, position1, position2))
                        gene.generate_decimal_gene()
                    """
                    if gene.get_fitness() != gene.get_fitness_fail() :
                        mutatedList.append(gene)
        return mutatedList

    def _perform_replacements(self, fitness_pool):
        position = 0
        for rsel in self.replacement_selections:
            rsel.set_fitness_list(self.fitness_list)

            for i in rsel.select():
                replaced_g = self.population[i]
                if position < len(fitness_pool):
                    newGene = fitness_pool[position]
                    newGene.member_no = replaced_g.member_no
                    newGene._generation = self._generation + 1
                    newGene.local_bnf['<member_no>'] = [newGene.member_no]
                    self.population[newGene.member_no] = newGene
                    position += 1
                else:
                    break

    def _continue_processing(self):
        status = True
        fitl = self.fitness_list
        print "fitness values:"
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

        if self.stopping_criteria[STOPPING_FITNESS_LANDSCAPE] is not None:
            status = self.stopping_criteria[STOPPING_FITNESS_LANDSCAPE](
                                                        self.fitness_list)

        return status
