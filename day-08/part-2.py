from sys import stdin


data = list()
index = 0


def solve():
	global data
	global index
	lst = list()
	val = 0

	childNodes = data[index]
	metadataEntries = data[index + 1]

	index += 2

	for _ in range(childNodes):
		lst.append(solve())

	if childNodes == 0:
		for _ in range(metadataEntries):
			val += data[index]
			index += 1
	else:
		for i in range(metadataEntries):
			if data[index] <= len(lst):
				val += lst[data[index] - 1]
			index += 1

	return val



if __name__ == '__main__':
	index = 0
	data = list(map(int, stdin.readline().split()))
	print(solve())
