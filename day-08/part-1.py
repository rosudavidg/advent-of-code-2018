from sys import stdin


data = list()
index = 0


def solve():
	global data
	global index
	totalSum = 0

	childNodes = data[index]
	metadataEntries = data[index + 1]

	index += 2

	for _ in range(childNodes):
		totalSum += solve()

	for _ in range(metadataEntries):
		totalSum += data[index]
		index += 1

	return totalSum



if __name__ == '__main__':
	index = 0
	data = list(map(int, stdin.readline().split()))
	print(solve())
