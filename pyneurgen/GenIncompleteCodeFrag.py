from random import randint

#Author: Spandan Veggalam
class GenIncompleteCodeFrag(object):
    
    #Author: Spandan Veggalam
    def genCodeFrag(self, parsetree, population_size):
        population = []
        
        for pop_count in range(0, population_size):
            inc =0
            code=""
            val=parsetree.split()
            nT=self._extractNonTerminal(val)
            selected=randint(0,len(nT)-1)
            start=False
            once=False
            for v in val:
                if "<<<" in v:
                    inc=inc+1
                    v=" "
                if selected == inc and not start and not once:
                    #code=code+" <"+nT[selected-1]+"> "
                    code=code+" "+nT[selected-1]+" "
                    start=True
                    once =True
                if start:
                    if ">>>" in v :
                        inc=inc-1   
                    if inc==selected-1:
                            start=False
                if not start:   
                    if ">>>" in v :
                        inc=inc-1                        
                    else:
                        v=v.strip()
                        if len(v) >0:
                            code =code+" "+v
            population.append(code.strip())
            
        return population
    
    #Author: Spandan Veggalam
    def _extractNonTerminal(self,val):
        nT=[]
        for v in val:
                if "<<<" in v:
                    nT.append(v.replace("<<<","").replace(":","").strip())
        return nT
    