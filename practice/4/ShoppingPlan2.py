import os
import sys
import math


class node:
	def __init__(item=None, location, cost=0):
		self.children=[]
		self.item = item
		self.location = location
		self.cost = cost
		self.parent = parent


def calculateDistance(source, destination):
	distance = math.sqrt((destination[1]-source[1])**2+(destination[0]-source[0])**2)
	return distance


	


def buildTree(items, petrolPrice, node, costDict, perishable):
	for item in items.keys():
		itemsCopy = dict(items)		
		itemProp = itemCopy.pop(item)
		shops = itemProp[1]
		for shop in shops:
			index=shop[0]
			coordinate=shop[1]
			price = shop[2]
			if perishable:
				if coordinate == node.location:
					totalCost = price + calculateDistance(node.location, coordinate)
				else:
					if(costDict.has_key((node.location, (0, 0)))):
						totalCost = costDict[(node.location, (0, 0))]
					else:
						costDict[(node.location, (0, 0)]=calcuateDistance(node.location, (0, 0))
						totalCost=costDict[(node.location), (0, 0)]
					homeNode = node('', (0, 0), totalCost)
					node.children.append(homeNode)
					perishable = itemProp[0]
			else:
				totalCost = price + calculateDistance(node.location, coordinate)
				perishable = itemProp[0]
				
			childNode = node(item, coordinate, totalCost))
			node.children.append(childNode)
			buildTree(items, petrolPrice, childNode, costDict, perishable)
		

def readItemDetails(inputFile, numberOfItem):
	itemDetails=inputFile.readline().split()
	items={}
	for i in itemDetails:
		if i.endswith('!'):
			items[i.strip('!')]=[1]
		else:
			items[i]=[0]
	return items


def readStoreDetails(inputFile, items, numberOfStore):
	for i in range(numberOfStore):
		storeDetails= inputFile.readline().strip().split()
		x = int(storeDetails[0])
		y = int(storeDetails[1])
		for storeItem in storeDetails[2:]:
			item= storeItem.split(':')[0]
			price = int(storeItem.split(':')[1])
			items[item].append([i+1, (x, y), price])

def getPlan(inputFile, outputFile):
	numberOfCase = int((inputFile.readline()).strip())
	for case in range(numberOfCase):
		details1= inputFile.readline().strip().split()
		numberOfItem = int(details1[0])
		numberOfStore = int(details1[1])
		petrolPrice= int(details1[2])
		items = readItemDetails(inputFile, numberOfItem)	
		readStoreDetails(inputFile, items, numberOfStore)
		costDict={}
		startNode=node('', (0, 0), cost)
		buildTree(items, petrolPrice, startNode, costDict, 0)
		outputFile.write('Case #%i: %.7f \n' %(case+1, findMin(startNode)))
		print items
		#print  (numberOfCase, numberOfItem, numberOfStore, petrolPrice, items)

def main():
	inputFile = open(sys.argv[1], 'r')
	outputFile = open(sys.argv[2], 'w')
	getPlan(inputFile, outputFile)
	inputFile.close()
	outputFile.close()
	



if __name__=='__main__':
	main()
