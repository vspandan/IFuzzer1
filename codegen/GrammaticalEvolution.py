#!/usr/bin/env python
from copy import deepcopy
from threading import Thread
from datetime import datetime
from os import path,listdir,remove,kill
from random import choice, randint, random
from re import sub,split,findall
from subprocess import Popen,PIPE
from langparser.AntlrParser import *
from codegen.fitness import CENTER, MAX, MIN
from codegen.fitness import FitnessList, Fitness, Replacement
from codegen.Genotypes import Genotype
from time import time,sleep
from jsbeautifier import beautify
from tempfile import NamedTemporaryFile

import tests.jit_test
import signal 
import ConfigParser
import logging

config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
LOG_LEVEL= config.get('Mappings', 'loglevel');

logging.basicConfig(filename=LOG_FILENAME,level=LOG_LEVEL,)

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
        self.parsimony_constant=0
        self.meanLength=1
        self.crossover_break=False
        self.mutation_break=False
        self.function_break=False
        self.crossover_bias_rate=0
        self.targetDir=config.get('TargetDir', 'BUGSDIR')
        self.getMetricNonTerminals()

    def getMetricNonTerminals(self):
        logging.info("getMetricNonTerminals Started")
        nonTerminalListStr= config.get('Interpreter', 'METRICS_NON_TEMINALS')
        nonTermList=nonTerminalListStr.split(",")
        self.metricNonTerm={}
        for nonTerm in nonTermList:
            splitValues=nonTerm.split(":")
            self.metricNonTerm[splitValues[0]]=float(splitValues[1])
        logging.info("getMetricNonTerminals Completed")

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

    def calcfitness(self):
        logging.info("calcfitness Started")
        self.meanLength=1
        
        def calculateCovariance(meanFitness):
            logging.info("calculateCovariance Started")
            value=0
            for gene in self.population:
                value += ( gene.get_fitness() - meanFitness ) * ( gene.prgLength - self.meanLength )
            logging.info("calculateCovariance Completed")
            return value

        def variance():
            logging.info("variance Started")
            value=0
            for gene in self.population:
                value += ( gene.prgLength - self.meanLength ) ** 2 
            logging.info("variance Completed")
            return value
        
        totalLength=0
        totalFitness=0.0
        for gene in self.population:
            starttime = datetime.now()
            gene._generation = self._generation
            gene.starttime = starttime
            gene.set_keys (self.non_Terminals)
            if self._generation == 0 :
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
            self.parsimony_constant=calculateCovariance(meanFitness)/varianceValue
        logging.info("calcfitness Completed")

    def run(self, starting_generation=0):
        logging.info("Starting Code Generation Process")
        self._generation = starting_generation
        starttime=time()
        self.calcfitness()
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
                self.calcfitness()
            else:
                break
            diff=round((time()-starttime))
            logging.info("completed : "+str(self._generation)+" in "+str(diff) + " seconds")
        logging.info("Completed Code Generation Process")
      
    def create_genotypes(self,fileList,interpreter_Shell,interpreter_Options,interpreter_ReturnCodes,preSelectedNonTerminals,shellfileOption):
        logging.info("create_genotypes Started")
        self.interpreter_Shell=interpreter_Shell
        self.shellfileOption=shellfileOption
        self.interpreter_Options =interpreter_Options
        self.interpreter_ReturnCodes=interpreter_ReturnCodes
        self.nT_Invld_Gen_Process=preSelectedNonTerminals
        self._extractProductions()
        
        if len(fileList)<self._population_size:
            logging.info("create_genotypes Completed")
            return
        member_no = 0
        
        while member_no < self._population_size:
            gene = Genotype(member_no)
            gene.local_bnf = deepcopy(self._bnf)
            gene.local_bnf['<member_no>'] = [gene.member_no]
            gene.keywords=self._bnf['keyword']+self._bnf['futureReservedWord']
            gene.preSelectedNonTerminals=preSelectedNonTerminals
            gene._initial_member_no =  member_no
            
            f=open(path.abspath(fileList[member_no]),"r")
            program=f.read()
            f.close()
            
            gene.origin=fileList[member_no]
            gene.evolutionGraph.append(fileList[member_no])
            gene.local_bnf["program"]=program
            gene.syntaxTree,gene._identifiers,dummy2=parseTree(program)
            gene.non_term=extractNonTerminal(gene.syntaxTree,[])
            self.population.append(gene)
            
            member_no += 1
        logging.info("create_genotypes Completed")
        return True;  
    
    def checkNResolveRefError(self, out, err):
        logging.info("checkNResolveRefError Started")
        if 'ReferenceError:' in err or 'ReferenceError' in out:
            if self._generation==0:
                logging.info("checkNResolveRefError Completed")
                return False
            words=err.split()
            nextword=words[words.index('ReferenceError:')+1]
            logging.info("Reference Error - Returning")
            if nextword == 'invalid' or nextword ==  'reference' :
                logging.info("checkNResolveRefError Completed")
                return 
            selected=None
            while nextword == selected or selected is None:
                if len(gene._identifiers)<0:
                    return False
                selected=choice(gene._identifiers)
                gene._identifiers.remove(selected)
            logging.info("Replacing "+nextword+" with "+selected)
            if nextword == selected or selected is None:
                logging.info("checkNResolveRefError Completed")
                return False
            
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
            logging.info("checkNResolveRefError Completed")
            return True
        logging.info("checkNResolveRefError Completed")
        return False

    def logBug(self,program,shell,option,err):
        logging.info("logBug Completed")
        program+="\n//"+shell+"\n//"+option + "\n//" + str(datetime.now()) + "\n//" + err.replace("\n"," ") +"\n//Generation:"+str(self._generation)
        logging.info("Crash:")
        logging.info(program)
        FILECOUNT = len(listdir(self.targetDir))
        newFile=self.targetDir+"/"+str(FILECOUNT)+".js"
        f1=open(newFile,'w')
        f1.write(program)
        f1.close
        logging.info("logBug Completed")

    def compute_fitness(self,gene):
        logging.info("compute_fitness started")
        ti=time()
        flag=True;
        gene._fitness=self._fitness_fail
        program=gene.local_bnf['program']
        if self._generation > 0:
            program=self.de_EscapeText(gene,program)
            try:
                program=beautify(program)
            except:
                pass
            gene.local_bnf['program']=program

        if len(program) > 0:
            try:
                f=NamedTemporaryFile(delete=False)
                f.close()
                refError=False
                while True:
                    tempFileObj=open(f.name,"w")
                    tempFileObj.write(program)
                    tempFileObj.close()
                    l=[None,None]
                    t=Thread(target=self.run_cmd,kwargs={'fi':f.name,'l':l,'option':self.interpreter_Options[0][0],'shellNum':0})
                    t.start()
                    t.join(self.execution_timeout)
                    if t.isAlive():
                        if l[0] is not None:
                            l[0].kill()
                            kill(l[0].pid, 9)
                            sleep(.1)
                            logging.info("compute_fitness completed - Killed timeout process"+str(time()-ti)+" seconds")
                        return
                    else:
                        (out,err,rc)=l[1]
                        if not self.checkNResolveRefError(out,err):
                            refError=False
                            break;
                        else:
                            refError=True
                if refError :
                    logging.info("compute_fitness completed - Reference Error"+str(time()-ti)+" seconds")
                    return
                execStart=time()
                for a in range(len(self.interpreter_Shell)):
                    for option in self.interpreter_Options[a]:

                        l=[None,None]        
                        t=Thread(target=self.run_cmd,kwargs={'fi':f.name,'l':l,'option':option, 'shellNum':a})
                        t.start()
                        t.join(self.execution_timeout)
                        if t.isAlive():
                            if l[0] is not None:
                                l[0].kill()
                                kill(l[0].pid, 9)
                                sleep(.1)
                                logging.info("compute_fitness completed - Killed timeout process"+str(time()-ti)+" seconds")
                            return
                        (out,err,rc)=l[1]
                        if rc not in self.interpreter_ReturnCodes[a]:
                            self.logBug(program,self.interpreter_Shell[a],option,err)

                score,prgLength = self.computeSubScore(gene,program,err,time()-execStart)
                gene.score+=score
                if gene.score is not None:
                    if self._generation==0:
                        gene._fitness =  gene.score
                    elif (gene.prgLength/prgLength) < (self.crossover_bias_rate/100):
                            gene._fitness =  gene.score - (self.parsimony_constant * gene.prgLength )
            finally:
                try:
                    logging.info("compute_fitness completed"+str(time()-ti)+" seconds")
                    remove(f.name)
                except:
                    pass
        
    
    def run_cmd(self, fi,l,option,shellNum):
        logging.info("run_cmd started")
        try:
            cmd=[]
            cmd.append(self.interpreter_Shell[shellNum].strip())
            opt=option.strip();
            if len(opt)>0:
                cmd=cmd+opt.split()
            if len(self.shellfileOption[shellNum])>0:
                cmd=cmd+self.shellfileOption[shellNum]
            cmd.append(fi)
            p = Popen(cmd, stdout=PIPE,stderr=PIPE)
            l[0]=p
            out, err = p.communicate()
            l[1]=(out,err,p.returncode)
            sys.stdout.flush()
            sys.stderr.flush()
        except:
            pass
        logging.info("run_cmd completed")

    def computeSubScore (self, gene, program,err,exec_time):
        logging.info("computeSubScore started")
        try:
            score=0.0
            ti=time()
            #TODO calc programlength using cyclic complexity
            prgLength=len(program.split())
            score= -float(exec_time)/prgLength
            nonTerminalsMeticsInfo=CountNestedStructures(gene.syntaxTree,self.metricNonTerm.keys())
            for a in nonTerminalsMeticsInfo.keys():
                for temp in a:
                    score += temp*self.metricNonTerm[a]
            if "warning" in err:
                logging.info("warning found: "+err)
                score+=10
        except:
            pass
        logging.info("computeSubScore completed")
        return score,prgLength

    def _perform_endcycle(self):
        logging.info("performing crossover and mutation")
        self._pre_selected = self._evaluate_fitness(True)
        childList=[]
        remainingPopCount = self._population_size - len(self._pre_selected)
        while len(childList) < remainingPopCount:
            if round(random(),1) <= 0.7:
                limitSelection=True
            else:
                limitSelection=False
            ch=choice([0,1])
            ch=0
            if ch==0:
                fitness_pool = self._evaluate_fitness(False,limitSelection)
                child_list = self._perform_crossovers(fitness_pool)
                if child_list is not None:
                	childList.extend(child_list)   
                fitness_pool = self._evaluate_fitness()
                child_list = self._perform_mutations(fitness_pool,(remainingPopCount-len(childList)))
                if child_list is not None:
                    childList.extend(child_list)
            else:
                fitness_pool = self._evaluate_fitness()
                child_list = self._perform_mutations(fitness_pool,(remainingPopCount-len(childList)))
                if child_list is not None:
                    childList.extend(child_list)
                    
                fitness_pool = self._evaluate_fitness(False,limitSelection)
                child_list = self._perform_crossovers(fitness_pool)
                if child_list is not None:
                	childList.extend(child_list)    
        self._perform_replacements(childList)
        logging.info("completed performing crossover and mutation")

    def _evaluate_fitness(self,ind=False,limitSelection=False): 
        logging.info("_evaluate_fitness started")
        parentlist = []
        parentlist1 = []
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
                    parentlist.append(i)
                    count += 1
            for member_no in parentlist:
                gene=self.population[member_no]
                if gene._fitness!=self._fitness_fail:
                    parentlist1.append(deepcopy(gene))
        else:
            for gene in self.population:
                if gene._fitness!=self._fitness_fail:
                    parentlist1.append(deepcopy(gene))
        logging.info("_evaluate_fitness completed")
        return parentlist1

    def _perform_crossovers(self, parentlist):
        logging.info("_perform_crossovers started")
        ti=time()
        child_list = []
        try:
            length = int(round(self._crossover_rate * float(self._population_size)))
            """
            If no of fitness selections is less than no of indv undergoing crossover, than only no equal to no of fitness selections are allowed to undergo process.
            """
            if len(parentlist) < length:
                length=len(parentlist)
            if length % 2 == 1:
                length -= 1
            if length >= 2:
                while len(parentlist) >=2 :
                    child1 = choice(parentlist)
                    child2 = choice(parentlist)
                    
                    parentlist.remove(child1)
                    parentlist.remove(child2)

                    child1Prg=child1.get_program()
                    child2Prg=child2.get_program()

                    child1.prgLength=len(child1Prg.split())
                    child2.prgLength=len(child2Prg.split())
        
                    if self.nT_Invld_Gen_Process is not None:
                        commonNonTerm=[val for val in child1.non_term if (val in set(child2.non_term) and val in self.nT_Invld_Gen_Process)]
                    else:
                        commonNonTerm=[val for val in child1.non_term if (val in set(child2.non_term))]
                    
                    trail=0
                    while trail<5:
                        trail += 1
                        count=1
                        if round(random(),1) < self._multiple_rate:
                            count=int(self.crossoverCount*(round(random(),1)))+1
                        
                        if len(commonNonTerm) < 0:
                            break
                        et1 = ElementTree.fromstring(child1.syntaxTree)
                        et2 = ElementTree.fromstring(child2.syntaxTree)

                        parent_map1 = dict((c, p) for p in et1.getiterator() for c in p)
                        parent_map2 = dict((c, p) for p in et2.getiterator() for c in p)
                        
                        for i in range(count):
                            k=choice(commonNonTerm)
                            li1= et1.findall('.//'+k)
                            li2= et2.findall('.//'+k)
                            selectedXMLNode1= random.choice(li)
                            selectedXMLNode2= random.choice(li1)

                            parent = parent_map1[selectedXMLNode1]
                            index = parent._children.index(selectedXMLNode1)
                            parent._children[index] = selectedXMLNode2

                            parent = parent_map2[selectedXMLNode2]
                            index = parent._children.index(selectedXMLNode2)
                            parent._children[index] = selectedXMLNode1
                            
                        p1=ProgramGen()
                        p2=ProgramGen()

                        child1.local_bnf['program']=p1.treeToProg(et1)
                        child2.local_bnf['program']=p2.treeToProg(et2)

                        child1.score=10
                        child2.score=10

                        self.compute_fitness(child1)
                        self.compute_fitness(child2)

                        if child1.get_fitness()!= self._fitness_fail and child2.get_fitness()!= self._fitness_fail:
                            
                            child1.syntaxTree=et1
                            child2.syntaxTree=et2
                            child1.non_term=extractNonTerminal(et1,[])
                            child2.non_term=extractNonTerminal(et2,[])

                            if self._children_per_crossover == 2:
                                child_list.append(child1)
                                child_list.append(child2)
                            else:
                                child_list.append(child1)
                            logging.info("Crossover-Success")
                            break;
                        else:
                            logging.info("Crossover-Failed")
                            child1.local_bnf['program']=child1Prg
                            child2.local_bnf['program']=child2Prg
                    if len(child_list) == length:
                        logging.info("_perform_crossovers completed")
                        return child_list
            
        except:
            logging.info("_perform_crossovers completed")
            return child_list

    def genIncompleteSyntaxTree(self,gene,count):
        logging.info("genIncompleteSyntaxTree started")
        et1 = ElementTree.fromstring(gene.syntaxTree)
        parent_map1 = dict((c, p) for p in et1.getiterator() for c in p)
        selectedNt=[]
        i=0;
        while i<count:
            k=choice(gene.non_term)
            li= et1.findall('.//'+k)
            if len(li)>0:
                selectedNt.append(k)
                selectedXMLNode1= choice(li)
                etTemp = ElementTree.fromstring("<MutationNode> "+k+" </MutationNode>")
                print k
                print selectedXMLNode1
                t1=ProgramGen()
                print t1.treeToProg(selectedXMLNode1)
                parent = parent_map1[selectedXMLNode1]
                index = parent._children.index(selectedXMLNode1)
                parent._children[index] = etTemp
                i+=1
        t=ProgramGen()
        logging.info("genIncompleteSyntaxTree completed")
        return t.treeToProg(et1),selectedNt

            
    def mutate(self,gene):
        try:
            logging.info("mutate started")
            pr=gene.local_bnf['program']
            ti3=time()
            if round(random(),1) < self._mutation_rate :
                generative=False
                shrink=False

                count=1
                if len(gene.non_term) > 1:
                    if round(random(),1) < self._generative_mutation_rate :
                        generative=True
                        gene._max_depth=self._max_depth
                    
                    if round(random(),1) < self._multiple_rate:
                        count=int(self.mutationCount*round(random(),1))+1

                    if round(random(),1) < self.shrink_mutation_rate:
                        shrink=True
                    
                    gene.prgLength=len(gene.get_program().split())
                    trail=0
                
                    while trail < 3:
                        trail+=1
                        gene.local_bnf['CodeFrag'],selectedNt=self.genIncompleteSyntaxTree(gene,count)
                        print gene.local_bnf['CodeFrag']

                        if len(selectedNt) <=0 :
                            logging.info("Mutation-Failed-Not selected any non-terminal")
                            return None
                
                        if shrink:
                            for val in selectedNt:
                                gene.local_bnf['CodeFrag'].replace(val,'')
                            break

                        gene.score=10
                        
                        gene._map_gene(selectedNt)
                        raw_input()
                        self.compute_fitness(gene)
                        if gene.get_fitness() != self._fitness_fail:
                            gene.syntaxTree,gene._identifiers,dummy2=parseTree(program)
                            gene.non_term=extractNonTerminal(gene.syntaxTree,[])
                            logging.info("Mutation-Success")
                            break
                        else:
                            gene.local_bnf['program']=pr
                            logging.info("Mutation-Failed")
        except:
            pass
        logging.info("mutate completed" +str(time()-ti3))
        return gene               
    
    def _perform_mutations(self, mlist, count):
        logging.info("_perform_mutations started")
        mutatedList=[]
        for gene in mlist:
            try:
                result=self.mutate(gene)
                if result is not None:
                    mutatedList.append(result)
                    mlist.remove(gene)
                if len(mutatedList) == count:
                    break
            except:
                pass
        logging.info("_perform_mutations completed")
        return mutatedList

    def _perform_replacements(self, fitness_pool):
        logging.info("_perform_replacements started")
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
        logging.info("_perform_replacements completed")

    def de_EscapeText(self, gene, string):
        logging.info("de_EscapeText started")
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
                word=word.replace("&gt;",">")
            elif "&quot" in word:
                word=word.replace("&quot;","\"")
            elif "&amp" in word:
                word=word.replace("&amp;","&")
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
            elif "quit" in word:
                    if indicator:
                        if self.identifiers_mapping.has_key(word):
                            word=self.identifiers_mapping[word]
                        else:
                            temp=choice(gene._identifiers).replace("quit","")
                            self.identifiers_mapping[word]=temp
                            word=temp
                    else:
                        word='a'
            modifiedWordList.append(word)
        logging.info("de_EscapeText completed")
        return ''.join(modifiedWordList)

    def _continue_processing(self):
        logging.info("_continue_processing started")
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
        logging.info(str(datetime.now()))
        logging.info(fitl)
        
        if self.stopping_criteria[STOPPING_MAX_GEN] is not None:
            if self.stopping_criteria[STOPPING_MAX_GEN] <= self._generation:
                logging.info("_continue_processing completed")
                return False
        if fitl.get_target_value() is not None:
                if fitl.best_value() == fitl.get_target_value():
                    logging.info("_continue_processing completed")
                    return False
        logging.info("_continue_processing completed")
        return status