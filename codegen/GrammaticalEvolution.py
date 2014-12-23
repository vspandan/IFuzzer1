#!/usr/bin/env python
from Tkconstants import INSERT
from Tkinter import Button, Frame, Tk, Text
from copy import deepcopy
from datetime import datetime
import logging
from os import path, system
from random import choice, randint
from re import sub
import subprocess
from tkFileDialog import askopenfilename
from tkMessageBox import askyesno, showwarning, showinfo, showerror
import tkMessageBox

from langparser.AntlrParser import *
from codegen.GenIncompleteCodeFrag import GenIncompleteCodeFrag
from codegen.fitness import CENTER, MAX, MIN
from codegen.fitness import FitnessList, Fitness, Replacement
from codegen.Genotypes import Genotype, MUT_TYPE_M, MUT_TYPE_S


STOPPING_MAX_GEN = 'max_generations'
STOPPING_FITNESS_LANDSCAPE = 'fitness_landscape'

#   Default values
DEFAULT_CROSSOVER_RATE = 0.2
DEFAULT_CHILDEREN_PER_CROSSOVER = 2
DEFAULT_MUTATION_TYPE = 's'
DEFAULT_MUTATION_RATE = 0.02
DEFAULT_MAX_FITNESS_RATE = .5
DEFAULT_WRAP = True
DEFAULT_EXTEND_GENOTYPE = True
DEFAULT_START_GENE_LENGTH = None
DEFAULT_MAX_GENE_LENGTH = None
DEFAULT_MAX_PROGRAM_LENGTH = None
DEFAULT_FITNESS_FAIL = -1000.0
DEFAULT_MAINTAIN_HISTORY = True
DEFAULT_TIMEOUTS = [20, 3600]

DEFAULT_LOG_FILE = 'GECodeGen.log'

logging.basicConfig(format='%(asctime)s %(message)s',
                    filename=DEFAULT_LOG_FILE,
                    level=logging.INFO)


