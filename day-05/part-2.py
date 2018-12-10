from math import fabs
from sys import stdin


def getLength(data):
	index = 0

	while index < len(data) - 1:
		if fabs(ord(data[index]) - ord(data[index + 1])) == 32:
			data = data[:index] + data[index + 2:]
			index -= 2

		index = max([0, index + 1])

	return data.__len__()


if __name__ == '__main__':
	data = stdin.readline()

	lengthList = [getLength(data)]

	for letterValue in [value for value in range(ord('a'), ord('z') + 1)]:
		newData = data.replace(chr(letterValue), '').replace(chr(letterValue - 32), '')
		lengthList.append(getLength(newData))


	print(min(lengthList))
