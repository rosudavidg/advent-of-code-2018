from sys import stdin

sums = set()
currentSum = 0
currentIndex = 0

numbers = list(map(int, stdin.readlines()))

while currentSum not in sums:
	sums.add(currentSum)

	currentSum += numbers[currentIndex]

	currentIndex += 1
	if currentIndex == numbers.__len__():
		currentIndex = 0

print(currentSum)
