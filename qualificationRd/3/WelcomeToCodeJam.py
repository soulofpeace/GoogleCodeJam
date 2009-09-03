import sys
import os
import logging
import pdb

logger = logging.getLogger('WelcomeToCodeJam')
logger.setLevel(logging.INFO)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


def count(caseList, fixPhrase):
	#pdb.set_trace()
	if(len(caseList)<len(fixPhrase)):
		return 0
	if(len(fixPhrase)==0):
		return 1
	total=0
	while(len(caseList)>0):
		fixPhraseCopy = list(fixPhrase)
		logger.debug('caseList is %s' %(str(caseList)))
		logger.debug('fixPhrase is %s' %(str(fixPhraseCopy)))
		logger.debug('total is %i' %(total))
		try:
			testChar = fixPhraseCopy.pop(0)
			logger.debug('testChar is %s' %testChar)
			x = caseList.index(testChar)
			caseList = caseList[x+1:]
			caseListCopy = caseList
			total+=count(caseListCopy, fixPhraseCopy)
				
		except ValueError:
			logger.debug('I am here')
			break
	return total
			
		

def solve(input, output):
	numberOfCases = int(input.readline().strip())
	fixPhrase=list('welcome to code jam')
	for i in range(numberOfCases):
		caseList = list(input.readline().strip())
		ans =str(count(caseList, fixPhrase))[-4:]
		while len(ans)<4:
			ans='0'+ans
			
		logger.debug('Final total is %s' %ans)
		output.write('Case #%i: %s\n' %((i+1), ans))
	
		



def main():
	input = open(sys.argv[1], 'r')
	output = open(sys.argv[2], 'w')
	solve(input, output)	
	input.close()
	output.close()

if __name__=='__main__':
	main()
