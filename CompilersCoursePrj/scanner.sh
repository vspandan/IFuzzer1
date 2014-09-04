flex $1.l
bison -d -v $1.y
cc -o $1 $1.tab.c lex.yy.c -ly -ll

./$1
