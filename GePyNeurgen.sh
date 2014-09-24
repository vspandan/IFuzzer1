python GeParser.py
curr_dir=`pwd`
cd ~/Documents/GePyNeurgen
flex -w lexfile.l
bison -d -v bison.y
cc -o parser lex.yy.c bison.tab.c -ll -ly
cd $curr_dir
python GECodeGen.py
