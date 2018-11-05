objects = 0
offset = 50
vars = {}
duplication_times = 3
file = 'C:/Users/xpaezr/Desktop/patch.pd'
originalFile = []

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
		
def isDuplicable(tokens):
	if len(tokens) > 1 and tokens[1] == 'floatatom' or tokens[1] == 'obj':
		return True
	else:
		return False
		
#look for variables
with open(file,'r') as f:
	originalFile = f.readlines();
	for line in originalFile:
		tokens = line.split()
		if len(tokens) > 4 and tokens[1] == 'text' and tokens[4] == 'VAR':
			vars[tokens[5]] = []
			index = 6
			while index < len(tokens):
				vars[tokens[5]].append(tokens[index])
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
			if isDuplicable(line.split()):
				duplicatedLine = line.split()
				#change if object is one of the vars, var is a dictionary
				if duplicatedLine[3] in vars:
					duplicatedLine[3] = duplicatedLine[3] + " " + str(vars[duplicatedLine[3]][index - 1])
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