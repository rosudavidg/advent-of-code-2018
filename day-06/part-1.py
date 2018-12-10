from math import fabs
from re import split
from sys import stdin


class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distanceTo(self, point):
		return abs(self.x - point.x) + abs(self.y - point.y)


class World():
	def __init__(self):
		self.map = list(list())
		self.points = list()
		self.width = 0
		self.height = 0

		self.readInput()
		self.setDimensions()
		self.initMap()

	def readInput(self):
		for line in stdin.readlines():
			parsedLine = split(' |, |\n', line)
			self.points.append(Point(int(parsedLine[1]), int(parsedLine[0])))

	def setDimensions(self):
		for point in self.points:
			if point.x > self.height:
				self.height = point.x

			if point.y > self.width:
				self.width = point.y

		self.height += 1
		self.width += 1

	def initMap(self):
		for _ in range(self.height):
			self.map.append(list('.' * self.width))

		for i in range(self.height):
			for j in range(self.width):
				self.map[i][j] = [0, -2]

	def computeMap(self):
		for i in range(self.height):
			for j in range(self.width):
				for pointIndex in range(self.points.__len__()):
					distance = self.points[pointIndex].distanceTo(Point(i, j))
	
					if self.map[i][j][1] == -2:
						self.map[i][j] = [distance, pointIndex]					
					elif distance < self.map[i][j][0]:
						self.map[i][j] = [distance, pointIndex]
					elif distance == self.map[i][j][0]:
						self.map[i][j][1] = -1

	def getInfiniteIndexPoints(self):
		ans = set()

		for i in range(self.height):
			ans.add(self.map[i][0][1])
			ans.add(self.map[i][self.width - 1][1])

		for j in range(self.width):
			ans.add(self.map[0][j][1])
			ans.add(self.map[self.height - 1][j][1])

		return ans

	def getAreas(self):
		areas = [0 for _ in range(self.points.__len__())]

		for i in range(self.height):
			for j in range(self.width):
				index = self.map[i][j][1]

				if index >= 0:
					areas[index] += 1			

		return areas


if __name__ == '__main__':
	world = World()
	world.computeMap()
	finitePointsSet = set([i for i in range(world.points.__len__())]).difference(world.getInfiniteIndexPoints())

	ans = 0
	areas = world.getAreas()

	for point in finitePointsSet:
		if areas[point] > ans:
			ans = areas[point]

	print(ans)
