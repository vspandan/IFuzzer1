python GeParser.py
curr_dir=`pwd`
cd ~/Documents/GePyNeurgen
flex -w lexfile.l
bison -d -v bison.y
cc -w -o parser lex.yy.c bison.tab.c -ll -ly

echo "var s=10+10; var p=10;"| ./parser >IncompleteCodeFrag

#mv IncompleteCodeFrag $curr_dir

cd $curr_dir


python GECodeGen.py
