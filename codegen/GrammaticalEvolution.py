#!/usr/bin/env python
from copy import deepcopy
from datetime import datetime
from os import path,listdir,remove
from random import choice, randint, random
from re import sub,split,findall
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
LOG_LEVEL= config.get('Mappings', 'loglevel');
import logging

logging.basicConfig(filename=LOG_FILENAME,
                    level=LOG_LEVEL,
                    )


VARIABLE_FORMAT = '(\W+)'
VARIABLE_FORMAT1 = '([a-zA-Z0-9_$]+)'
STOPPING_MAX_GEN = 'max_generations'

class GrammaticalEvolution(object):

    def __init__(self):
        self.shrink_mutation_rate=0
        self.FUNCTION_EXEC_TIMEOUT=5
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
        self.crossover_break=False
        self.mutation_break=False
        self.function_break=False
        self.crossover_bias_rate=0

    def set_crossover_bias_rate(self,percentage):
        self.crossover_bias_rate=percentage

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
                remove(fileName)

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

    def set_wrap(self, true_false):
            self._wrap = true_false

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

    def set_maintain_history(self, true_false):
            self._maintain_history = true_false

    def set_max_program_length(self, max_program_length):
        max_program_length = long(max_program_length)
        self._max_program_length = max_program_length

    def set_fitness_fail(self, fitness_fail):
        fitness_fail = float(fitness_fail)
        self._fitness_fail = fitness_fail

    def set_mutation_type(self, mutation_type):
        self._mutation_type = mutation_type

    def set_mutation_rate(self, mutation_rate):
        self._mutation_rate = mutation_rate

    def set_crossover_rate(self, crossover_rate):
        self._crossover_rate = crossover_rate

    def set_children_per_crossover(self, children_per_crossover):
        self._children_per_crossover = children_per_crossover

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
                gene.score=10
                self.compute_fitness(gene)
            self.population[gene.member_no]=gene
            self.fitness_list[gene.member_no][0] = gene.get_fitness()
            totalLength += gene.prgLength
            totalFitness += gene.get_fitness()

        self.meanLength=totalLength/self._population_size
        meanFitness=totalFitness/self._population_size
        varianceValue=variance()
        if varianceValue == 0:
            self.parsimony_constant=0
        else:
            # self.parsimony_constant=abs(calculateCovariance(meanFitness)/varianceValue)
            self.parsimony_constant=calculateCovariance(meanFitness)/varianceValue

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
      
    def create_genotypes(self,file,interpreter_Shell,interpreter_Options,preSelectedNonTerminals,interpreterInd):
        self.interpreter_Shell=interpreter_Shell
        self.interpreter_Options =interpreter_Options
        self.interpreterInd=interpreterInd
        self.nT_Invld_Gen_Process=preSelectedNonTerminals
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
            gene.preSelectedNonTerminals=preSelectedNonTerminals
            gene._initial_member_no =  member_no
            member_no += 1
            gene.local_bnf["program"]=self.initial_Population[gene.member_no]
            self.population.append(gene)
        self.initial_Population=None
        return True;  
    
           

    def compute_fitness(self,gene,prgLength=None):
        logging.info("compute_fitness entered")
        ti=time()
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
        prglen=len(program)
        if prglen > 0:
            try:
                f=NamedTemporaryFile(delete=False)
                f.close()
                if self.interpreter_Options is not None:
                    option = choice(self.interpreter_Options)
                else:
                    option=""
                timedout=False
                while prglen>0:
                    prglen -= 1
                    tempFileObj=open(f.name,"w")
                    tempFileObj.write(program)
                    tempFileObj.close()
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
                        gene.rc=rc
                        # Eliminating reference error; JS support hostilling
                        if 'ReferenceError:' in err:
                            if self._generation==0:
                                break
                            words=err.split()
                            nextword=words[words.index('ReferenceError:')+1]
                            if nextword == 'invalid' or nextword ==  'reference' :
                                return 
                            selected=None
                            while nextword == selected or selected is None:
                                if len(gene._identifiers)<0:
                                    break
                                selected=choice(gene._identifiers)
                                gene._identifiers.remove(selected)
                            logging.info("Replacing "+nextword+" with "+selected)
                            if nextword == selected or selected is None:
                                break
                            
                            newWordList=[]
                            wordList=split(VARIABLE_FORMAT1, program)
                            for word in wordList:
                                if word == nextword:
                                    newWordList.append(selected)
                                else:
                                    newWordList.append(word)
                            logging.info("Replaced "+nextword+" with "+selected)
                            program=''.join(newWordList)
                            gene.local_bnf['program'] = program
                        else:
                            break
                if timedout:
                    return
                if "timeout" in err or "terminating" in err or "out of memory" in err:
                    return
                if self.interpreterInd==3:
                    if (rc < 0 or rc > 1) and rc != -6 :
                        program+="\n//"+option + "\n//" + err.replace("\n"," ")
                        logging.info("Crash:")
                        logging.info("Interpreter:"+self.interpreter_Shell)
                        logging.info("Error:"+err)
                        logging.info("TimeStamp:" + str(datetime.now()))
                        logging.info("++++++++++++++++++++++++++++++++++++++++")
                        logging.info(program)
                        logging.info("++++++++++++++++++++++++++++++++++++++++")
                        FILECOUNT = len(listdir(self.targetDirectory))+1 
                        if gene._generation!=0:
                            gene._fitness=self._fitness_fail
                        newFile=self.targetDirectory+"/"+str(FILECOUNT)+"_.js"
                        f1=open(newFile,'w')
                        f1.write(program)
                        f1.close
                    else:
                        if rc == 0 :
                            gene.score += self.computeSubScore(gene,program,err)
                            if gene.score is not None:
                                if self._generation==0:
                                    gene._fitness =  gene.score
                                else:
                                    if prgLength is not None:
                                        if (gene.prgLength/prgLength) > (self.crossover_bias_rate/100):
                                            return
                                    gene._fitness =  gene.score - (self.parsimony_constant * gene.prgLength )

                else:
                    if rc != 0 and rc != 3:
                        program+="\n//"+option + "\n//" + err.replace("\n"," ")
                        logging.info("Crash:")
                        logging.info("Interpreter:"+self.interpreter_Shell)
                        logging.info("Error:"+err)
                        logging.info("TimeStamp:" + str(datetime.now()))
                        logging.info("++++++++++++++++++++++++++++++++++++++++")
                        logging.info(program)
                        logging.info("++++++++++++++++++++++++++++++++++++++++")
                        FILECOUNT = len(listdir(self.targetDirectory))+1 
                        gene._fitness=self._fitness_fail
                        newFile=self.targetDirectory+"/"+str(FILECOUNT)+"_.js"
                        f1=open(newFile,'w')
                        f1.write(program)
                        f1.close
                    else:
                        if rc!=3 :
                            gene.score=self.computeSubScore(gene,program,err)
                            if gene.score is not None:
                                if self._generation==0:
                                    gene._fitness =  gene.score
                                else:
                                    if prgLength is not None:
                                        if (gene.prgLength/prgLength) > (self.crossover_bias_rate/100):
                                            return
                                    gene._fitness =  gene.score - (self.parsimony_constant * gene.prgLength )
            except:
                pass
            finally:
                try:
                    logging.info("Calculating Fitness - Completed in " +str(time()-ti)+" seconds")
                    remove(f.name)
                except:
                    pass
        logging.info("compute_fitness completed")

    def run_cmd(self, fi,l,option):
        try:
            exec_cmd=self.interpreter_Shell+" "+option+" shell.js " + fi
            p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
            l[0]=p
            out, err = p.communicate()
            l[1]=(out,err,p.returncode)
            sys.stdout.flush()
            sys.stderr.flush()
        except:
            pass
    
    def computeSubScore (self, gene, program,err):
        try:
            score=0.0
            logging.info("Inside computeSubScore method")
            ti=time()
            incompl,dummy,exec_time=parseTree(program,True)
            res=findall('(<)([a-zA-Z]+)(><\/)+([a-zA-Z]+)(>)',incompl)
            if len(res) > 0:
                print "computeSubScore-rejection"
                return None
            logging.info("Score Calc: Invoked parser for " +str(time()-ti) +" seconds")
            gene.prgLength=len(extractNonTerminal(incompl,[]))
            score= -float(exec_time)/gene.prgLength
            a,b,c,d=CountNestedStructures(incompl)
            logging.info("Completed - Score Calc in " +str(time()-ti) + " seconds")
            
            for temp in a:
                if temp>0:
                    temp=temp-1
                score += temp*1.0
            for temp in b:
                if temp>0:
                    temp=temp-1
                score += temp*1.0
            for temp in c:
                if temp>0:
                    temp=temp-1
                score += temp*1.0
            for temp in d:
                if temp>0:
                    temp=temp-1
                score += temp*1
            if "warning" in err:
                logging.info("warning found: "+err)
                score+=10
            logging.info("exiting computeSubScore method")
        except:
            return None
        finally:
            return score

    def _perform_endcycle(self):
        self._pre_selected = self._evaluate_fitness(True)
        childList=[]
        # for gene in self._pre_selected:
        #     childList.append(deepcopy(gene))
        remainingPopCount = self._population_size - len(self._pre_selected)
        while len(childList) < remainingPopCount:
            if round(random(),1) <= 0.7:
                limitSelection=True
            else:
                limitSelection=False
            ch=choice([0,1])
            ch=0
            if ch==0:
                logging.info("performing crossover and mutation")
                fitness_pool = self._evaluate_fitness(False,limitSelection)
                child_list = self._perform_crossovers(fitness_pool)
                if child_list is not None:
                	childList.extend(child_list)   
                fitness_pool = self._evaluate_fitness()
                child_list = self._perform_mutations(fitness_pool,(remainingPopCount-len(childList)))
                if child_list is not None:
                    childList.extend(child_list)
            else:
                logging.info("performin mutation and crossover")
                fitness_pool = self._evaluate_fitness()
                child_list = self._perform_mutations(fitness_pool,(remainingPopCount-len(childList)))
                if child_list is not None:
                    childList.extend(child_list)
                    
                fitness_pool = self._evaluate_fitness(False,limitSelection)
                child_list = self._perform_crossovers(fitness_pool)
                if child_list is not None:
                	childList.extend(child_list)    
        self._perform_replacements(childList)

    """
        if ind=True; certain num of indv are selected based on max fitness rate (say m). These are included in offspring list.

        remianing individuals max_pop - m are selected which includes these m indiv undergo crossover and mutation
        m+(n-m) = n (new offspring are generated which represents next generations)
    """
    def _evaluate_fitness(self,ind=False,limitSelection=False): 
        flist = []
        flist1 = []
        if ind:
            total = int(round(self._max_fitness_rate * float(self._population_size)))
        else: 
            total = len(self.population)
        count = 0
        if limitSelection or ind:
            for fsel in self.fitness_selections:
                fsel.set_fitness_list(self.fitness_list)
                selected=fsel.select()
                for i in selected:
                    if count == total:
                        break
                    flist.append(i)
                    count += 1
            for member_no in flist:
                gene=self.population[member_no]
                if gene._fitness!=self._fitness_fail:
                    flist1.append(deepcopy(gene))
        else:
            for gene in self.population:
                if gene._fitness!=self._fitness_fail:
                    flist1.append(deepcopy(gene))
        return flist1

    def _perform_crossovers(self, flist):
        logging.info("Crossover: Started")
        ti=time()
        child_list = []
        try:
            
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
                while len(flist) >=2 :
                # for i in xrange(0, length, 2):
                    # parent1 = flist[i]
                    # flist.remove(parent1)
                    # parent2 = flist[i+1]
                    # flist.remove(parent2)
                    parent1 = choice(flist)
                    parent2 = choice(flist)
                    flist.remove(parent1)
                    flist.remove(parent2)

                    if randint(0, 1):
                            child1 = (parent1)
                            child2 = (parent2)
                    else:
                            child1 = (parent2)
                            child2 = (parent1)
                    
                    child1_binary = child1.binary_gene
                    child2_binary = child2.binary_gene
                    
                    child1Prg=child1.get_program()
                    child2Prg=child2.get_program()
        
            
                    ti1=time()
                    child1ParseTree,child1._identifiers,exec_time=parseTree(child1Prg,True)
                    res=findall('(<)([a-zA-Z]+)(><\/)+([a-zA-Z]+)(>)',child1ParseTree)
                    if len(res) > 0:
                        print "crossover1-rejection"
                        continue
                    non_term1=extractNonTerminal(child1ParseTree,[])
                    logging.info("Invoked parser - Crossover-1 for " +str(time()-ti1) +" seconds")
                    child1.prgLength=len(non_term1)

                    
                    ti2=time()
                    child2ParseTree,child2._identifiers,exec_time=parseTree(child2Prg,True)
                    res=findall('(<)([a-zA-Z]+)(><\/)+([a-zA-Z]+)(>)',child2ParseTree)
                    if len(res) > 0:
                        print "crossover2-rejection"
                        continue
                    non_term2=extractNonTerminal(child2ParseTree,[])
                    child2.prgLength=len(non_term2)
                    logging.info("Invoked parser - Crossover-2 for " +str(time()-ti2)+" seconds")

                    
                    if self.nT_Invld_Gen_Process is not None:
                        commonNonTerm=[val for val in non_term1 if (val in set(non_term2) and val in self.nT_Invld_Gen_Process)]
                    else:
                        commonNonTerm=[val for val in non_term1 if (val in set(non_term2))]
                    
                    trail=0
                    while trail<5:
                        trail += 1
                        count=1
                        if round(random(),1) < self._multiple_rate:
                            count=int(self.crossoverCount*(round(random(),1)))+1        
                        selectedNt=[]
                        if len(commonNonTerm) > 0:
                            for i in range(count):
                                selectedNt.append(choice(commonNonTerm))
                        else:
                            break
                        ti3=time()
                        subString1,s1,selected1NTList=genCodeFrag(child1ParseTree,non_term1,selectedNt,None,len(selectedNt))
                        subString2,s2,selected2NTList=genCodeFrag(child2ParseTree,non_term2,selectedNt,None,len(selectedNt))
                        logging.info("Invoked Parser - Crossover-SubCode for " +str(time()-ti3)+" seconds")
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
                        child1.score=10
                        self.compute_fitness(child1,len(non_term1))
                        child2.local_bnf['program']=child2Prg_
                        child2.score=10
                        self.compute_fitness(child2,len(non_term1))

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
                            break;
                        else:
                            logging.info("Crossover-Failed")
                            # if child1.get_fitness()== self._fitness_fail and child1.rc != 3:
                            #     logging.info(child1.local_bnf['program'])
                            # if child2.get_fitness()== self._fitness_fail and child2.rc != 3:
                            #     logging.info(child2.local_bnf['program'])
                            child1.local_bnf['program']=child1Prg
                            child2.local_bnf['program']=child2Prg
                            logging.debug(child1.err)
                            logging.debug(child1.rc)
                            logging.debug(child2.err)
                            logging.debug(child2.rc)
                        logging.debug(subString1)
                        logging.debug(subString2)
                    if len(child_list) == length:
                        return child_list
            
        except:
            logging.info("Crossover Completed in "+str(time()-ti))
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
        try:
            pr=gene.local_bnf['program']
            
            if round(random(),1) < self._mutation_rate :
                logging.debug("mutation started")
                generative=False
                shrink=False
                
                ti1=time()
                incompl, gene._identifiers,exec_time = parseTree(gene.get_program(),True)
                res=findall('(<)([a-zA-Z]+)(><\/)+([a-zA-Z]+)(>)',incompl)
                if len(res) > 0:
                    print "mutation-rejection"
                    return None
                non_TerminalsList=extractNonTerminal(incompl,[])
                logging.info("Invoked parser - Mutation-1 for " +str(time()-ti1)+" seconds")
                count=1

                if len(non_TerminalsList) > 1:

                    if round(random(),1) < self._generative_mutation_rate :
                        generative=True
                        gene._max_depth=self._max_depth
                    
                    if round(random(),1) < self._multiple_rate:
                        count=int(self.mutationCount*round(random(),1))+1

                    if round(random(),1) < self.shrink_mutation_rate:
                        shrink=True
                    ti2=time()
                    gene.prgLength=len(non_TerminalsList)
                    trail=0
                
                    while trail < 3:
                        trail+=1
                        logging.info("Invoked parser - Mutation-SubCode for " +str(time()-ti2)+" seconds")
                        dummy,gene.local_bnf['CodeFrag'],selectedNt=genCodeFrag(incompl,non_TerminalsList,None,self.nT_Invld_Gen_Process,count)
                        logging.info("Invoked parser - Mutation-SubCode for " +str(time()-ti2)+" seconds")
                        
                        if len(selectedNt) <=0 :
                            logging.info("Mutation-Failed")
                            return None
                        if shrink:
                            for val in selectedNt.values():
                                gene.local_bnf['CodeFrag'].replace(val,'')
                            break

                        tmp=gene.local_bnf['CodeFrag']
                        gene.local_bnf['CodeFrag']=tmp
                        gene.score=10
                        ti3=time()
                        gene._map_gene(selectedNt)
                        logging.info("Mutation completed " +str(time()-ti3))
                        logging.debug(dummy)
                        self.compute_fitness(gene)
                        if gene.get_fitness() != self._fitness_fail :
                            gene.local_bnf['CodeFrag']=""
                            gene.prog_generated = 1
                            logging.info("Mutation-Success")
                            break
                        else:
                            gene.local_bnf['program']=pr
                            logging.info("Mutation-Failed")
                            # if gene.get_fitness()== self._fitness_fail and gene.rc != 3:
                            #     logging.info(gene.local_bnf['CodeFrag'])
                            logging.debug(selectedNt)
                            logging.debug(dummy)
                            logging.debug(gene.local_bnf['CodeFrag'])
                            logging.debug(pr)
                            logging.debug (gene.err)
                            logging.debug(gene.rc)
        except:
            pass
        finally:
            return gene               
    
    def _perform_mutations(self, mlist, count):
        mutatedList=[]
        for gene in mlist:
            try:
                result=self.mutate(gene)
                if result is not None:
                    mutatedList.append(result)
                    mlist.remove(gene)
                if len(mutatedList) == count:
                    return mutatedList
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
        
        for gene in fitness_pool:
            if position<self._population_size:
                gene.member_no=position
                self.population[position]=gene
                position+=1
            else:
                break
        logging.info("replacement done")

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
            elif "timeout" in word:
                    if indicator:
                        if self.identifiers_mapping.has_key(word):
                            word=self.identifiers_mapping[word]
                        else:
                            temp=choice(gene._identifiers).replace("timeout","")
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
        s=set()
        for i in range(len(fitl)):
            s.add(fitl[i][0])
        logging.info(self.interpreter_Shell)
        logging.info("Mutation_rate:"+str(self._mutation_rate) +",crossover_rate:"+str(self._crossover_rate)+",multiple_rate:"+str(self._multiple_rate))
        logging.info("Unique: "+str(len(s)) +" Genotype Objects based on Fitness")
        logging.info("Fitness values : After Generation " + str(self._generation))
        logging.info(fitl)
        
        if self.stopping_criteria[STOPPING_MAX_GEN] is not None:
            if self.stopping_criteria[STOPPING_MAX_GEN] <= self._generation:
                return False
        if fitl.get_target_value() is not None:
                if fitl.best_value() == fitl.get_target_value():
                    return False
        return status
