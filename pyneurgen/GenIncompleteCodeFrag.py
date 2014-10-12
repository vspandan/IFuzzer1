from random import randint

class GenIncompleteCodeFrag(object):

    

    def genCodeFrag(self, parsetree, population_size):
        population = []
        
        for pop_count in range(0, population_size):
            inc =0
            code=""
            nT=[]
            val=parsetree.split()
            for v in val:
                if "<<<" in v:
                    nT.append(v.replace("<<<","").replace(":","").strip())
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
                        code=code+" "
                    else:
                        code =code+" "+v
                
            population.append(code)
            
        return population
