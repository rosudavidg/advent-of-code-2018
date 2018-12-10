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
				self.map[i][j] = 0

	def computeMap(self):
		ans = 0

		for i in range(self.height):
			for j in range(self.width):
				for pointIndex in range(self.points.__len__()):
					distance = self.points[pointIndex].distanceTo(Point(i, j))
					self.map[i][j] += distance

				if self.map[i][j] < 10000:
					ans += 1
		return ans


if __name__ == '__main__':
	print(World().computeMap())
