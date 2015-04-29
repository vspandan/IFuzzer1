#!/usr/bin/env python
from copy import deepcopy
from datetime import datetime
from os import path,listdir,remove
from random import choice, randint, random
from re import sub
from subprocess import Popen,PIPE
from langparser.AntlrParser import *
from codegen.fitness import CENTER, MAX, MIN
from codegen.fitness import FitnessList, Fitness, Replacement
from codegen.Genotypes import Genotype
from time import time
from threading import Thread
from jsbeautifier import beautify
from tempfile import NamedTemporaryFile

import signal 
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
import logging

logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                   )


VARIABLE_FORMAT = '(\W+)'
STOPPING_MAX_GEN = 'max_generations'

class GrammaticalEvolution(object):

    def __init__(self):
        self.FUNCTION_EXEC_TIMEOUT=10
        self._pre_selected = []
        self.history = []
        self.population = []
        self.initial_Population = []
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

        self._bnf = {}
        self._population_size = 0
        
        self.dynamic_mutation = 0
        self.dynamic_crossover = 0

        self.mutationCount = 1
        self.crossoverCount = 1
        self._multiple_rate = 0
        self._max_depth = 0
        self._generative_mutation_rate=0.5
        self.identifiers_mapping={}
        self.targetDirectory=""
        self.parsimony_constant=0
        self.meanLength=1

    def set_max_depth(self,depth):
        self._max_depth=depth

    def set_generative_mutation_rate(self,rate):
        self._generative_mutation_rate=rate

	def set_multiple_rate(self, rate):
		self._multiple_rate = rate

    def set_crossover_count(self, count):
        self.crossoverCount=count

    def set_mutation_count(self, count):
        self.mutationCount=count

    def set_execution_timeout(self, timeout):
        self.execution_timeout = timeout

    def dynamic_mutation_rate(self, ind):
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
    
    def _prepareInitial_Population (self,fileList):
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
        self._mutation_type = mutation_type

    def get_mutation_type(self):
        return self._mutation_type

    def set_mutation_rate(self, mutation_rate):
        self._mutation_rate = mutation_rate

    def get_mutation_rate(self):
        return self._mutation_rate

    def set_crossover_rate(self, crossover_rate):
        self._crossover_rate = crossover_rate

    def get_crossover_rate(self):
        return self._crossover_rate

    def set_children_per_crossover(self, children_per_crossover):
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

    def _compute_fitness(self):
        self.meanLength=1
        def calculateCovariance(meanFitness):
            value=0
            for gene in self.population:
                value += ( gene.get_fitness() - meanFitness ) * ( gene.prgLength - self.meanLength )
            return value

        def variance():
            value=0
            for gene in self.population:
                value += ( gene.prgLength - self.meanLength ) ** 2 
            return value
        
        totalLength=0
        totalFitness=0.0
        for gene in self.population:
            starttime = datetime.now()
            gene._generation = self._generation
            gene.starttime = starttime
            gene.set_keys (self.non_Terminals)
            if self._generation == 0 :
                logging.debug("evaluating" + str(gene.member_no))
                logging.debug(gene.local_bnf["program"])
                gene.score=0
                self.compute_fitness(gene)
            self.population[gene.member_no]=gene
            self.fitness_list[gene.member_no][0] = gene.get_fitness()
            totalLength += gene.prgLength
            totalFitness += gene.get_fitness()

        self.meanLength=totalLength/self._population_size
        meanFitness=totalFitness/self._population_size

        print meanFitness
        print self.meanLength
        
        self.parsimony_constant=calculateCovariance(meanFitness)/variance()
        print self.parsimony_constant

    

    def run(self, starting_generation=0):
        self._generation = starting_generation
        starttime=time()
        self._compute_fitness()
        self._generation+=1
        logging.info("completed : "+str(self._generation)+" in "+str(round((time()-starttime))) + " seconds")
        while True:
            logging.info("Starting "+str(self._generation)+" Generation - "+str(datetime.now()))
            starttime=time()
            if self._maintain_history:
                self.history.append(deepcopy(self.fitness_list))
            if self._continue_processing() and self.fitness_list.best_value() != self._fitness_fail:
                self._perform_endcycle()
                self._generation+=1
                self._compute_fitness()
            else:
                break
            logging.info("completed : "+str(self._generation)+" in "+str(round((time()-starttime))) + " seconds")
      
    def create_genotypes(self,file,interpreter_Shell,interpreter_Options,nTInvlvdGenProcess,interpreterInd):
        self.interpreter_Shell=interpreter_Shell
        self.interpreter_Options =interpreter_Options
        self.interpreterInd=interpreterInd
        self.nT_Invld_Gen_Process=nTInvlvdGenProcess
        self._extractProductions()
        self._prepareInitial_Population(file)
        if len(self.initial_Population)<=0:
            return
        member_no = 0
        
        while member_no < self._population_size:
            gene = Genotype(self._start_gene_length,
                        self._max_gene_length,
                        member_no)
            gene.local_bnf = deepcopy(self._bnf)
            gene.local_bnf['<member_no>'] = [gene.member_no]
            gene.keywords=self._bnf['keyword']+self._bnf['futureReservedWord']
            gene._extend_genotype = self._extend_genotype
            gene._wrap = self._wrap
            gene.nTInvlvdGenProcess=nTInvlvdGenProcess
            member_no += 1
            gene.local_bnf["program"]=self.initial_Population[gene.member_no]
            self.population.append(gene)
        self.initial_Population=None
        return True;  
    
           

    def compute_fitness(self,gene):
        logging.info("Calculating Fitness - started" +str(datetime.now()))
        gene._fitness=self._fitness_fail
        program=gene.local_bnf['program']
        if self._generation > 0:
            program=self.de_EscapeText(gene,program)
            try:
            	prg=beautify(program)
            	program=prg
            except:
            	pass
            
            gene.local_bnf['program']=program
        if len(program) > 0:
            try:
            	f=NamedTemporaryFile(delete=False)
                f.write(program)
                f.close()
                if self.interpreter_Options is not None:
                    option = choice(self.interpreter_Options)
                else:
                    option=""
                timedout=False
                l=[None,None]        
                t=Thread(target=self.run_cmd,kwargs={'fi':f.name,'l':l,'option':option})
                t.start()
                t.join(self.execution_timeout)
                if t.isAlive():
                    if l[0] is not None:
                        logging.info("JS shell execution timeout. Process : "+str(l[0].pid))
                        l[0].kill()
                        kill(l[0].pid, 9)
                        timedout=True
                        sleep(.1)
                else:
                    (out,err,rc)=l[1]
                    gene.err=err
                    if "timeout" in err or "terminating" in err or "out of memory" in err:
                        return
                    if self.interpreterInd==3:

                        if (rc < 0 or rc > 1) and rc != -6 :
                            gene._fitness=self._fitness_fail * (-1)
                            program+="\n//"+option
                            logging.info("Crash:")
                            logging.info("++++++++++++++++++++++++++++++++++++++++")
                            logging.info(program)
                            logging.info("++++++++++++++++++++++++++++++++++++++++")
                            logging.info("error:"+err)
                            logging.info("interpreter:"+self.interpreter_Shell)
                            FILECOUNT = len(listdir(self.targetDirectory))+1 
                            if gene._generation!=0:
                                gene._fitness=self._fitness_fail*(-10)
                            newFile=self.targetDirectory+"/"+str(FILECOUNT)+"_.js"
                            f1=open(newFile,'w')
                            f1.write(program)
                            f1.close
                        else:
                            if rc == 0 :
                                gene._fitness = self.computeSubScore(gene,program,err) - (self.parsimony_constant * gene.prgLength )

                    else:
                        if rc not in [0,1,2,3,4] :
                            gene._fitness=self._fitness_fail * (-1)
                            program+="\n//"+option
                            logging.info("Crash:")
                            logging.info("++++++++++++++++++++++++++++++++++++++++")
                            logging.info(program)
                            logging.info("++++++++++++++++++++++++++++++++++++++++")
                            logging.info("error:"+err)
                            logging.info("interpreter:"+self.interpreter_Shell)
                            FILECOUNT = len(listdir(self.targetDirectory))+1 
                            if gene._generation!=0:
                                gene._fitness=self._fitness_fail*(-10)
                            newFile=self.targetDirectory+"/"+str(FILECOUNT)+"_.js"
                            f1=open(newFile,'w')
                            f1.write(program)
                            f1.close
                        else:
                            if rc != 3 :
                                gene._fitness = self.computeSubScore(gene,program,err) - (self.parsimony_constant * gene.prgLength )
            except: 
                pass
            finally:
                try:
                    logging.info("Calculating Fitness -Done " +str(datetime.now()))
                    remove(f.name)
                except:
                    pass

    def run_cmd(self, fi,l,option):
        try:
            exec_cmd=self.interpreter_Shell+" "+option+" shell.js "+ fi
            p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
            l[0]=p
            out, err = p.communicate()
            l[1]=(out,err,p.returncode)
            sys.stdout.flush()
            sys.stderr.flush()
        except:
            pass
    
    def computeSubScore (self, gene, program,err):
        def handler(signum, frame):
                raise Exception("Function execution timeout")

        signal.signal(signal.SIGALRM, handler)
        if self._generation == 0:
            signal.alarm(6*self.FUNCTION_EXEC_TIMEOUT)
        else:
            signal.alarm(3*self.FUNCTION_EXEC_TIMEOUT)
        logging.info("Invoking Parser - Pasring - Score Calc " +str(datetime.now()))
        incompl,dummy=parseTree(program,True)
        logging.info("Calculating " +str(datetime.now()))
        if self._generation==0:
            gene.prgLength=len(extractNonTerminal(incompl))
        a,b,c,d=CountNestedStructures(incompl)
        logging.info("Completed - Score Calc " +str(datetime.now()))
        
        for temp in a:
            if temp>0:
                temp=temp-1
            gene.score += temp*1.5
        for temp in b:
            if temp>0:
                temp=temp-1
            gene.score += temp*2.5
        for temp in c:
            if temp>0:
                temp=temp-1
            gene.score += temp*1.0
        for temp in d:
            if temp>0:
                temp=temp-1
            gene.score += temp*3
        if "warning" in err:
            logging.info("warning found: "+err)
            gene.score+=10
        return gene.score

    def _perform_endcycle(self):
        self._pre_selected = self._evaluate_fitness(True)

        childList=[]
        for gene in self._pre_selected:
            childList.append(deepcopy(gene))
        fitness_pool = self._evaluate_fitness()
        child_list = self._perform_crossovers(fitness_pool)
        childList.extend(child_list)
        while len(childList) < self._population_size:
                fitness_pool = self._evaluate_fitness()
                child_list = self._perform_mutations(fitness_pool)
                if child_list is not None:
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
        else: 
            total = len(self.population)
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
        # else:
        #     for gene in self.population:
        #         if gene.get_fitness()!=self._fitness_fail:
        #             flist1.append(deepcopy(gene))
        return flist1

    def _perform_crossovers(self, flist):
        child_list = []
        try:
            #this kills entire crossover process; hope it doesnt have much impact
            def handler(signum, frame):
                raise Exception("Function execution timeout")

            signal.signal(signal.SIGALRM, handler)
            signal.alarm(len(flist)*self.FUNCTION_EXEC_TIMEOUT)

            logging.debug("crossover started")
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
                    parent1 = flist[i]
                    flist.remove(parent1)
                    parent2 = flist[i+1]
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
        
                    
                    logging.info("Invoking Parser - Parsing Crossover-1 " +str(datetime.now()))
                    child1ParseTree,child1._identifiers=parseTree(child1Prg,True)
                    non_term1=extractNonTerminal(child1ParseTree)
                    logging.info("Completed - Crossover-1 " +str(datetime.now()))
                    child1.prgLength=len(non_term1)

                    
                    logging.info("Invoking Parser - Parsing Crossover-2 " +str(datetime.now()))
                    child2ParseTree,child2._identifiers=sparseTree(child2Prg,True)
                    non_term2=extractNonTerminal(child2ParseTree)
                    child2.prgLength=len(non_term2)
                    logging.info("Completed - Crossover-2 " +str(datetime.now()))
                    
                    if self.nT_Invld_Gen_Process is not None:
                        commonNonTerm=[val for val in non_term1 if (val in set(non_term2) and val in self.nT_Invld_Gen_Process)]
                    else:
                        commonNonTerm=[val for val in non_term1 if (val in set(non_term2))]
                    trail=0
                    while trail<3:
                        trail += 1
                        count=1
                        if round(random(),1) < self._multiple_rate:
                            count=int(self.crossoverCount*(round(random(),1)))+1        
                        selectedNt=[]
                        if len(commonNonTerm) > 0:
                            for i in range(count):
                                selectedNt.append(choice(commonNonTerm))
                        else:
                            continue
                        logging.info("Invoking Parser - Crossover-3 ")
                        subString1,s1,selected1NTList=genCodeFrag(child1ParseTree,non_term1,selectedNt,None,len(selectedNt))
                        subString2,s2,selected2NTList=genCodeFrag(child2ParseTree,non_term2,selectedNt,None,len(selectedNt))
                        logging.info("Completed - Crossover-3 " +str(datetime.now()))
                        
                        try:
                            for k in selected2NTList:
                                s1 = s1.replace(selected2NTList[k],subString2[k])
                            for k in selected1NTList:
                                s2 = s2.replace(selected1NTList[k],subString1[k])
                            child1Prg_=s1
                            child2Prg_=s2
                        
                        except:
                            continue

                        child1.local_bnf['program']=child1Prg_
                        child1.score=0
                        self.compute_fitness(child1)
                        child2.local_bnf['program']=child2Prg_
                        child2.score=0
                        self.compute_fitness(child2)

                        if child1.get_fitness()!= self._fitness_fail and child2.get_fitness()!= self._fitness_fail:
                            
                            child1.generate_decimal_gene()
                            child1._update_genotype()
                            child1.local_bnf['CodeFrag']=""

                            child2.generate_decimal_gene()
                            child2._update_genotype()
                            child2.local_bnf['CodeFrag']=""

                            if self._children_per_crossover == 2:
                                child_list.append(child1)
                                child_list.append(child2)
                            else:
                                ch=choice([0,1])
                                if ch==0:
                                    child_list.append(child1)
                                else:
                                    child_list.append(child2)
                            logging.info("Crossover-Success")
                        else:
                            logging.info("Crossover-Failed")
                            logging.debug(child1.err)
                            logging.debug(child2.err)
            return child_list
        except:
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

    def mutate(self,gene):
    
        def handler(signum, frame):
            raise Exception("Function execution timeout")
        
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(self.FUNCTION_EXEC_TIMEOUT)
        
        pr=gene.local_bnf['program']
        
        if round(random(),1) < self._mutation_rate :
            logging.debug("mutation started")
            generative=False
            
            
            logging.info("Invoking Parser - Parsing Mutation-1 " +str(datetime.now()))
            incompl, gene._identifiers = parseTree(gene.get_program(),True)
            non_TerminalsList=extractNonTerminal(incompl)
            logging.info("Completed - Mutation-1 " +str(datetime.now()))
            
            if len(non_TerminalsList) >1:

                if round(random(),1) < self._generative_mutation_rate :
                    generative=True
                    gene._max_depth=self._max_depth
                count=1
                if round(random(),1) < self._multiple_rate:
                    count=int(self.mutationCount*round(random(),1))+1
                logging.info("Invoking Parser - Mutation-2 " +str(datetime.now()))
                gene.prgLength=len(non_TerminalsList)
                dummy,gene.local_bnf['CodeFrag'],selectedNt=genCodeFrag(incompl,non_TerminalsList,None,self.nT_Invld_Gen_Process,count)
                logging.info("Completed - Mutation-2 " +str(datetime.now()))
                
                if len(selectedNt) <=0 :
                    logging.info("Mutation-Failed")
                    return None
                # reseting score before mutation
                trail=0
                tmp=gene.local_bnf['CodeFrag']
                while trail < 3:
                    trail+=1
                    gene.local_bnf['CodeFrag']=tmp
                    gene.score=0
                    logging.info("Mutation started " +str(datetime.now()))
                    gene._map_gene(selectedNt)
                    logging.info("Mutation completed " +str(datetime.now()))
                    self.compute_fitness(gene)
                    if gene.get_fitness() != self._fitness_fail :
                        gene.local_bnf['CodeFrag']=""
                        gene.prog_generated = 1
                        logging.info("Mutation-Success")
                        return gene
                    else:
                        logging.info("Mutation-Failed")
                        logging.debug(gene.err)
                        logging.debug(selectedNt)
                        logging.debug(dummy)
                        logging.debug(gene.local_bnf['CodeFrag'])
                        logging.debug(pr)
                        logging.debug(gene.local_bnf['program'])
                        
    
    def _perform_mutations(self, mlist):
        mutatedList=[]
        for gene in mlist:
            try:
                result=self.mutate(gene)
                if result is not None:
                    mutatedList.append(result)
            except:
                logging.info("Function execution timeout")
                pass
        return mutatedList

    def _perform_replacements(self, fitness_pool):
        position = 0
        for gene in self._pre_selected:
            gene.member_no=position
            self.population[position]=gene
            position+=1
        self._pre_selected
        for gene in fitness_pool:
            if position<self._population_size:
                gene.member_no=position
                self.population[position]=gene
                position+=1
            else:
                break
        logging.info("replacement done")
        # for rsel in self.replacement_selections:
        #     rsel.set_fitness_list(self.fitness_list)

        #     for i in rsel.select():
        #         replaced_g = self.population[i]
        #         if position < len(fitness_pool):
        #             newGene = fitness_pool[position]
        #             newGene.member_no = replaced_g.member_no
        #             newGene._generation = self._generation + 1
        #             newGene.local_bnf['<member_no>'] = [newGene.member_no]
        #             self.population[newGene.member_no] = newGene
        #             position += 1
        #         else:
        #             break

    def de_EscapeText(self, gene, string):
        self.identifiers_mapping={}
    	indicator=False
        if len(gene._identifiers)> 0:
            indicator=True
    	wordList=split(VARIABLE_FORMAT, string)
        modifiedWordList=[]
        for word in wordList:
    		if "&lt" in word:
    			word=word.replace("&lt;","<")
    		elif "&gt" in word:
    			word=word.replace("&lt;",">")
    		elif "&quot" in word:
    			word=word.replace("&lt;","\"")
    		elif "&amp" in word:
    			word=word.replace("&lt;","&")
    		elif "&apos" in word:
    			word=word.replace("&apos;","\\")
    		elif "&pipe" in word:
    			word=word.replace("#pipe;","|")
    		elif "_id_" in word:
                    if indicator:
                        if self.identifiers_mapping.has_key(word):
                            word=self.identifiers_mapping[word]
                        else:
                            temp=choice(gene._identifiers).replace("_id_","")
                            self.identifiers_mapping[word]=temp
                            word=temp
                    else:
                        word='a'
    		modifiedWordList.append(word)
        return ''.join(modifiedWordList)

    def _continue_processing(self):
        """
        This method analyzes the fitness list against the stopping_criteria defined over target_value and max generations
        """
        status = True
        fitl = self.fitness_list
        logging.info("mutation_rate:"+str(self._mutation_rate) +",crossover_rate:"+str(self._crossover_rate)+",multiple_rate:"+str(self._multiple_rate))
        logging.info("fitness values : After Generation " + str(self._generation))
        logging.info(self.interpreter_Shell)
        logging.info(fitl)

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
