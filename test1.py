from os.path import isfile, join
from os import listdir,stat,rename
TestCaseSubDirs=[]
class s(object):
	def __init__(self):
		self.count =0
	def listAllTestCasesDir(self,testCasesDir):
	        for f in listdir(testCasesDir):
	            fi=join(testCasesDir,f)
	            if not isfile(fi):
	                self.listAllTestCasesDir(fi)
	            else:
	            	if "shell.js" in f:
	            		if stat(fi).st_size != 0:
	            			print fi
	            			f1=open(fi,"r")
	            			f=open("/home/spandan/Desktop/shells/"+str(self.count)+".js","a+")
	            			f.write(f1.read())
	            			f.write("\n")
	            			f1.close()
	            			f.close()


if __name__ == '__main__':
	temp=s()
	temp.listAllTestCasesDir("/home/spandan/geinterpreterfuzz/mozillaJSTestSuite")
    