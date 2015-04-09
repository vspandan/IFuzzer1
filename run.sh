if [ "$1" == "-c" ]; then
	cd langparser
	java -jar antlr-4.5-rc-2-complete.jar -package langparser ECMAScript.g4
	javac -cp "../lib/*" *.java
	cd ..
	jar cvfm ECMAScript.jar langparser/Manifest.txt langparser/*.class langparser/antlr-4.5-rc-2-complete.jar
	mv ECMAScript.jar langparser/
	rm -rf langparser/*.class
else
	jython GEInterpreterFuzzer.py
fi;