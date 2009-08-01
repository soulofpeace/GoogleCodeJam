import sys

NORTH=0
EAST=1
SOUTH=2
WEST=3

cardinals=[NORTH, EAST, SOUTH, WEST]
outputDict = {(1, 0, 0, 0):'1', (0, 0, 1, 0):'2', (1, 0, 1, 0):'3', (0, 0, 0, 1):'4', (1, 0, 0, 1):'5', (0, 0, 1, 1):'6', (1, 0, 1, 1):'7', (0, 1, 0, 0):'8', (1, 1, 0, 0):'9', (0, 1, 1, 0):'a', (1, 1, 1, 0):'b', (0, 1, 0, 1):'c', (1, 1, 0, 1):'d', (0, 1, 1, 1):'e', (1, 1, 1, 1):'f'}
def move(currentCoordinate, currentDirection, mazeStructure):
	if currentDirection == NORTH:
		currentCoordinate[1] +=1
	if currentDirection == SOUTH:
		currentCoordinate[1] -=1
	if currentDirection == EAST:
		currentCoordinate[0] +=1
	if currentDirection == WEST:
		currentCoordinate[0] -=1
	lobangDir=cardinals[currentDirection+2 if currentDirection+2 <len(cardinals) else currentDirection+2 - len(cardinals)]
	#print mazeStructure
	#print currentCoordinate[0]
	if mazeStructure.has_key(currentCoordinate[1]):
		if mazeStructure[currentCoordinate[1]].has_key(currentCoordinate[0]):
			mazeStructure[currentCoordinate[1]][currentCoordinate[0]][cardinals[lobangDir]]=1
		else:
			mazeStructure[currentCoordinate[1]][currentCoordinate[0]]=[0, 0, 0, 0]
			mazeStructure[currentCoordinate[1]][currentCoordinate[0]][cardinals[lobangDir]]=1
	else:
		mazeStructure[currentCoordinate[1]]={}
		mazeStructure[currentCoordinate[1]][currentCoordinate[0]]=[0, 0, 0, 0]
		mazeStructure[currentCoordinate[1]][currentCoordinate[0]][cardinals[lobangDir]]=1
		

def isTopLeft(topLeftCoordinate, currentCoordinate):
	if currentCoordinate[0] <= topLeftCoordinate[0]:
		if currentCoordinate[1] >= topLeftCoordinate[1]:
			return True
	return False

def getMazeStructure(directionString, mazeStructure, currentCoordinate, currentDirection):
	#print directionString
	topleftCoordinate = (0, 0)
	directionTokens = list(directionString)[1: len(directionString)-1]
	#print directionTokens
	for token in directionTokens:
		if token =='W':
			move(currentCoordinate, currentDirection, mazeStructure)
			if isTopLeft(topleftCoordinate, currentCoordinate):
				topleftCoordinate = tuple(currentCoordinate)
			#print currentCoordinate
			#print dict[currentDirection]
			#print topleftCoordinate
		elif token=='L':
			currentDirection = cardinals[currentDirection-1]
		else:
			currentDirection = cardinals[currentDirection+1 if currentDirection+1<len(cardinals) else currentDirection+1 - len(cardinals)]
	return (topleftCoordinate, currentCoordinate, currentDirection)


def printMazeStructure(mazeStructure, topleftCoordinate):
	out=''
	topX = topleftCoordinate[0]
	topY = topleftCoordinate[1]
	countY = len(mazeStructure)
	for y in range(topY, topY-countY, -1):
		#print y
		#print mazeStructure[x]
		countX = len(mazeStructure[y])
		for x in range(topX, topX+countX, 1):
			#print x,
			out+=outputDict[tuple(mazeStructure[y][x])]
		out+='\n'
	return out


def start(inputFile, outputFile):
	case = 1
	count = 0
	for line in inputFile:
		if count == 0:
			#print line
			pass
		else:
			line = line.strip()
			tokens = line.split()
			fwdDir = tokens[0]
			bwdDir = tokens[1]
			mazeStructure={0:{0:[1, 0, 0, 0]}}
			currentCoordinate = [0, 0]
			topleftCoordinate1, currentCoordinate, exitDirection = getMazeStructure(fwdDir, mazeStructure, currentCoordinate, SOUTH)
			mazeStructure[currentCoordinate[1]][currentCoordinate[0]][exitDirection]=1
			lobangDir=cardinals[exitDirection+2 if exitDirection+2 <len(cardinals) else exitDirection+2 - len(cardinals)]
			#print 'start'+ str(currentCoordinate)+' '+ dict[lobangDir]
			#print 'end: ' + str(topleftCoordinate1)
			topleftCoordinate2, currentCoordinate, exitDirection = getMazeStructure(bwdDir, mazeStructure, currentCoordinate, lobangDir)
			if isTopLeft(topleftCoordinate1, topleftCoordinate2):
				topleftCoordinate = topleftCoordinate2
			else:
				topleftCoordinate = topleftCoordinate1
			
			
			#print mazeStructure
			#print '*'*30
			#for key1, value1 in mazeStructure.iteritems():
			#	for key2, value2 in value1.iteritems():
					#print key1,
					#print key2,
					#print value2,
				#print
			#print '*'*30
			out=printMazeStructure(mazeStructure, topleftCoordinate)
			outputFile.write('Case #%i: \n' % count)
			outputFile.write(out)
		count +=1		
		

def main():
	inputFile = open(sys.argv[1], 'r')
	outputFile = open(sys.argv[2], 'w')
	start(inputFile, outputFile)
	inputFile.close()
	outputFile.close()

if __name__=='__main__':
	main()
