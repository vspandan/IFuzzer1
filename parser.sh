cd langparser
#javac -cp "../lib/antlr-4.5-rc-2-complete.jar" *.java
java -cp ".:../lib/antlr-4.5-rc-2-complete.jar" AntlrParser $1 $2
cd ..
