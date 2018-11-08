import sys

objects = 0
offset = 150
vars = {}
duplication_times = int(sys.argv[2])
file = sys.argv[1]
originalFile = []
replace_tokens = sys.argv[3];

#program call -> new.py C:/users/file 2 "select 98 99: key 99 100"

def isObj(tokens):
	if len(tokens) > 1 and tokens[1] == 'floatatom' or tokens[1] == 'obj' or tokens[1] == 'text':
		return True
	else:
		return False
	
def isWire(tokens):
	if len(tokens) > 1 and tokens[1] == 'connect':
		return True
	else:
		return False
		
with open(file,'r') as f:
	originalFile = f.readlines()
		
#look for variables, an instruction is an object and its values, e.g select 97 98 99
for instruction in replace_tokens.split(":"):
	object = instruction.split()[0]
	vars[object] = []
	index = 1
	while index < len(instruction.split()):
		vars[object].append(instruction.split()[index])
		index = index + 1

print(vars)

#count objects
for line in originalFile:
			if isObj(line.split()):
				objects = objects + 1
					
index = 1
while index < duplication_times:	
	#read lines form file and duplicate objects
	with open(file,'a+') as f:
		for line in originalFile:
			if isObj(line.split()):
				duplicatedLine = line.split()
				#change if object is one of the vars, var is a dictionary
				for key in vars.keys():
					if key + ";" in duplicatedLine:
						duplicatedLine[4] = duplicatedLine[4].replace(";","") +  " " + vars[key][index - 1].replace(";","") + ";" 
				#change position value
				#parse to int in order to increment
				duplicatedLine[2] = int(duplicatedLine[2]) + (offset * index)
				#parse to str in order to print
				duplicatedLine[2] = str(duplicatedLine[2])
				newLine = "\n" + " ".join(duplicatedLine) 
				f.write(newLine)
	#read lines form file and duplicate wires, it has to be done once the objcets has been counted
	with open(file,'a+') as f:
		for line in originalFile:
			if isWire(line.split()):
				duplicatedLine = line.split()
				#change connections value
				#parse to int in order to increment
				duplicatedLine[2] = int(duplicatedLine[2]) + (objects * index)
				duplicatedLine[4] = int(duplicatedLine[4]) + (objects * index)
				#parse to str in order to print
				duplicatedLine[2] = str(duplicatedLine[2])
				duplicatedLine[4] = str(duplicatedLine[4])
				newLine = "\n" + " ".join(duplicatedLine) 
				f.write(newLine)
	index = index + 1