from sys import stdin


data = [line.replace('\n', '') for line in stdin.readlines()]

for i in range(len(data) - 1):
	for j in range(i + 1, len(data)):
		diff_index = [index for index in range(len(data[i])) if data[i][index] != data[j][index]]
		
		if len(diff_index) == 1:
			print(data[i][:diff_index[0]] + data[i][diff_index[0] + 1:])
			exit(0)
