#!/usr/bin/env python

from os import listdir,remove
from os.path import isfile, join, abspath

from codegen.fitness import FitnessElites, FitnessTournament
from codegen.fitness import ReplacementTournament, MAX, MIN, CENTER
from codegen.GrammaticalEvolution import GrammaticalEvolution

from random import choice
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
import logging
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    )


FILECOUNT = 0

Population_size=100
Timeout = 15
Generations=100


#Author: Spandan Veggalam
def runFuzzer(TestCases,targetDirectory,interpreter,options,excludeFiles,nTInvlvdGenProcess, interpreterInd):
    def selectGrammarFIle():
        Tk().withdraw()        
        e.set(askopenfilename())   
    
    #Author: Spandan Veggalam
    def initialize():
        FileList=[]
        def process(fil):
                bnf=""
                ges = GrammaticalEvolution()
                ges.setGrammarFile(abspath("grammarFiles/JavaScript.g4"))
                ges.set_bnf(bnf)
                ges.set_genotype_length(20, 5000)
                ges.set_population_size(Population_size)
                ges.set_wrap(True)
                ges.set_max_generations(Generations)
                ges.set_fitness_type('max', float(10000))
                
                ges.set_max_program_length(500)
                ges.set_fitness_fail(float(-1000))
                
                ges.set_execution_timeout(Timeout)
                
                ges.set_fitness_selections(
                    FitnessElites(ges.fitness_list, 0.1))
                
                ges.set_crossover_rate(float(0.2))
                ges.set_mutation_rate(float(0.8))

                ges.set_max_depth(2)
                ges.set_generative_mutation_rate(0.0)

                ges.set_children_per_crossover(2)
                
                ges.set_mutation_type('s')

                ges.set_mutation_count(1);
                ges.set_crossover_count(1);
                ges._multiple_rate=(0.2)

                ges.set_max_fitness_rate(float(0.1))
                
                ges.set_replacement_selections(
                        ReplacementTournament(ges.fitness_list, tournament_size=3))
                
                ges.set_maintain_history(False)
                ges.set_extend_genotype(True)
                
                ges.dynamic_mutation_rate(1)
                ges.dynamic_crossover_rate(1)
                ges.targetDirectory=targetDirectory
                
                # print fil
                

                if ges.create_genotypes(fil,interpreter,options,nTInvlvdGenProcess,interpreterInd):
                    ges.run()
                    for gene in ges.population:
                        if gene.get_fitness() != ges._fitness_fail :
                            generatedPrg= gene.get_program()
                            # print generatedPrg
                            FILECOUNT = len(listdir(targetDirectory))+1 
                            newFile=targetDirectory+"/"+str(FILECOUNT)+".js"
                            
                            FileList.append(newFile)
                            f=open(newFile,'w')
                            f.write(generatedPrg)
                            f.close
                ges=None
                for fl in fil:
                    try:
                        remove(fl)
                    except:
                        print "Error deleting file"
                return False
            
        threadList=[]
        totalTempList=[]
        while True:
            if len(TestCases) < Population_size:
                for f in TestCases:
                    try:
                        remove(f)
                    except:
                        print "Error deleting file"
                print "breaking"
                return True
            tempList=[]    
            while len(tempList)<Population_size:
                t=choice(TestCases)
                # if t in totalTempList:
                #     continue
                tempList.append(t)
                TestCases.remove(t)
            logging.debug(tempList)
            process(tempList)
            return False
            import threading
            th=threading.Thread(target=process,kwargs={'fil':tempList})
            threadList.append(th)
            totalTempList += tempList
            if len(threadList)==2:
                for thrd in threadList:
                    thrd.start()
                for thrd in threadList:
                    thrd.join()
                return False
    return initialize()
