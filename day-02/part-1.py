from sys import stdin


counts = list()

for line in stdin.readlines():
	counts += list({line.count(chr(index)) for index in range(ord('a'), ord('z') + 1)})

print(counts.count(2) * counts.count(3))
