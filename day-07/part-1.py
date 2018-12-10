from sys import stdin
from collections import OrderedDict


data = [[line.split()[1], line.split()[7]] for line in stdin.readlines()]
letters = OrderedDict()

for c1, c2 in data:
	if c1 not in letters:
		letters.update({(c1, 0)})

	if c2 not in letters:
		letters.update({(c2, 1)})
	else:
		letters.update({(c2, letters[c2] + 1)})

while any([True for key, value in letters.items() if value >= 0 ]):
	for key, value in sorted(letters.items()):
		if value == 0:
			print(key, end='')
			letters.update({(key, -1)})
			
			lst = [entry[1] for entry in data if entry[0] == key]

			for letter in lst:
				letters.update({(letter, letters[letter] - 1)})
			break
print()
