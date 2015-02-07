cd langparser
javac -cp "../lib/*" *.java
java -cp ".:../lib/*" AntlrParser&
cd ..
python GEInterpreterFuzzer1.py