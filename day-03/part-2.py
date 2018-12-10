from sys import stdin


zones = dict()
notok = set()

for line in stdin.readlines():
	[ID, _, startToken, dimToken] = line.split(' ')
	
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
				notok.add(zones[key][1])
				notok.add(ID)
				zones.update({(key, tuple([zones[key][0] + 1, ID]))})

			else:
				zones.update({(key, tuple([1, ID]))})

for val, idu in zones.values():
	if idu not in notok:
		print(idu[1:])
		break
