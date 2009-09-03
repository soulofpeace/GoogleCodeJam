import sys
import os
import logging
import math

logger = logging.getLogger('WaterSheds')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


		

class cell:
	def __init__(self, row, column):
		self.flow=(-1, -1)
		self.altitude=-1
		self.child=set()
		self.sink=(row, column)
		
	def __str__(self):
		return str(self.altitude)

def check(coord, altitudeMap):
	if coord[0]>=0 and coord[0] < len(altitudeMap):
		if coord[1] >=0 and coord[1] < len(altitudeMap[coord[0]]):
			return True
	return False

def update(flow, altitudeMap):
	destination = altitudeMap[flow[0]][flow[1]].flow
	if destination!=(-1, -1):
		altitudeMap[destination[0]][destination[1]].child=altitudeMap[destination[0]][destination[1]].child.union(altitudeMap[flow[0]][flow[1]].child)
		update(destination, altitudeMap)
	else:
		if flow==(-1, -1):
			logger.debug('Hey flow is (-1, -1)')
		for c in altitudeMap[flow[0]][flow[1]].child:
			altitudeMap[c[0]][c[1]].sink=flow
		return 
	
def compareSink(x , y):
	distx = math.sqrt(x[0]**2+x[1]**2)
	disty=  math.sqrt(y[0]**2+y[1]**2)
	return cmp(distx, disty)

def computeBasin(altitudeMap):
	for i in range(len(altitudeMap)):
		for j in range(len(altitudeMap[i])):
			c = altitudeMap[i][j]
			logger.debug('Calculating flow for (%i, %i) ' %(i, j))
			flow=(-1, -1)
			minAltitude=10000
			northCoord =(i-1, j)
			westCoord =(i, j-1)
			eastCoord=(i, j+1)
			southCoord=(i+1, j)
			checkList =[northCoord, westCoord, eastCoord, southCoord]
			for coord in checkList:
				if check(coord, altitudeMap):
					if (altitudeMap[coord[0]][coord[1]]).altitude < minAltitude:
						flow =coord
						minAltitude=altitudeMap[flow[0]][flow[1]].altitude
			if flow==(-1, -1):
				logger.debug('Hey why is it -1, -1')
			logger.debug('flow is %s' %(str(flow)))
			if c.altitude > altitudeMap[flow[0]][flow[1]].altitude:
					c.flow = flow
					logger.debug('Child for (%i, %i): %s' %(i, j, str(c.child)))
					altitudeMap[flow[0]][flow[1]].child.add((i, j))
					altitudeMap[flow[0]][flow[1]].child=altitudeMap[flow[0]][flow[1]].child.union(c.child)
					update(flow, altitudeMap)
					

def printLabel(altitudeMap, outputFile):
	sinkLabelDict={}
	label='a'
	for i in range(len(altitudeMap)):
		row=''
		for j in range(len(altitudeMap[i])):
			sink=altitudeMap[i][j].sink
			logger.debug('sink for %s is % s' %(str((i, j)), str(sink)))
			if sinkLabelDict.has_key(sink):
				row +=sinkLabelDict[sink]+' '
			else:
				sinkLabelDict[sink]=label
				label = chr(ord(label)+1)
				row +=sinkLabelDict[sink]+' '
		row=row.strip()
		outputFile.write(row+'\n')
	

	

def solve(input, output):
	numberOfCase = int(input.readline())
	for i in range(numberOfCase):
		altitudeMap=[]
		#sink=[]
		#cellDict={}
		logger.debug('Case %i' %(i+1))
		mapDimension=map(int, input.readline().strip().split())
		logger.debug('Map dimension: %s' %str(mapDimension))
		for row in range(mapDimension[0]):
			altitudeDetails=input.readline().strip().split()
			rowDetails=[]
			for col in range(mapDimension[1]):
				c = cell(row, col)
				c.altitude = int(altitudeDetails[col])
				#cellDict[(row, col)]=c
				rowDetails.append(c)
			logger.debug('Row %i: %s' %(row, str(map(str, rowDetails))))
			altitudeMap.append(rowDetails)
		computeBasin(altitudeMap)
		#logger.debug('Sink is %s' %str(map(str, sink)))
		output.write('Case #%i:\n' %(i+1))
		printLabel(altitudeMap, output)
	


def main():
	input = open(sys.argv[1], 'r')
	output = open(sys.argv[2], 'w')
	solve(input, output)	
	input.close()
	output.close()

if __name__=='__main__':
	main()
