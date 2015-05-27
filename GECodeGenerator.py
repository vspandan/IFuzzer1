#!/usr/bin/env python

from os import listdir,remove
from os.path import isfile, join, abspath

from codegen.fitness import FitnessElites, FitnessTournament, FitnessProportionate
from codegen.fitness import ReplacementTournament, MAX, MIN, CENTER
from codegen.GrammaticalEvolution import GrammaticalEvolution

from random import choice
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
LOG_LEVEL= config.get('Mappings', 'loglevel');
import logging

logging.basicConfig(filename=LOG_FILENAME,
                    level=LOG_LEVEL,
                    )

FILECOUNT = 0

Population_size=300
Timeout = 10
Generations=1000


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
                    FitnessElites(ges.fitness_list, 0.5))

                # ges.set_fitness_selections(
                #     FitnessProportionate(ges.fitness_list, 'linear'))
                
                ges.set_crossover_rate(float(0.95))
                ges.set_mutation_rate(float(0.2))

                ges.set_max_depth(2)
                ges.set_generative_mutation_rate(0.3)

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

                ges.set_crossover_bias_rate(115)
                
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

        threadList=[]
        totalTempList=[]
        while True:
            tempList=[]    
            while len(tempList)<Population_size:
                t=choice(TestCases)
                tempList.append(t)
                TestCases.remove(t)
            logging.debug(tempList)
            process(tempList)
            return False
            
    return initialize()
