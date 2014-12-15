from random import randint, choice


#Author: Spandan Veggalam
class GenIncompleteCodeFrag(object):
    
    #Author: Spandan Veggalam
    def genCodeFrag(self, parsetree, population_size,nT,subTree = None,nonTerminal=None):
        population = []
        
        for pop_count in range(0, population_size):            
            
            val=parsetree.split()
            if len(nT) != 0: 
                
                if nonTerminal is None:
                    self.selected=randint(0,len(nT)-1)
                    selectedNt=nT[self.selected-1]
                else:
                    selectedNt=nonTerminal
                    indices = [i for i, x in enumerate(nT) if x == nonTerminal]
                    self.selected=choice(indices)+1
                    
                nTposition=0;
                indicator = False
                temp=0
                code=""
                subcode=""
                
                for v in val:
                    
                    if '<<<' in v:
                        nTposition=nTposition+1
                        if indicator:
                            temp=temp+1
                        
                    if nTposition == self.selected and not indicator:
                        nTposition =-10000
                        code=code+" "+selectedNt
                        indicator=True                    
                        temp=temp+1
                        
                    if '>>>' in v:
                        if indicator:
                            temp=temp-1
                            
                    if indicator:
                        #for complete parse representation that is being replaced use below code statement.
                        #subcode=subcode + " " +v
                        if "<<<" not in v :
                            if ">>>" not in v:
                                subcode=subcode+" "+v
                    if not indicator:
                        if "<<<" not in v :
                            if ">>>" not in v:
                                code=code+" "+v
                    
                    if temp==0 and indicator:
                        indicator=False
                    
            if population_size == 1: 
                if subTree is None:
                    return code.strip(),selectedNt
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
if __name__=='__main__':
    g=GenIncompleteCodeFrag()
    str=raw_input()
    print g.genCodeFrag(str, 1, g.extractNonTerminal(str.split()), None, None)