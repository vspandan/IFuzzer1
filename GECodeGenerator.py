#!/usr/bin/env python

from os import listdir,remove
from os.path import isfile, join, abspath

from shutil import rmtree

from codegen.fitness import FitnessElites, FitnessTournament, FitnessProportionate
from codegen.fitness import ReplacementTournament, MAX, MIN, CENTER
from codegen.GrammaticalEvolution import GrammaticalEvolution

from random import choice
import ConfigParser
import logging

config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
LOG_LEVEL= config.get('Mappings', 'loglevel');

logging.basicConfig(filename=LOG_FILENAME,
                    level=LOG_LEVEL,
                    )

Population_size=int(config.get('Mappings', 'populationsize'));
Timeout = int(config.get('Mappings', 'interpretertimeout'));
Generations=int(config.get('Mappings', 'generations'));
FileListDir=config.get('TargetDir', 'TEMP')

#Author: Spandan Veggalam
def runFuzzer(targetDirectory,interpreter,options,excludeFiles,nTInvlvdGenProcess,shellFiles):

    TestCases=[]
    tempList=[]    

    for f in listdir(FileListDir):
        fi=join(FileListDir,f)
        TestCases.append(abspath(fi))
    try:
        while len(tempList)<Population_size:
            if len(TestCases)>0:
                t=choice(TestCases)
                tempList.append(t)
                TestCases.remove(t)
            else:
                break
        if len(tempList) >= Population_size:
            logging.debug(tempList)
            bnf=""
            ges = GrammaticalEvolution()
            ges.setGrammarFile(abspath(config.get('Mappings', 'grammarFile')))
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
            
            ges.set_crossover_rate(float(0.4))
            ges.set_mutation_rate(float(0.8))

            ges.set_max_depth(2)
            ges.set_generative_mutation_rate(0.3)

            ges.set_children_per_crossover(2)
            
            ges.set_mutation_type('s')

            ges.set_mutation_count(3);
            ges.set_crossover_count(3);
            ges._multiple_rate=(0.5)

            ges.set_max_fitness_rate(float(0.04))
            
            ges.set_replacement_selections(
                    ReplacementTournament(ges.fitness_list, tournament_size=3))
            
            ges.set_maintain_history(False)
            ges.set_extend_genotype(True)
            
            ges.dynamic_mutation_rate(1)
            ges.dynamic_crossover_rate(1)
            ges.targetDirectory=targetDirectory

            ges.set_crossover_bias_rate(115)
            
            if ges.create_genotypes(tempList,interpreter,options,nTInvlvdGenProcess,shellFiles):
                ges.run()
                for gene in ges.population:
                    if gene.get_fitness() != ges._fitness_fail :
                        generatedPrg= gene.get_program()
                        newFile=targetDirectory+"/"+str(len(listdir(targetDirectory))+1)+".js"
                        f=open(newFile,'w')
                        f.write(generatedPrg)
                        f.close
            ges=None
            for f in tempList:
                try:
                    remove(f);                
                except:
                    pass
        else:
            raw_input("deleting")                    
            rmtree(FileListDir)
            raw_input("deleted")
    except:
        pass
        