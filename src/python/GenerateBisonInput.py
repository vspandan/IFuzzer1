from Property import *
from os import listdir
from os.path import isfile, join
from os import system
from os import remove


class GenerateBisonInput(object):
    
    
        

    def createBisonInput(self,grammar_file):
        with open (BISON_FILE,WRITE) as f:
            temp = open(TEMP_FILE,READ);
            for line in temp:
                f.write("%token ")
                f.write(line)
                f.write(NEW_LINE)
            temp.close()
            f.write("%error-verbose")
            f.write(NEW_LINE)
            f.write("%union {"+NEW_LINE+" int a;"+NEW_LINE+"float b;"+NEW_LINE+"char *c;"+NEW_LINE+"}")
            f.write(NEW_LINE +"%{" + NEW_LINE + "#include <stdlib.h>"  + NEW_LINE + "%}")
            f.write(NEW_LINE +"%{" + NEW_LINE + "#include <stdio.h>"  + NEW_LINE + "%}")
            f.write(NEW_LINE +"%{" + NEW_LINE + "#include <string.h>"  + NEW_LINE + "%}")
            f.write(NEW_LINE+"%%"+NEW_LINE)
            #remove(TEMP_FILE)
            temp = open (grammar_file, READ)
            start=True
            for line in temp:
                
                if line.find(RULE_DELIM) >= 0 :
                    key, values = line.split(RULE_DELIM,1)
                    key = key.strip()
                    
                    f.write(key +"\t"+ RULE_DELIM +NEW_LINE)
                                       
                    productions=values.split(PROD_DELIMITER)
                    i=0
                    for prod in productions:
                        f.write("\t\t\t\t")
                        if i != 0 :
                            f.write(PROD_DELIMITER)
                        f.write(prod)
                        j = len(prod.split())
                        ############
                        if j>0 and start:
                        #if j>0 :
                            f.write("\t");
                            f.write("{")
                            for k in range (j):
                                f.write("if ($<c>"+str(k+1)+"== \'\\0\')\t")
                                f.write("$<c>"+str(k+1)+"= \"@\";\t") 
                            if start:
                                f.write("printf(\"<<<"+key)
                                start=False
                            else :
                                f.write("sprintf($<c>$,\" <<<"+key)
                            for k in range (j):
                                f.write(" %s")
                            f.write(" >>>\"")
                            for k in range (j):
                                
                                f.write(",$<c>"+str(k+1))
                            f.write(");}")
                        f.write(NEW_LINE)
                        i = i+1
                    f.write("\t\t\t\t");
                    f.write(RULE_END_DELIM);
                    f.write(NEW_LINE)
                    
            f.write(NEW_LINE+"%%"+NEW_LINE)  
            f.write("int main()" + NEW_LINE + "{"  + NEW_LINE + "yyparse();"  + NEW_LINE + "}")  
    
                
                
    
                