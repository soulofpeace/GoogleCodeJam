import sys


def findMinTotalEggs(numFloor, breakEggs, dict):
	max = breakEggs
	minAnswer= -1
	min = 1
	test = (max+min)/2
	while min<=max :
		print 'minAnswer: %i, test: %i, min: %i, max: %i' %(minAnswer, test, min, max)
		maxF=findMaxFloor(test, breakEggs, dict)
		if maxF==-1:
			maxF=2**32
		if maxF >=numFloor:
			if minAnswer ==-1:
				minAnswer = test
			else:
				if test<minAnswer:
					minAnswer=test
			max = test-1
		else:
			min = test+1
		test = (max+min)/2
		
	if minAnswer ==-1:
		test =breakEggs
		maxF =findMaxFloor(test, breakEggs, dict)
		if maxF ==-1:
			maxF = 2**32
		while maxF <numFloor:
			test = test +1
			maxF =findMaxFloor(test, breakEggs, dict)
			if maxF ==-1:
				maxF = 2**32
		minAnswer = test
		
	return minAnswer
	

def findMinBreakEggs(numFloor, totalEggs, dict):
	max = totalEggs
	minAnswer=-1
	min = 1
	test = (max+min)/2
	while min <=max:
		maxF=findMaxFloor(totalEggs, test, dict)
		if maxF==-1:
			maxF=2**32
		if maxF >=numFloor:
			if minAnswer ==-1:
				minAnswer = test
			else:
				if test<minAnswer:
					minAnswer=test
			max = test-1
		else:
			min = test+1
			
		test = (max+min)/2
	return minAnswer
	
def findMaxFloor(totalEggs, breakEggs, dict):
	maxFloor=0
	if totalEggs >33:
		return -1
	if breakEggs >33:
		return -1
	for tEgg in range(0, totalEggs+1):
		for bEgg in range(breakEggs+1):
			if tEgg ==0 or bEgg ==0:
				dict[(tEgg, bEgg)]=0
			else:
				dict[(tEgg, bEgg)]=dict[(tEgg-1, bEgg)]+dict[(tEgg-1, bEgg-1)]+1
	if dict[(tEgg, bEgg)] >2**32:
		return -1
	else:
		return dict[(tEgg, bEgg)]

def findMaxFloorRecurse(totalEggs, breakEggs, dict):
	print 'total Eggs: %i\tbreak Eggs: %i' %(totalEggs, breakEggs)
	if totalEggs == 0 or breakEggs == 0:
		return 0
	else:
		if dict.has_key((totalEggs-1, breakEggs)):
			answer1 = dict[(totalEggs-1, breakEggs)]
		else:
			dict[(totalEggs-1, breakEggs)]=findMaxFloor(totalEggs-1, breakEggs, dict)
			answer1=dict[(totalEggs-1, breakEggs)]
		if dict.has_key((totalEggs-1, breakEggs-1)):
			answer2 = dict[(totalEggs-1, breakEggs-1)]
		else:
			dict[(totalEggs-1, breakEggs-1)]=findMaxFloor(totalEggs-1, breakEggs-1, dict)
			answer2=dict[(totalEggs-1, breakEggs-1)]
		return answer1+answer2+1
		
def compute(inputFile, outputFile):
	count = 0
	dict={}
	for line in inputFile:
		#print line
		if count==0:
			pass
		else:
			#print line
			line = line.strip()
			tokens = line.split()
			#print numFloor
			numFloor = int(tokens[0])
			totalEggs = int(tokens[1])
			breakEggs = int(tokens[2])
			maxFloor  = findMaxFloor(totalEggs, breakEggs, dict)
			print 'Max Floor: %i' %maxFloor
			minBreakEggs = findMinBreakEggs(numFloor, totalEggs, dict)
			print 'Min Break Eggs: %i' %minBreakEggs
			
			minTotalEggs = findMinTotalEggs(numFloor, breakEggs, dict)
			print 'Min Total Eggs: %i' %minTotalEggs
			
			#print maxFloor
			print 'Case #%i: %i %i %i \n' %(count, maxFloor, minTotalEggs, minBreakEggs)
			outputFile.write('Case #%i: %i %i %i \n' %(count, maxFloor, minTotalEggs, minBreakEggs))
			
		count = count+1
		
def main():
	inputFile = open(sys.argv[1], 'r')
	outputFile = open(sys.argv[2], 'w')
	compute(inputFile, outputFile)
	inputFile.close()
	outputFile.close()
	
	
if __name__=='__main__':
	main()
	
