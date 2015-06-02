if [ "$1" == "-c" ]; then
	cd langparser
	java -jar antlr-4.5-rc-2-complete.jar -package langparser ECMAScript.g4
	javac -cp "antlr-4.5-rc-2-complete.jar" *.java
	cd ..
	jar cvfm ECMAScript.jar langparser/Manifest.txt langparser/*.class langparser/antlr-4.5-rc-2-complete.jar
	mv ECMAScript.jar langparser/
	rm -rf langparser/*.class
elif [ "$1" == "-r" ]; then
	if [ "$2" == "js31" ]; then
		while true
		do
			jython -J-Xmx2000m GEInterpreterFuzzer.py 2
			echo "Spidermonkey-31"
			break
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