from sys import stdin


class Game():
	def __init__(self, players, lastMarble):
		self.table = [0]
		self.players = players
		self.lastMarble = lastMarble
		self.currentMarble = 0
		self.currentMarblePosition = 0
		self.currentPlayer = 0
		self.scores = list([0] * players)

	def getNextPosition(self):
		position = self.currentMarblePosition + 1

		if position >= len(self.table):
			position -= len(self.table)

		return position

	def getNextPositionWithOffset(self, offset):
		position = self.currentMarblePosition + offset

		while position >= len(self.table):
			position -= len(self.table)

		while position < 0:
			position += len(self.table)

		return position

	def incrementCurrentPlayer(self):
		self.currentPlayer += 1

		if self.currentPlayer >= self.players:
			self.currentPlayer = 0

	def start(self):
		while self.currentMarble != self.lastMarble:
			self.currentMarble += 1

			if self.currentMarble % 23 == 0:
				self.currentMarblePosition = self.getNextPositionWithOffset(-7)
				self.scores[self.currentPlayer] += self.currentMarble + self.table[self.currentMarblePosition]
				del self.table[self.currentMarblePosition]
				
				if self.currentMarblePosition > len(self.table):
					self.currentMarblePosition = 0

			else:
				self.currentMarblePosition = self.getNextPositionWithOffset(1) + 1
				self.table.insert(self.currentMarblePosition, self.currentMarble)
			
			self.incrementCurrentPlayer()

	def getMaxScore(self):
		return max(self.scores)


if __name__ == '__main__':
	data = stdin.readline().split()

	game = Game(int(data[0]), int(data[6]))
	game.start()
	print(game.getMaxScore())
