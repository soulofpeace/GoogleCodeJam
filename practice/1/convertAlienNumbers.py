import sys

def parseTargetNumberSys(stringNumberSys):
	numberSys = {}
	numberSysToken = list(stringNumberSys)
	count = 0
	for token in numberSysToken:
		numberSys[count] = token
		count +=1
	return numberSys

def parseSourceNumberSys(stringNumberSys):
	numberSys = {}
	numberSysToken = list(stringNumberSys)
	count = 0
	for token in numberSysToken:
		numberSys[token] = count
		count +=1
	return numberSys


def convertSourceNumToDec(sourceNumSys, number):
	decNumber = 0
	placingPosition = 1
	for placing in number:
		currentWeight = len(sourceNumSys)**(len(number) -placingPosition)
		decNumber +=sourceNumSys[placing]* currentWeight
		placingPosition +=1
		
	return decNumber

def convertDecToTarget(targetNumSys, decNumber):
	targetNumber = ''
	while decNumber > 0:
		targetNumber = targetNumSys[decNumber%len(targetNumSys)] + targetNumber
		decNumber = decNumber /len(targetNumSys)
	return targetNumber

def convertInput(inputFile, outputFile):
	numCasesLine = 1
	count = 1
	numCases =-1
	for line in inputFile:
		line = line.strip()
		if count == numCasesLine:
			numCases = int(line)
		else:
			tokens = line.split()
			needToConvertNumberToken = tokens[0]
			sourceNumSys = parseSourceNumberSys(tokens[1])
			targetNumSys = parseTargetNumberSys(tokens[2])
			answer = convertDecToTarget(targetNumSys, convertSourceNumToDec(sourceNumSys, needToConvertNumberToken))
			print answer
			outputFile.write('Case #%i: %s \n' %(count-1, answer))
		count +=1

				

def main():
	inputFile = open(sys.argv[1], 'r')
	outputFile = open(sys.argv[2], 'w')
	convertInput(inputFile, outputFile)
	inputFile.close()
	outputFile.close()


if __name__=='__main__':
	main()
