from random import randint, choice

#Author: Spandan Veggalam
class GenIncompleteCodeFrag(object):
    
    #Author: Spandan Veggalam
    def genCodeFrag(self, parsetree, population_size,nT,subTree = None,nonTerminal=None):
        population = []
        
        for pop_count in range(0, population_size):
            inc =0
            code=""
            val=parsetree.split()
            
            if nonTerminal is None:
                self.selected=randint(0,len(nT)-1)
                selectedNt=nT[self.selected-1]
            else:
                selectedNt=nonTerminal
                indices = [i for i, x in enumerate(nT) if x == nonTerminal]
                self.selected=choice(indices)
                
            start=False
            once=False
            subcode=""
            for v in val:
                v=v.strip()
                if len(v) >= 1:
                    if "<<<" in v:
                        inc=inc+1
                        v=" "
                    if self.selected == inc and not start and not once:
                        #code=code+" <"+nT[self.selected-1]+"> "
                        code=code+" "+selectedNt+" "
                        start=True
                        once =True
                    if start:
                        
                        if ">>>" in v :
                            inc=inc-1
                        else:                        
                            subcode=subcode+" "+v    
                        if inc==self.selected-1:
                                start=False
                    if not start:
                        if ">>>" in v :
                            inc=inc-1                        
                        else:
                            if len(v) >0:
                                code =code+" "+v                
            if population_size == 1: 
                if subTree is None:                    
                    return code.strip()
                if subTree is not None:                    
                    return subcode.strip()
            population.append(code.strip())
            
        return population
        
            
    
    #Author: Spandan Veggalam
    def extractNonTerminal(self,val):        
        nT=[]
        for v in val:
                if "<<<" in v:
                    nT.append(v.replace("<<<","").replace(":","").strip())
        return nT
    