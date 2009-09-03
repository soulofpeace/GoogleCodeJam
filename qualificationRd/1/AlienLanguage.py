import sys
import os
import re
import logging


logger = logging.getLogger('AlienWord')
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


def convertToRegex(testCase):
	regex1 = testCase.replace('(', '[')
	logger.debug('Regex Test Case stage1: %s' %regex1)
	regex2 = regex1.replace(')', ']')
	logger.debug('Regex Test Case stage2: %s' %regex2)
	regex2list = list(regex2)
	flag =False
	regexFinal=''
	for i in range(len(regex2list)):
		char = regex2list[i]
		logger.debug('Character is :%s '% char)
		if char=='[':
			flag =True
		elif char==']':
			flag =False
		if flag:
			if char!='[':
				regexFinal = regexFinal+'|'+char
			else:	
				regexFinal = regexFinal+char
		else:
			regexFinal = regexFinal+char
	logger.debug('Regex final: %s' %regexFinal)		
	return regexFinal

def countMatch(wordList, regexFinal):
	regex = re.compile(regexFinal)
	count = 0
	for word in wordList:
		if(regex.match(word)):
			count +=1
	return count

def check(wordList, previousChar):
	for word in wordList:
		if word.startswith(previousChar):
			return True
	return False

def checkTestCase(wordList, testCase, previousChar):
	logger.debug('Checking %s with previousChar %s' %(testCase, previousChar))
	if(len(testCase)==0):
		return 1
	else:
		if testCase.startswith('('):
			testCaseTest= testCase[1:testCase.index(')')]
			count = 0
			for i in range(len(testCaseTest)):
				temp = previousChar
				temp += str(testCaseTest[i])
				logger.debug('Checking whether any word starts with: %s' %temp)
				if check(wordList, temp):
					start = testCase.index(')')+1
					if start < len(testCase):
						count +=checkTestCase(wordList, testCase[start:], temp)
					else:
						count +=1
			return count
		else:
			previousChar+=str(testCase[0])
			check(wordList, previousChar)
			if check(wordList, previousChar):
				return checkTestCase(wordList, testCase[1:], previousChar)
			else:
				return 0

def solve(inputFile, outputFile):
	wordList=[]
	testCases=[]
	testDetails=(inputFile.readline().strip()).split()
	numberOfAlphabets= int(testDetails[0])
	logger.debug('Number of Alphabets: %i' %numberOfAlphabets)
	numberOfWords=int(testDetails[1])
	logger.debug('Number of words: %i' %numberOfWords)
	numberOfTestCases=int(testDetails[2])
	logger.debug('Number of TestCases: %i' %numberOfTestCases)
	for i in range(numberOfWords):
		word = inputFile.readline().strip()
		logger.debug('Word %i : %s' %(i, word))
		wordList.append(word)
	
	for j in range(numberOfTestCases):
		testCase = inputFile.readline().strip()
		logger.debug('Original testCase %i: %s' %(j, testCase))
		#for normal case
		outputFile.write('Case #%i: %i\n' %(j+1, checkTestCase(wordList, testCase, ''))) 
		logger.debug('Case #%i: %i' %(j+1, checkTestCase(wordList, testCase, '')))
		#for regex case
		'''
		regexFinal= convertToRegex(testCase)
		count=countMatch(wordList, regexFinal)
		outputFile.write('Case #%i: %i\n' %(j+1, count)) 
		logger.debug('Case #%i: %i\n' %(j+1, count))
		'''
def main():	
	inputFile =open(sys.argv[1], 'r')
	outputFile = open(sys.argv[2], 'w')
	solve(inputFile, outputFile)
	inputFile.close()
	outputFile.close()


if __name__=="__main__":
	main()
