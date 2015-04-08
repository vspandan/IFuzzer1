cd langparser
javac -cp "../lib/*" *.java
cd ..
jar cvfm ECMAScript.jar langparser/Manifest.txt langparser/*.class
mv ECMAScript.jar langparser/
rm -rf langparser/*.class
jython GEInterpreterFuzzer.py