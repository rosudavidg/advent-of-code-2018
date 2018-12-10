from sys import stdin


zones = dict()

for line in stdin.readlines():
	[_, _, startToken, dimToken] = line.split(' ')
	
	[startW, startH] = startToken.split(',')
	startW = int(startW)
	startH = int(startH[:-1])
	
	[dimW, dimH] = dimToken.split('x')

	if dimH[-1] == '\n':
		dimH = dimH[:-1]

	dimW = int(dimW)
	dimH = int(dimH)

	for i in range(startH, startH + dimH):
		for j in range(startW, startW + dimW):
			key = tuple([i, j])

			if key in zones:
				zones.update({(key, zones[key] + 1)})
			else:
				zones.update({(key, 1)})

count = 0
for value in zones.values():
	if value >= 2:
		count += 1
		
print(count)
