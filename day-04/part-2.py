from re import split
from sys import stdin


data = list()
dct = dict()

for line in stdin.readlines():
	data.append(line)

data.sort()
init = tuple()

for _ in range(60):
	init += tuple([0])

start = 0
stop  = 0
guard = '#david'

for entry in data:
	tokens = split('-| |:', entry)

	if tokens[6][0] == '#':
		guard = tokens[6]

		if guard not in dct:
			dct.update({(guard, init)})
	elif tokens[5] == 'falls':
		start = int(tokens[4][:-1])
	elif tokens[5] == 'wakes':
		stop = int(tokens[4][:-1])

		foo = list(dct[guard])
		for i in range(start, stop):
			foo[i] += 1

		dct.update({(guard, tuple(foo))})

guardName = ''
minuteIndex = -1
times = -1

for key, value in dct.items():
	for i in range(60):
		if value[i] > times:
			times = value[i]
			minuteIndex = i
			guardName = key

print(int(guardName[1:]) * minuteIndex)
