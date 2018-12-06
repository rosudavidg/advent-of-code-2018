from sys import stdin

data = [line.replace('\n', '') for line in stdin.readlines()]

for i in range(data.__len__() - 1):
	for j in range(i + 1, data.__len__()):
		diff_index = [index for index in range(len(data[i])) if data[i][index] != data[j][index]]
		index = diff_index[0]
		
		if len(diff_index) == 1:
			print(data[i][:index] + data[i][index + 1:])
			exit(0)
