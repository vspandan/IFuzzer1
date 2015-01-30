#!/usr/bin/env python

from datetime import datetime
import logging
import random
from re import sub
import re
from string import lower
import subprocess
import traceback
from pickle import load
from os import path

from codegen.Utilities import base10tobase2, base2tobase10
import collections
from random import randint
from os.path import abspath


VARIABLE_FORMAT = '(\W+)'
MUT_TYPE_M = 'm'
MUT_TYPE_S = 's'
BNF_PROGRAM = 'program'

#   Positions in _timeouts
TIMEOUT_PROG_BUILD = 0
TIMEOUT_PROG_EXECUTE = 1

DEFAULT_LOG_FILE = 'GECodeGen.log'
DEFAULT_LOG_LEVEL = logging.INFO

DEFAULT_DATABASE_PATH = "../database"
APPEND = "a+"
READ = "r"

logging.basicConfig(format='%(asctime)s %(message)s',
                    filename=DEFAULT_LOG_FILE,
                    level=DEFAULT_LOG_LEVEL)


class Genotype(object):

    # Modified Author : Spandan Veggalam 
    def __init__(self, start_gene_length,
                        max_gene_length,
                        member_no):
        self._keys = []        
        self.member_no = member_no
        self.local_bnf = {}
        self._max_program_length = None
        self._fitness = None
        self._fitness_fail = None
        self._wrap = True
        self._extend_genotype = True
        self.starttime = None
        self._timeouts = (0, 0)
        self._gene_length = start_gene_length
        self._max_gene_length = max_gene_length

        self.binary_gene = None
        self.decimal_gene = None
        self._generate_binary_gene(self._gene_length)
        self.generate_decimal_gene()

        self._position = (0, 0)
        self.keywords = None
        self._identifiers=[]
        self.errors = []
    
    # Author : Spandan Veggalam    
    def set_keys(self, keys):
        self._keys = keys
    
    def _generate_binary_gene(self, length):
        geno = []
        count = 0
        while count < length * 8:
            geno.append(str(random.randint(0, 1)))
            count += 1
        self.binary_gene = ''.join(geno)

    
    def set_binary_gene(self, binary_gene):
        length = len(binary_gene)
        trunc_binary_gene = binary_gene[:length - (length % 8)]
        self.binary_gene = trunc_binary_gene
        self._gene_length = len(self.binary_gene) / 8

    def generate_decimal_gene(self):
    
        if self._gene_length == 0:
            raise ValueError("Invalid gene length")
        dec_geno = []

        for i in range(0, self._gene_length * 8, 8):
            item = self.binary_gene[i:i + 8]
            str_trans = base2tobase10(item)
            dec_geno.append(int(str_trans))

        self.decimal_gene = dec_geno
        self._position = (0, 0)

    @staticmethod
    def _dec2bin_gene(dec_gene):
       
        bin_gene = []
        for item in dec_gene:
            bin_gene.append(base10tobase2(item, zfill=8))
        return ''.join(bin_gene)

    def set_bnf_variable(self, variable_name, value):
        if isinstance(value, list):
            self.local_bnf[variable_name] = value
        else:
            self.local_bnf[variable_name] = [str(value)]

    # Modified Author : Spandan Veggalam 
    def resolve_variable(self, variable):
        values = self.local_bnf[variable]
        value = self._select_choice(self._get_codon(), values)
        value = re.sub('[\'()]', '', value)
        return str(value)
    
    
    # Author : Spandan Veggalam 
    def _converge(self, item):
        
        fileName = abspath(DEFAULT_DATABASE_PATH + "/" + item)
        if  path.isfile(fileName): 
            f = open(fileName, READ)
            # TODO apply strategy to select based on its score values
            d = load(f)
            f.close()
            #keys = d.keys()
            return d[random.randint(0, len(d) - 1)]
        else:
            print "No related mapping found for "+item
            return self.resolve_variable(item)
            
    
    # Modified Author : Spandan Veggalam 
    def _map_variables(self, program, check_stoplist):
        #print program
        initialMapping = 0
        def on_stoplist(item):
            status = False
            for stopitem in STOPLIST:
                if item.find(stopitem) > -1:
                    status = True

            return status

        self.errors = []
        prg_list = re.split(VARIABLE_FORMAT, str(program))
        while True:

            position = 0
            continue_map = False
            while position < len(prg_list):
                #TODO check this process
                item = prg_list[position]
                if item in self.keywords:
                    prg_list[position]=lower(item)
                    position += 1
                    continue
        
                if item == "identifier" or "__id__" in item:
                    l=len(self._identifiers)
                    if l>0:
                        ident=str(self._identifiers[randint(0,l-1)])
                        prg_list[position]= ident.replace("__id__","")
                    else:
                        prg_list[position]="id"
                    position += 1
                    continue

                if item in ['StringLiteral','RegularExpressionLiteral']:
                    prg_list[position] = self._converge('literal')
                    position += 1
                    continue
                
                if item in ['HexIntegerLiteral' , 'DecimalLiteral' , 'OctalIntegerLiteral']:
                    prg_list[position] = self._converge('numericLiteral')
                    position += 1
                    continue
        
                if item in self._keys:
                    if check_stoplist and position >= 0:
                        #print item
                        if initialMapping == 0:
                            prg_list[position] = self.resolve_variable(item)
                        else:
                            prg_list[position] = self._converge(item)
                        continue_map = True
                        #print prg_list[position]
                position += 1
                
            initialMapping = 1
            program = ''.join(prg_list)
            prg_list = re.split(VARIABLE_FORMAT, str(program))
            elapsed = datetime.now() - self.starttime

            #   Reasons to fail the process
            if check_stoplist:
                #   Program already running
                if elapsed.seconds > self._timeouts[TIMEOUT_PROG_EXECUTE]:
                    msg = "elapsed time greater than program timeout"
                    logging.debug(msg)
                    self.errors.append(msg)
                    raise StandardError(msg)
                    # continue_map = False
            else:
                #   Preprogram
                if elapsed.seconds > self._timeouts[TIMEOUT_PROG_BUILD]:
                    msg = "elapsed time greater than preprogram timeout"
                    logging.debug(msg)
                    self.errors.append(msg)
                    raise StandardError(msg)
                    # continue_map = False

            """if len(program) > self._max_program_length:
                #   Runaway process
                msg = "program length, %s is beyond max program length: %s" % (
                            len(program), self._max_program_length)
                logging.debug(msg)
                logging.debug("program follows:")
                # logging.debug(program)
                self.errors.append(msg)
                self._fitness = self._fitness_fail
                continue_map = False;
                # continue_map = False
            """
            if continue_map is False:
                return program

    def _get_codon(self):
        #   position is the location on the gene, sequence_no is the number of
        #   codons used since the start
        position, sequence_no = self._position
        length = len(self.decimal_gene)
        wrap = self._wrap

        status = True
        while status:
            if not wrap:
                if sequence_no == self._max_gene_length:
                    raise ValueError("Max length of genotype reached.")
            codon = self.decimal_gene[position]
            if self._extend_genotype:
                if sequence_no == length:
                    #   modify var directly
                    self.decimal_gene.append(codon)
                    self._gene_length = len(self.decimal_gene)

            position += 1
            sequence_no += 1
            if position == length:
                if wrap:
                    position = 0

            self._position = (position, sequence_no)
            return codon

    def _reset_gene_position(self):
        self._position = (0, 0)

    def _update_genotype(self):
        self.set_binary_gene(self._dec2bin_gene(self.decimal_gene))

    def compute_fitness(self):
        self._reset_gene_position()
        self._map_gene()
        if self._extend_genotype:
            logging.debug("updating genotype...")
            self._update_genotype()
            logging.debug("Finished updating genotype...")

        return self._fitness

    # Modified Author : Spandan Veggalam 
    def _map_gene(self):
        self.local_bnf['<fitness>'] = [str(self._fitness_fail)]
        logging.debug("==================================================")
        logging.debug("mapping variables to program...")
        program = self._map_variables(self.local_bnf['CodeFrag'], True)
        logging.debug("finished mapping variables to program...")
        self.local_bnf[BNF_PROGRAM] = program
        logging.debug(program)
        status = self._execute_code(program)
        logging.debug("==================================================")
        if status == 1:
            elapsedTime = datetime.now() - self.starttime
            elapsed = elapsedTime.total_seconds()
        if status == 0:
            logging.debug("program failed")
            program = self.local_bnf[BNF_PROGRAM]
            logging.debug("errors: %s", (self.errors))
            logging.debug(program)
            logging.debug("end of failure report")
            elapsed = self._fitness_fail

        self._fitness = elapsed
		
    # Modified Author : Spandan Veggalam 
    def _execute_code(self, program):

        program = sub(r'\s+', ' ', program)
        self.local_bnf[BNF_PROGRAM] = program    
        
        if len(program) == 0:
            return 0
        else:                
            print "executing \t" + program
            p = subprocess.Popen(["js24 -e \'" + program + "\'"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = p.communicate()
            
            if 'SyntaxError' in err or 'Syntax error' in err:
                print "err:"+err
                return 0    
            return 1    

    def get_binary_gene_length(self):
       return self._gene_length * 8
    
    # Author: Spandan Veggalam
    def _single_mutate(self, position1=None, position2=None):
        if position1 is None or position2 is None:
            position = random.randint(0, self._gene_length * 8 - 1)
            gene = self.binary_gene
            self.binary_gene = self._mutate(gene, position1)
        
        else:
            program1 = self.local_bnf[BNF_PROGRAM]
            self.local_bnf[BNF_PROGRAM] = sub(r'\s+', ' ', self._map_variables(self.local_bnf['CodeFrag'], True))
            subCode = self.local_bnf['CodeFrag'][position2:]
            position2 = self.local_bnf[BNF_PROGRAM].find(subCode)
            gene = self.binary_gene
            self.binary_gene = self._mutate(gene, position1, position2)
            
        self.generate_decimal_gene()

    # Author: Spandan Veggalam
    @staticmethod
    def _mutate(gene, position1, position2=None):
        newRandBGene = ""
        
        count = 0
        if position2 is not None:
            length = position2 - position1
        else:
            length = 1
        if length > 0:
            while count < length * 8 :
                newRandBGene = newRandBGene + str(random.randint(0, 1))
                count += 1        
            gene = ''.join([gene[:position1 * 8], newRandBGene , gene[(position1 + length) * 8:]])
        
        return gene

    @staticmethod
    def _select_choice(codon, selection):
        if isinstance(selection, list):
            return selection[codon % len(selection)]
        else:
            msg = "selection. %s, must be a list" % (selection)
            raise ValueError(msg)

    def get_program(self):
        return self.local_bnf[BNF_PROGRAM]

    def get_fitness(self):
        return self._fitness

    def get_fitness_fail(self):
        return self._fitness_fail

    def set_identifiers(self,idenfifiers):
        self._identifiers=idenfifiers
    
    def get_identifiers(self):
        return self._identifiers