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
        self._pre_selected = []
        self.history = []
        self.population = []
        parser = None
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
        self._multiple_rate = 0
        self.fitness_list_history = []
        self._max_depth = 0
        self._generative_mutation_rate=0.5
        self.identifiers_mapping={}
        self.targetDirectory=""

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
    
    def parseCode(self,codeFragment):
    	parser = AntlrParser()
    	parseCode,identifiers=parser.parseTree(codeFragment,True)
    	parser = None
        return parseCode,identifiers
    
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
                logging.debug("evaluating" + str(gene.member_no))
                logging.debug(gene.local_bnf["program"])
                self.compute_fitness(gene, True)

            self.population[gene.member_no]=gene
            self.fitness_list[gene.member_no][0] = gene.get_fitness()

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
                        member_no,interpreter_Shell,interpreter_Options)
            gene.local_bnf = deepcopy(self._bnf)
            gene.local_bnf['<member_no>'] = [gene.member_no]
            gene.keywords=self._bnf['keyword']+self._bnf['futureReservedWord']
            gene._max_program_length = self._max_program_length
            gene._fitness_fail = self._fitness_fail
            gene._extend_genotype = self._extend_genotype
            gene._timeouts = self._timeouts
            gene._wrap = self._wrap
            gene.nTInvlvdGenProcess=nTInvlvdGenProcess
            member_no += 1
            gene.local_bnf["program"]=self.initial_Population[gene.member_no]
            gene.execution_timeout = self.execution_timeout
            self.population.append(gene)
        return True;  
    
           

    def compute_fitness(self,gene,mutation=False):
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
                    if rc and rc not in [0,1,2,3,4] :
                        if gene._generation != 0:
                            program+="\n//"+option
                            logging.info("Crash:")
                            logging.info("mutation_rate:"+str(self._mutation_rate) +",crossover_rate:"+str(self._crossover_rate)+",multiple_rate:"+str(self._multiple_rate))
                            logging.info("++++++++++++++++++++++++++++++++++++++++")
                            logging.info(program)
                            logging.info("++++++++++++++++++++++++++++++++++++++++")
                            logging.info("error:"+err)
                            logging.info("interpreter:"+self.interpreter_Shell)
                            gene._fitness=gene._fitness_fail*-10
                            FILECOUNT = len(listdir(self.targetDirectory))+1 
                            newFile=self.targetDirectory+"/"+str(FILECOUNT)+"_.js"
                            f=open(newFile,'w')
                            f.write(program)
                            f.close
                    else:
                        if rc != 3 and rc != 1 :
                            gene._fitness = self.computeSubScore(gene,program,err)*-1
            except: 
                pass
            finally:
                try:
                    remove(f.name)
                except:
                    pass

    def run_cmd(self, fi,l,option):
        try:
            if self.interpreterInd!=3:
                exec_cmd=self.interpreter_Shell+" "+option+" shell.js "+ fi
            else:
                exec_cmd=self.interpreter_Shell+" "+ fi
            p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
            l[0]=p
            out, err = p.communicate()
            l[1]=(out,err,p.returncode)
            sys.stdout.flush()
            sys.stderr.flush()
        except:
            pass
    
    def computeSubScore (self, gene, program,err):
        incompl,dummy=self.parseCode(program)
        parser = AntlrParser()
        a,b,c,d=parser.CountNestedStructures(incompl)
        parser = None
        for temp in a:
                gene.score += temp*1.5
        for temp in b:
                gene.score += temp*1.0
        for temp in c:
                gene.score += temp*1.0
        for temp in d:
                gene.score += temp*0.5
        if "warning" in err:
            logging.info("warning found: "+err)
            gene.score+=3
        return gene.score

    def _perform_endcycle(self):
        self._pre_selected = self._evaluate_fitness(True)

        childList=[]
        for gene in self._pre_selected:
            childList.append(deepcopy(gene))


        while len(childList) + len(self._pre_selected) < self._population_size:
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
                    
                    child1ParseTree,child1._identifiers=self.parseCode(child1Prg)
                    parser = AntlrParser()
                    non_term1=parser.extractNonTerminal(child1ParseTree)
                    parser = None

                    child2ParseTree,child2._identifiers=self.parseCode(child2Prg)
                    parser = AntlrParser()
                    non_term2=parser.extractNonTerminal(child2ParseTree)
                    parser = None
                    if self.nT_Invld_Gen_Process is not None:
                        commonNonTerm=[val for val in non_term1 if (val in set(non_term2) and val in self.nT_Invld_Gen_Process)]
                    else:
                        commonNonTerm=[val for val in non_term1 if (val in set(non_term2))]

                    count=1
                    if round(random(),1) < self._multiple_rate:
                        count=int(self.crossoverCount*(round(random(),1)))+1        
                    selectedNt=[]
                    if len(commonNonTerm) > 0:
                        for i in range(count):
                            selectedNt.append(choice(commonNonTerm))
                    else:
                        return child_list
                    parser = AntlrParser()
                    subString1,s1,selected1NTList=parser.genCodeFrag(child1ParseTree,non_term1,selectedNt,None,len(selectedNt))
                    subString2,s2,selected2NTList=parser.genCodeFrag(child2ParseTree,non_term2,selectedNt,None,len(selectedNt))
                    parser = None
                    
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
                    self.compute_fitness(child1)
                    child2.local_bnf['program']=child2Prg_
                    child2.generate_decimal_gene()
                    self.compute_fitness(child2)
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

    #Author: Spandan Veggalam
    def _perform_mutations(self, mlist):
        mutatedList=[]
        
        for gene in mlist:
            pr=gene.local_bnf['program']
            if round(random(),1) < self._mutation_rate :
                logging.debug("mutation started")
                generative=False
                incompl, gene._identifiers = self.parseCode(gene.get_program())
                parser = AntlrParser()
                non_TerminalsList=parser.extractNonTerminal(incompl)
                parser = None
                if len(non_TerminalsList) >1:

                    if round(random(),1) < self._generative_mutation_rate :
                        generative=True
                        gene._max_depth=self._max_depth
                    count=1
                    if round(random(),1) < self._multiple_rate:
                        count=int(self.mutationCount*round(random(),1))+1
                    parser = AntlrParser()
                    dummy,gene.local_bnf['CodeFrag'],selectedNt=parser.genCodeFrag(incompl,non_TerminalsList,None,self.nT_Invld_Gen_Process,count)
                    parser = None
                    if len(selectedNt) <=0 :
                        continue
                    gene._map_gene(selectedNt)
                    self.compute_fitness(gene,True)
                    if gene.get_fitness() != self._fitness_fail :
                        gene.local_bnf['CodeFrag']=""
                        gene.prog_generated = 1
                        mutatedList.append(gene)
                        logging.info("Mutation-Success")
                    else:
                        logging.info("Mutation-Failed")
                        logging.debug(gene.err)
                        logging.debug(selectedNt)
                        logging.debug(dummy)
                        logging.debug(gene.local_bnf['CodeFrag'])
                        logging.debug(pr)
                        logging.debug(gene.local_bnf['program'])
                        

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
