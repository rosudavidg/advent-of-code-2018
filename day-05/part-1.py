from math import fabs
from sys import stdin


data = stdin.readline()
index = 0

while index < data.__len__() - 1:
	if fabs(ord(data[index]) - ord(data[index + 1])) == ord('a') - ord('A'):
		data = data[:index] + data[index + 2:]
		index -= 2

	index = max([0, index + 1])

print(len(data))
