import os
import sys
import math

def calculateDistance(source, destination):
	distance = math.sqrt((destination[1]-source[1])**2+(destination[0]-source[0])**2)
	return distance


def calculateCost(itemProp, currentLocation, petrolPrice):
	#print itemProp
	perishable=itemProp[0]
	shops = itemProp[1:]
	min = -1
	futureLocation=[currentLocation[0], currentLocation[1]]
	for shop in shops:
		index = shop[0]
		coordinate = shop[1]
		price = shop[2]
		distanceToShop=calculateDistance(currentLocation, coordinate)
		totalDistance=distanceToShop
		if perishable:
			distanceBackHome=calculateDistance(coordinate, (0, 0))
			totalDistance = totalDistance+distanceBackHome
		petrolCost = totalDistance *petrolPrice
		#print 'petrol cost: %i' %petrolCost
		cost=petrolCost + price
		#print 'item cost : %i' %price
		#print 'totalCost: %i ' % cost
		if min==-1:
			min = cost
			if perishable:
				futureLocation =[0, 0]
			else:
				futureLocation=[coordinate[0], coordinate[1]]
		else:
			if(cost < min):
				min = cost
				if perishable:
					futureLocation =[0, 0]
				else:
					futureLocation=[coordinate[0], coordinate[1]]
	currentLocation[0]=futureLocation[0]
	currentLocation[1]=futureLocation[1]
	return min


def buy(items, currentLocation, petrolPrice, locationMap):
	minLocationMap=[]
	if(len(items) >0):
		min=-1
		for item in items.keys():
			currentLocationCopy = list(currentLocation)
			locationMapCopy = list(locationMap)
			itemCopy = dict(items)
			itemProp = itemCopy.pop(item)
			cost = calculateCost(itemProp, currentLocationCopy, petrolPrice)
			locationMapCopy.append((cost, item, tuple(currentLocationCopy)))
			totalCost = cost + buy(itemCopy, currentLocationCopy, petrolPrice, locationMapCopy)
			if (min==-1):
				min = totalCost
				minLocationMap=locationMapCopy
			else:
				if cost<=min:
					min = totalCost
					minLocationMap=locationMapCopy
		print 'item %i: %f' %(len(items), min)
		print minLocationMap
		return min
	else:
		distanceHome=calculateDistance(currentLocation, (0, 0))
		locationMap.append((distanceHome*petrolPrice, (0, 0)))
		return distanceHome * petrolPrice
		

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

def getPlan(inputFile):
	numberOfCase = int((inputFile.readline()).strip())
	for case in range(numberOfCase):
		details1= inputFile.readline().strip().split()
		numberOfItem = int(details1[0])
		numberOfStore = int(details1[1])
		petrolPrice= int(details1[2])
		items = readItemDetails(inputFile, numberOfItem)	
		readStoreDetails(inputFile, items, numberOfStore)
		currentLocation= [0, 0]
		locationMap=[tuple(currentLocation)]
		print '%.7f' %buy(items, currentLocation, petrolPrice, locationMap)
		#print  (numberOfCase, numberOfItem, numberOfStore, petrolPrice, items)

def main():
	inputFile = open(sys.argv[1], 'r')
	outputFile = open(sys.argv[2], 'w')
	getPlan(inputFile)
	

if __name__=='__main__':
	main()
