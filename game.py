from rules import Rules
from board import Board
import random
import os

class Game(object):
	"""docstring for Game"""
	def __init__(self, board):
		super(Game, self).__init__()
		self.rules = Rules()
		self.board = board
		self.xSize = board.getXSize()
		self.ySize = board.getYSize()


	def iterate(self):
		newBoard = Board(self.xSize, self.ySize)
		
		for i in xrange(self.xSize):
			for j in xrange(self.ySize):
				count = self.board.getAliveNeiburghs(i,j)
				state = self.board.isAlive(i,j)
				newState = self.rules.apply(count, state)
				newBoard.setState(i,j,newState)


		self.board = newBoard

	def playGame(self):
		while(not self.board.isAllDead()):
			self.iterate()
			self.printBoard()

	def printLines(self):
		line = '\n'
		for i in xrange(self.ySize):
			line += '-'

		print line + '\n'

	def printBoard(self):
		os.system('clear')
		self.printLines()
		print self.board.toString()
		self.printLines()

def genRandomBoard(xSize, ySize):
	board = Board(xSize, ySize)

	print board.getBoard()

	for i in xrange(xSize):
		for j in xrange(ySize):
			state = random.choice([True, False])
			board.setState(i,j,state)

	return board




initialBoard = Board(25,25)
initialBoard.load('cool.txt')


#initialBoard = genRandomBoard(30,190)
#initialBoard.save('board.txt')


game = Game(initialBoard)

game.printBoard()
game.playGame()
