from Property import *
from os import listdir
from os.path import isfile, join
from os import system
from os import remove
from os import path
from os import stat
from os import mkdir


class GenerateBisonInput(object):
    
    
    def __init__(self):
        
        self.HOME_DIR=path.expanduser(DIR)
        try:
            stat(self.HOME_DIR)
        except:
            mkdir(self.HOME_DIR)  



    def createBisonInput(self,grammar_file):
        with open (self.HOME_DIR+BISON_FILE,WRITE) as f:
            temp = open(self.HOME_DIR+TEMP_FILE1,READ);
            for line in temp:
                f.write("%token ")
                f.write(line)
                f.write(NEW_LINE)
            temp.close()
            temp = open(self.HOME_DIR+TEMP_FILE2,READ);
            strs = []
            for line in temp:
                strs=line.split()                
            temp.close()
            
            f.write(NEW_LINE)
            f.write("%left '(' '[' '*' '/' '%' '+' '-' \"<<\" \">>\" \">>>\" '<' '>' \"<=\" \">=\" \"==\" \"!=\" '&' '^' '#' \"&&\" \"##\" '?' ':' '=' ")
            f.write(NEW_LINE)
            f.write("%error-verbose")
            f.write(NEW_LINE)
            f.write("%union {"+NEW_LINE+" int a;"+NEW_LINE+"float b;"+NEW_LINE+"char *c;"+NEW_LINE+"}")
            f.write(NEW_LINE +"%{" + NEW_LINE + "#include <stdlib.h>"  + NEW_LINE + "#include <stdio.h>"  + NEW_LINE + "#include <string.h>"  + NEW_LINE + "%}")
            f.write(NEW_LINE+"%{"+NEW_LINE+"char *s;"+NEW_LINE+"%}")
            f.write(NEW_LINE+"%%"+NEW_LINE)
            remove(self.HOME_DIR+TEMP_FILE1)
            remove(self.HOME_DIR+TEMP_FILE2)
            temp = open (grammar_file, READ)            
            start=True
            prodnum=0
            for line in temp:
                if line.find(RULE_DELIM) >= 0 :
                    key, values = line.split(RULE_DELIM,1)
                    key = key.strip()
                    f.write(key +"\t"+ RULE_DELIM +NEW_LINE)
                    productions=values.split(PROD_DELIMITER1)
                    i=0
                    for prod in productions:
                        prodnum=prodnum+1
                        f.write("\t\t\t\t")
                        if i != 0 :
                            f.write(PROD_DELIMITER1)
                        if len(strs)>0 :
                            for s in strs :
                                if prod.find(s) >= 0:
                                    st= s.replace("\'","\"")
                                    prod=prod.replace(s,st)
                        f.write(prod)
                        
                        j = len(prod.split())
                        print prod
                        print prod.split()
                        print j
                        f.write("\t");
                        f.write("{")
                        if j==0:                                
                                f.write("$<c>$=\"EMPTY\";");
                        elif j==1:
                            if not start:                         
                                f.write("$<c>$=$<c>1;");
                            if start:
                                f.write("printf(\"<<<"+key+": %s >>>\",$<c>$);")
                                start=False
                        elif j>1 :
                            if start:
                                f.write("printf(\"<<<"+key+":")
                            else :
                                f.write("int len=");
                                for k in range (j):
                                    f.write("strlen($<c>"+str(k+1)+")")
                                    f.write("+")
                                f.write("7+"+str(len(key)+j)+" ;");
                                f.write("char *s"+str(prodnum)+"=malloc(sizeof(char)*len);")
                                f.write("sprintf(s"+str(prodnum)+",\" <<<"+key+":")
                            
                            for k in range (j):
                                f.write(" %s")
                            f.write(" >>>\"")
                            for k in range (j):
                                f.write(",$<c>"+str(k+1))
                            f.write(");")
                            if not start:
                                f.write("$<c>$=s"+str(prodnum)+";");
                            start=False
                            

                            
                        ############
                        f.write("}")
                        f.write(NEW_LINE)
                        i = i+1
                    f.write("\t\t\t\t");
                    f.write(RULE_END_DELIM);
                    f.write(NEW_LINE)
                    
            f.write(NEW_LINE+"%%"+NEW_LINE)  
            f.write("int main()" + NEW_LINE + "{"  + NEW_LINE + "yyparse();"  + NEW_LINE + "}")  
    
                
                
    
                