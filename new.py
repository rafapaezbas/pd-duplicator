objects = 0
offset = 50
vars = {}

def isObj(tokens):
	if len(tokens) > 1 and tokens[1] == 'floatatom' or tokens[1] == 'obj':
		return True
	else:
		return False
		

def isWire(tokens):
	if len(tokens) > 1 and tokens[1] == 'connect':
		return True
	else:
		return False
		
#look for variables
with open('C:/Users/xpaezr/Desktop/patch.pd','r+') as f:
	lines = f.readlines()
	for line in lines:
		tokens = line.split()
		if len(tokens) > 5 and tokens[1] == 'text' and tokens[4] == 'VAR':
			vars[tokens[5]] = []
			
			index = 6
			while index < len(tokens):
				vars[tokens[5]].append(tokens[index])
				index = index + 1
			
			
print(vars)

#read lines form file and duplicate objects
with open('C:/Users/xpaezr/Desktop/patch.pd','r+') as f:
	lines = f.readlines()
	#check if every line is an object
	for line in lines:
		if isObj(line.split()):
			objects = objects + 1
			duplicatedLine = line.split()
			#change position value
			#parse to int in order to increment
			duplicatedLine[2] = int(duplicatedLine[2]) + offset
			#parse to str in order to print
			duplicatedLine[2] = str(duplicatedLine[2])
			newLine = "\n" + " ".join(duplicatedLine) 
			f.write(newLine)
			
#read lines form file and duplicate wires
with open('C:/Users/xpaezr/Desktop/patch.pd','r+') as f:
	lines = f.readlines()
	#check if every line is an object
	for line in lines:
		if isWire(line.split()):
			duplicatedLine = line.split()
			#change connections value
			#parse to int in order to increment
			duplicatedLine[2] = int(duplicatedLine[2]) + objects
			duplicatedLine[4] = int(duplicatedLine[4]) + objects
			#parse to str in order to print
			duplicatedLine[2] = str(duplicatedLine[2])
			duplicatedLine[4] = str(duplicatedLine[4])
			newLine = "\n" + " ".join(duplicatedLine) 
			f.write(newLine)