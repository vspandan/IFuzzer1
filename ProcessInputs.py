from os import listdir, chdir, mkdir, system, stat
from os.path import isfile, join, isdir, exists

TestCases=[]
def listAllTestCasesDir(testCasesDir):
        for f in listdir(testCasesDir):
            fi=join(testCasesDir,f)
            if not isfile(fi):
                listAllTestCasesDir(fi)
            else:
            	if f.endswith("js"):
                    TestCases.append(fi)

def main():
	listAllTestCasesDir("/home/spandan/repo/geinterpreterfuzz/testsamples/tests_67eac0234f15")
	for test in TestCases:
		from subprocess import Popen,PIPE
		exec_cmd="timeout 2 /home/spandan/mozilla/centralrepo/mozilla-central/js/src/dist/bin/js -f /home/spandan/repo/geinterpreterfuzz/shell.js -f "+test
		p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
		(out,err)=p.communicate()
		print test
		print err


if __name__ == '__main__':
	main()