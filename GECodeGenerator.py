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

Population_size=int(config.get('Options', 'POPULATION_SIZE'));
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
            ges.setGrammarFile(abspath(config.get('Options', 'GRAMMAR_FILE')))
            ges.set_bnf(bnf)
            ges.set_genotype_length(int(config.get('Options', 'MIN_GENE_LENGTH')), int(config.get('Options', 'MAX_GENE_LENGTH')))
            ges.set_population_size(Population_size)
            ges.set_wrap(bool(config.get('Options', 'WRAP')))
            ges.set_max_generations(int(config.get('Options', 'MAX_GENERATIONS')))
            ges.set_fitness_type(config.get('Options', 'FITNESS_TYPE'), float(config.get('Options', 'MAX_FITNESS_VALUE')))
            
            ges.set_max_program_length(int(config.get('Options', 'MAX_PROGRAM_LENGTH')))
            ges.set_fitness_fail(float(config.get('Options', 'FITNESS_FAIL')))
            
            ges.set_execution_timeout(int(config.get('Options', 'INTERPRETER_TIMEOUT')))
            
            ges.set_fitness_selections(
                FitnessElites(ges.fitness_list, 0.5))

            # ges.set_fitness_selections(
            #     FitnessProportionate(ges.fitness_list, 'linear'))
            
            ges.set_crossover_rate(float(config.get('Options', 'CROSSOVER_RATE')))
            ges.set_mutation_rate(float(config.get('Options', 'MUTATION_RATE')))

            ges.set_max_depth(int(config.get('Options', 'MAX_DEPTH_EXPANSION')))
            ges.set_generative_mutation_rate(float(config.get('Options', 'GENERATIVE_PROBABILITY')))

            ges.set_children_per_crossover(int(config.get('Options', 'CHILDREN_PER_CROSSOVER')))
            
            ges.set_mutation_type(config.get('Options', 'MUTATION_TYPE'))

            ges.set_mutation_count(int(config.get('Options', 'MULTIPLE_MUTATION_COUNT')));
            ges.set_crossover_count(int(config.get('Options', 'MULTIPLE_CROSSOVER_COUNT')));
            ges._multiple_rate=(float(config.get('Options', 'MULTIPLE_RATE')))

            ges.set_max_fitness_rate(float(config.get('Options', 'MAX_FITNESS_INDV_RATE')))
            
            ges.set_replacement_selections(
                    ReplacementTournament(ges.fitness_list, tournament_size=int(config.get('Options', 'REPLACEMENT_TOURNAMENT_SIZE'))))
            
            ges.set_maintain_history(bool(config.get('Options', 'MAINTAIN_HISTORY')))
            ges.set_extend_genotype(bool(config.get('Options', 'EXTEND_GENOTYPE')))
            
            ges.dynamic_mutation_rate(int(config.get('Options', 'DYNAMIC_MUTATION_RATE')))
            ges.dynamic_crossover_rate(int(config.get('Options', 'DYNAMIC_CROSSOVER_RATE')))
            ges.targetDirectory=targetDirectory

            ges.set_crossover_bias_rate(int(config.get('Options', 'CROSSOVER_BIAS_RATE')))
            
            if ges.create_genotypes(tempList,interpreter,options,nTInvlvdGenProcess,shellFiles):
                ges.run()
                for gene in ges.population:
                    if gene.get_fitness() != ges._fitness_fail :
                        generatedPrg= gene.get_program()
                        newFile=targetDirectory+"/"+str(len(listdir(targetDirectory))+1)+config.get('Interpreter', 'FILE_TYPE')
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
            rmtree(FileListDir)
    except:
        pass