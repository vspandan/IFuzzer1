#!/usr/bin/env python

from pyneurgen.grammatical_evolution import GrammaticalEvolution
from pyneurgen.fitness import FitnessElites, FitnessTournament
from pyneurgen.fitness import ReplacementTournament, MAX, MIN, CENTER


f = open('JavaScript.g', 'r');

bnf=""

for line in f:
    bnf+=line;
f.close()

#Build UI to take input folder
#ability to handle multiple programs
f1=open('IncompleteCodeFrag','r')

bnf+="""<S>:"""
for line in f1:
    bnf+=line;



ges = GrammaticalEvolution()

ges.set_bnf(bnf)
ges.set_genotype_length(start_gene_length=20,
                        max_gene_length=50)
ges.set_population_size(50)
ges.set_wrap(True)

ges.set_max_generations(1000)
ges.set_fitness_type(MIN, .01)

ges.set_max_program_length(500)
ges.set_timeouts(10, 120)
ges.set_fitness_fail(100.0)

ges.set_mutation_rate(.025)
ges.set_fitness_selections(
    FitnessElites(ges.fitness_list, .05),
    FitnessTournament(ges.fitness_list, tournament_size=2))
ges.set_max_fitness_rate(.5)

ges.set_crossover_rate(.2)
ges.set_children_per_crossover(2)
ges.set_mutation_type('m')
ges.set_max_fitness_rate(.25)

ges.set_replacement_selections(
        ReplacementTournament(ges.fitness_list, tournament_size=3))

ges.set_maintain_history(True)
ges.create_genotypes()
print ges.run()
print ges.fitness_list.sorted()
print
print
gene = ges.population[ges.fitness_list.best_member()]
print gene.get_program()
