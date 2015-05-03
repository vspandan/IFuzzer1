if [ "$1" == "-c" ]; then
	cd langparser
	java -jar antlr-4.5-rc-2-complete.jar -package langparser ECMAScript.g4
	javac -cp "../lib/*" *.java
	cd ..
	jar cvfm ECMAScript.jar langparser/Manifest.txt langparser/*.class langparser/antlr-4.5-rc-2-complete.jar
	mv ECMAScript.jar langparser/
	rm -rf langparser/*.class
elif [ "$1" == "-r" ]; then
	if [ "$2" == "js18" ]; then
		while true
		do
			jython -J-Xmx2048m GEInterpreterFuzzer.py 1
			echo "Spidermonkey"
		done
	elif [ "$2" == "js31" ]; then
		while true
		do
			jython -J-Xmx1024m GEInterpreterFuzzer.py 2
		done
	elif [ "$2" == "v8" ]; then
		while true
		do
			jython -J-Xmx1024m GEInterpreterFuzzer.py 3
		done
	elif [ "$2" == "gen" ]; then
		jython GEInterpreterFuzzer.py 0
	else
		echo "run [options]"
		echo "\"-r gen\" fragments generation"
		echo "\"-r js18\" Spidermonkey 1.8.5"
		echo "\"-r js31\" Spidermonkey 31"
		echo "\"-r v8\" Chrome V8"
	fi;
else 
	echo "run [options]"
	echo "\"-r gen\" fragments generation"
	echo "\"-r js18\" Spidermonkey 1.8.5"
	echo "\"-r js31\" Spidermonkey 31"
	echo "\"-r v8\" Chrome V8"
fi;