class GrammaticalEvolution(object):

    def __init__(self):
        self.history = []
        self.population = []
        self.parser = AntlrParser()
        self.initial_Population = []
        self.non_Terminals=[]
        self.stopping_criteria = {
                STOPPING_MAX_GEN: None,
                STOPPING_FITNESS_LANDSCAPE: None}
        self.current_g = None
        self.fitness_selections = []
        self.replacement_selections = []        
        
        self._ind= None
        self._crossover_rate = DEFAULT_CROSSOVER_RATE
        self._children_per_crossover = DEFAULT_CHILDEREN_PER_CROSSOVER
        self._mutation_type = DEFAULT_MUTATION_TYPE
        self._mutation_rate = DEFAULT_MUTATION_RATE
        self._max_fitness_rate = DEFAULT_MAX_FITNESS_RATE

        #   Parameters for phenotype creation
        self._wrap = DEFAULT_WRAP
        self._extend_genotype = DEFAULT_EXTEND_GENOTYPE
        self._start_gene_length = DEFAULT_START_GENE_LENGTH
        self._max_gene_length = DEFAULT_MAX_PROGRAM_LENGTH
        self._max_program_length = DEFAULT_MAX_PROGRAM_LENGTH

        #   Parameters for overall process
        self.fitness_list = FitnessList(CENTER)
        self._generation = 0
        self._fitness_fail = DEFAULT_FITNESS_FAIL
        self._maintain_history = DEFAULT_MAINTAIN_HISTORY
        self._timeouts = DEFAULT_TIMEOUTS

        self._bnf = {}
        self._population_size = 0

    #Author : Spandan Veggalam	
    def set_ind(self, ind):
        self._ind=ind
    
    #Author : Spandan Veggalam
    def setGrammarFile(self,fileName):
        self.grammarFile=fileName
    
    #Author : Spandan Veggalam    
    def _extractProductions(self):
        bnf=""        
        f = open(self.grammarFile,'r')
        for line in f:
            bnf+=line;
        f.close()        
        self.set_bnf(bnf)
    
    #Author : Spandan Veggalam
    def parseCode(self,codeFragment):
        codeFragment= codeFragment.replace('\n', '')
        return self.parser.parseTree(codeFragment)
    
    #Author : Spandan Veggalam
    def _prepareInitial_Population (self,fileName):
        try:
            f=open(fileName,'r')
            self.parseRepr=self.parser.parseTree(f.read())
            if self.parseRepr is not None and len(self.parseRepr)>0:
                self.codefragGen =  GenIncompleteCodeFrag()
                self.initial_Population = self.codefragGen.genCodeFrag(self.parseRepr,self._population_size,self.parser.non_Terminals)
            else:
                print fileName
                print "Syntax error"
            f.close()
        except:
            """
            if program is syntactically invalid. it is not considered; simply skipped
            """
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
    
    #Modified Author : Spandan Veggalam 
    def set_bnf(self, bnf):
        def strip_spaces(key, values):
            values = [value.strip()
                for value in values.split('|') if value]
            return values

        non_Terminals=[]

        bnf_dict = {}
        if self._ind == 1:
            for item in bnf.split('\n'):
                if item.find('::=') >= 0:
                    key, values = item.split('::=')
                    key = key.strip()
                    bnf_dict[key] = strip_spaces(key, values)
                    non_Terminals.append(key)
                elif item:
                    values = bnf_dict[key]
                    values.extend(strip_spaces(key, item))
                    
                    bnf_dict[key] = values
                else:
                    #   blank line
                    pass                
        else:
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
                    #   blank line
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
        #   coerce if possible
        fitness_fail = float(fitness_fail)
        if not isinstance(fitness_fail, float):
            raise ValueError(errmsg)

        self._fitness_fail = fitness_fail

    def get_fitness_fail(self):
        return self._fitness_fail

    def set_mutation_type(self, mutation_type):
        errmsg = "The mutation type must be either '%s' or '%s'." % (
                                                    MUT_TYPE_S, MUT_TYPE_M)
        if mutation_type not in [MUT_TYPE_M, MUT_TYPE_S]:
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


    #Modified Author : Spandan Veggalam  
    def _compute_fitness(self):
        for gene in self.population:
            starttime = datetime.now()
            gene._generation = self._generation
            logging.debug("Starting member G %s: %s at %s" % (
                self._generation, gene.member_no,
                starttime.strftime('%m/%d/%y %H:%M')))

            gene.starttime = starttime
            gene.set_keys (self.non_Terminals)
            self.current_g = gene
            gene.compute_fitness()
            self.population[gene.member_no]=gene
            logging.debug("fitness=%s" % (gene.get_fitness()))
            self.fitness_list[gene.member_no][0] = gene.get_fitness()

    def run(self, starting_generation=0):
        logging.info("started run")
        self._generation = starting_generation
        while True:
            self._compute_fitness()
            if self._maintain_history:
                self.history.append(deepcopy(self.fitness_list))

            if self._continue_processing():
                self._perform_endcycle()

                logging.info("Finished generation: %s Max generations: %s" % (
                            self._generation,
                            self.get_max_generations()))
                logging.info(' '.join(
                            ["best_value: %s" % (
                                self.fitness_list.best_value()),
                            "median: %s" % (self.fitness_list.median()),
                            "mean: %s" % (self.fitness_list.mean())]))
                #temp -- remove this
                gene = self.population[self.fitness_list.best_member()]
                program = gene.get_program()
                #Update codefragementsbased upon their fitness
                logging.info(program)

                #logging.debug("stddev= %s" % self.fitness_list.stddev())
                self._generation += 1
            else:
                break

        logging.info(
            "completed run: generations: %s, best member:%s fitness: %s" % (
                    self._generation,
                    self.fitness_list.best_member(),
                    self.fitness_list.best_value()))

        return self.fitness_list.best_member()

    #Modified Author : Spandan Veggalam 
    def create_genotypes(self,file):
        self._extractProductions()
        self._prepareInitial_Population(file)
        if len(self.initial_Population)<=0:
            """
            if program is syntactically invalid. it is not considered; simply skipped
            """
            return
        member_no = 0
        while member_no < self._population_size:
            gene = Genotype(self._start_gene_length,
                        self._max_gene_length,
                        member_no)
            #   a local copy is made because variables
            #   can be saved within the local_bnf
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
            gene._identifiers=self.parser.identifiers
        return True;  

    def _perform_endcycle(self):
        fitness_pool = self._evaluate_fitness()
        child_list = self._perform_crossovers(fitness_pool)

        fitness_pool.extend(child_list)
        self._perform_mutations(fitness_pool)
        self._perform_replacements(fitness_pool)

    def _evaluate_fitness(self):
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
                    #   Done
                    break

        flist1 = []
        for member_no in flist:
            flist1.append(deepcopy(self.population[member_no]))

        return flist1

    def _perform_crossovers(self, flist):
        child_list = []
        length = len(flist)
        if length % 2 == 1:
            length -= 1
        if length >= 2:
            for i in xrange(0, length, 2):
                parent1 = flist[i]
                parent2 = flist[i + 1]

                child1, child2 = self._crossover(parent1, parent2,True)
                if self._children_per_crossover == 2:
                    child_list.append(child1)
                    child_list.append(child2)
                else:
                    child_list.append(child1)

        return child_list

    #Modified Author : Spandan Veggalam 
    def _crossover(self, parent1, parent2, ind=None):
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
        
        if ind is None:
            minlength = min(len(child1_binary), len(child2_binary))
            crosspoint = randint(2, minlength - 2)
    
            child1_binary, child2_binary = self._crossover_function(
                child1.binary_gene, child2.binary_gene, crosspoint)
            
            child1.set_binary_gene(child1_binary)
            child1.generate_decimal_gene()
            child2.set_binary_gene(child2_binary)
            child2.generate_decimal_gene()
        
            return (child1, child2)
    
        child1Prg=child1.get_program()
        child2Prg=child2.get_program()
        
        child1ParseTree=self.parseCode(child1Prg)
        non_term1=self.parser.non_Terminals
        child2ParseTree=self.parseCode(child2Prg)
        non_term2=self.parser.non_Terminals

        commonNonTerm=[val for val in non_term1 if val in set(non_term2)]
        
        if len(commonNonTerm) > 0:
            selectedNt= choice(commonNonTerm)
        else:
            return (child1, child2)
        
        #retrieves substring under selected non-terminal from both the childs and these are used in crossover 
        subString1=self.codefragGen.genCodeFrag(child1ParseTree,1,non_term1,True,selectedNt)        
        subString2=self.codefragGen.genCodeFrag(child2ParseTree,1,non_term2,True,selectedNt)       
        
        subString1=sub(r'\s+', ' ',subString1)
        subString2=sub(r'\s+', ' ',subString2)
        if child1Prg.find(subString2) <0 or child2Prg.find(subString1) <0:
            return (child1, child2) 
        
        startPoint1=child1Prg.index(subString1)
        startPoint2=child2Prg.index(subString2)
        
        child1Prg_ = child1Prg[0:startPoint1]+subString2 +child1Prg[startPoint1+len(subString1):]
        child2Prg_ = child2Prg[0:startPoint2]+subString1 +child2Prg[startPoint2+len(subString2):]
        
        #TODOcheck the binary string against child and also parent
        child1PrgBinay_ = child1_binary[0:startPoint1*8]+ child2_binary[(startPoint2)*8:(startPoint2+len(subString2))*8] +child1Prg[(startPoint1+len(subString1))*8:]
        child2PrgBinay_ = child2_binary[0:startPoint2*8]+ child1_binary[(startPoint1)*8:(startPoint1+len(subString1))*8] +child2Prg[(startPoint2+len(subString2))*8:]
        
        incompl1=self.parseCode(child1Prg_)
        child1.set_identifiers(self.parser.identifiers)
        incompl2=self.parseCode(child2Prg_)
        child2.set_identifiers(self.parser.identifiers)
        
        child1.local_bnf['CodeFrag'],dummy =  self.codefragGen.genCodeFrag(incompl1,1,self.codefragGen.extractNonTerminal(incompl1.split()))
        child2.local_bnf['CodeFrag'],dummy =  self.codefragGen.genCodeFrag(incompl2,1,self.codefragGen.extractNonTerminal(incompl2.split()))
        
        child1.set_binary_gene(child1_binary)
        child1.generate_decimal_gene()
        child2.set_binary_gene(child2_binary)
        child2.generate_decimal_gene()
        
        return (child1, child2) 
        

    @staticmethod
    def _crossover_function(child1_binary, child2_binary, crosspoint):
        child1_binary, child2_binary = child1_binary[0:crosspoint] + \
                                    child2_binary[crosspoint:], \
                                    child2_binary[0:crosspoint] + \
                                    child1_binary[crosspoint:]

        return (child1_binary, child2_binary)

    #Author: Spandan Veggalam
    def _perform_mutations(self, mlist):
        for gene in mlist:
            prg=gene.get_program()
            incompl=self.parseCode(prg)
            gene.set_identifiers(self.parser.identifiers)
            if len(incompl.strip()) >0:
                gene.local_bnf['CodeFrag'],selectedNt=self.codefragGen.genCodeFrag(incompl,1,self.codefragGen.extractNonTerminal(incompl.split()))
                position1=gene.local_bnf['CodeFrag'].find(selectedNt)
                position2=position1+len(selectedNt)            
                gene.mutate(self._mutation_rate, self._mutation_type,position1, position2)

    def _perform_replacements(self, fitness_pool):
        position = 0
        for rsel in self.replacement_selections:
            rsel.set_fitness_list(self.fitness_list)

            for replaced_no in rsel.select():
                replaced_g = self.population[replaced_no]
                if position < len(fitness_pool):
                    new_g = fitness_pool[position]
                    new_g.member_no = replaced_g.member_no
                    new_g._generation = self._generation + 1

                    #   update local bnf
                    new_g.local_bnf['<member_no>'] = [new_g.member_no]

                    self.population[new_g.member_no] = new_g
                    position += 1
                else:
                    break

    def _continue_processing(self):
        status = True
        fitl = self.fitness_list

        #   check max generations first
        if self.stopping_criteria[STOPPING_MAX_GEN] is not None:
            if self.stopping_criteria[STOPPING_MAX_GEN] <= self._generation:
                logging.info("stopping processing due to max generation")
                return False

        #   check target value
        if fitl.get_target_value() is not None:
            if fitl.get_fitness_type() == MAX:
                if fitl.best_value() >= fitl.get_target_value():
                    logging.info(' '.join([
                    "stopping processing due to",
                    "best value, %s, better than target value, %s" % (
                    fitl.best_value(), fitl.get_target_value())]))
                    return False
            elif fitl.get_fitness_type() == MIN:
                if fitl.best_value() <= fitl.get_target_value():
                    logging.info(' '.join([
                    "stopping processing due to",
                    "best value, %s, better than target value, %s" % (
                    fitl.best_value(), fitl.get_target_value())]))
                    return False
            elif fitl.get_fitness_type() == CENTER:
                if fitl.best_value() <= fitl.get_target_value():
                    logging.info(' '.join([
                    "stopping processing due to",
                    "best value, %s, better than target value, %s" % (
                    fitl.best_value(), fitl.get_target_value())]))
                    return False

        #   Finally check if there is a stopping function
        if self.stopping_criteria[STOPPING_FITNESS_LANDSCAPE] is not None:
            status = self.stopping_criteria[STOPPING_FITNESS_LANDSCAPE](
                                                        self.fitness_list)
            logging.info(' '.join([
                                "stopping processing due to",
                                "fitness landscape being reached."]))

        return status
