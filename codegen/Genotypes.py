#!/usr/bin/env python

from datetime import datetime
from re import sub,split
from string import lower
from marshal import load
from os import path
from codegen.Utilities import base10tobase2, base2tobase10
from random import choice
from os.path import abspath

import logging

LOG_FILENAME = 'CodegenLog.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    )


VARIABLE_FORMAT = '(\W+)'
BNF_PROGRAM = 'program'

TIMEOUT_PROG_BUILD = 0
TIMEOUT_PROG_EXECUTE = 1

class Genotype(object):

    def __init__(self, start_gene_length,
                        max_gene_length,
                        member_no,interpreter_Shell,interpreter_options):
        self._keys = []        
        self._generation=0
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
        self.interpreter_Shell=interpreter_Shell
        self.interpreter_options=interpreter_options
        self.nTInvlvdGenProcess=[]
        self.prev_program_history={}
        self.prog_generated=0
        self.execution_timeout = 30
        self._max_depth = 0
        self.err = ""
        self.score=0
    
    def set_keys(self, keys):
        self._keys = keys
    
    def _generate_binary_gene(self, length):
        geno = []
        count = 0
        while count < length * 8:
            geno.append(str(choice([0, 1])))
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

    def resolve_variable(self, variable):
        self.score+=1
        values = self.local_bnf[variable]
        value = self._select_choice(self._get_codon(), values)
        #value = sub('[\'()]', '', value)
        return str(value)
    
    def _converge(self, item):
        fileName = abspath("database" + "/" + item)
        
        if  path.isfile(fileName) and item in self.nTInvlvdGenProcess: 
            f = open(fileName,'r')
            d = load(f)
            f.close()
            s = choice(d)
            return s
        else:
            return self.resolve_variable(item)
            
    
    def _map_variables(self, program, check_stoplist):
        try:
            depth = 0
            def on_stoplist(item):
                status = False
                for stopitem in STOPLIST:
                    if item.find(stopitem) > -1:
                        status = True

                return status

            self.errors = []
            prg_list = split(VARIABLE_FORMAT, str(program))
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
            
                    elif item in self._keys:
                        if check_stoplist and position >= 0:
                            if item in ['identifier']:
                                prg_list[position] = self._converge(item)
                            elif item in ['StringLiteral','RegularExpressionLiteral']:
                                prg_list[position] = self._converge('literal')
                            elif item in ['DecimalLiteral','HexIntegerLiteral','OctalIntegerLiteral']:
                                prg_list[position] = self._converge('numericLiteral')
                            else:
                                if depth < self._max_depth:
                                    prg_list[position] = self.resolve_variable(item)
                                else:
                                    prg_list[position] = self._converge(item)
                            continue_map = True
                    position += 1
                    
                depth += 1
                program = ''.join(prg_list)
                
                prg_list = split(VARIABLE_FORMAT, str(program))
                elapsed = datetime.now() - self.starttime

                #TIMEOUT PARAMETER
                """
                if check_stoplist:
                    if elapsed.seconds > self._timeouts[TIMEOUT_PROG_EXECUTE]:
                        msg = "elapsed time greater than program timeout"
                        self.errors.append(msg)
                        raise StandardError(msg)
                else:
                    if elapsed.seconds > self._timeouts[TIMEOUT_PROG_BUILD]:
                        msg = "elapsed time greater than preprogram timeout"
                        self.errors.append(msg)
                        raise StandardError(msg)

                if len(program) > self._max_program_length:
                    msg = "program length, %s is beyond max program length: %s" % (
                                len(program), self._max_program_length)
                    self.errors.append(msg)
                    self._fitness = self._fitness_fail
                    continue_map = False;
                """
                if continue_map is False:
                    return program

        except:
            return ""

    def _get_codon(self):
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

    
    def _map_gene(self):
        self.score=0
        self._reset_gene_position()
        if self._extend_genotype:
            self._update_genotype()
        program = self._map_variables(self.local_bnf['CodeFrag'], True)
        program = sub(r'\s+', ' ', program)
        self.local_bnf[BNF_PROGRAM] = program  
        #True-Mutation


    
    def get_binary_gene_length(self):
       return self._gene_length * 8
    
    @staticmethod
    def _select_choice(codon, selection):
        if isinstance(selection, list):
            return selection[codon % len(selection)]
        else:
            return str(selection)

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
