class Board:
	def __init__(self):
		self.Board = [0,1,2,3,4,5,6,7,8]
		self.complete = False
	def move(self, location, value):
		if (self.Board[location]!="X" and self.Board[location]!="Y"):
			self.Board[location] = value;
	def display(self):
		print(self.Board[0], self.Board[1], self.Board[2]);
		print(self.Board[3], self.Board[4], self.Board[5]);
		print(self.Board[6], self.Board[7], self.Board[8]);
		#print board
	def hasWon(self):
		if (self.Board[0] == self.Board[1] == self.Board[2]):
			return (True, self.Board[0])
		elif (self.Board[3] == self.Board[4] == self.Board[5]):
			return (True, self.Board[3])
		elif (self.Board[0] == self.Board[3] == self.Board[6]):
			return (True, self.Board[0])
		elif (self.Board[1] == self.Board[4] == self.Board[7]):
			return (True, self.Board[1])
		elif (self.Board[2] == self.Board[5] == self.Board[8]):
			return (True, self.Board[2])
		elif (self.Board[0] == self.Board[4] == self.Board[8]):
			return (True, self.Board[0])
		elif (self.Board[2] == self.Board[4] == self.Board[6]):
			return (True, self.Board[2])
		else:
			return False
		#if player won, return true and who won

Game = Board()
print("Welcome to Tic Tac Toe!");
Player = "X"
gameOver = False
print(gameOver==False)

while gameOver == False:
	print "Player %s, please select a board location (1-9)" % Player
	Spot = input()
	Game.move(Spot, Player)
	Game.display()
	gameOver = Game.hasWon()
	winner = Player
	if Player == "Y":
		Player = "X"
	elif Player == "X":
		Player = "Y"

print "%s won" % winner