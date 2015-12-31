from lizard import analyze_file
i = analyze_file("Bugs/21.js")
print i.__dict__
for index in range(len(i.function_list)):
	print i.function_list[index].__dict__