class Board(object):
	def __init__(self, xSize, ySize):
		super(Board, self).__init__()
		self.board = [[False for x in xrange(ySize)] for x in xrange(xSize)] 
		self.xSize = xSize
		self.ySize = ySize

	def translate(self, i, size):
		while(i<0):
			i += size

		return i % size

	def isAlive(self, x, y):
		x = self.translate(x, self.xSize)
		y = self.translate(y, self.ySize)
		return self.board[x][y]

	def setState(self, x, y, state):
		x = self.translate(x, self.xSize)
		y = self.translate(y, self.ySize)
		self.board[x][y] = state

	def getAliveNeiburghs(self, x, y):
		count = 0

		for i in xrange(-1, 2):
			for j in xrange(-1, 2):
				if self.isAlive(x+i, y+j) and not (i == 0 and j == 0):
					count += 1

		return count

	def isAllDead(self):
		for i in xrange(self.xSize):
			for j in xrange(self.ySize):
				if self.isAlive(i,j) == True:
					return False

		return True

	def save(self, fileName):
		content = self.toString()
		f = open(fileName, 'w')
		f.write(content)
		f.close()

	def load(self, fileName):
		f = open(fileName, 'r')
		lines = f.readlines()
		self.xSize = len(lines)		
		self.ySize = len(lines[0]) - 1

		self.board = [[False for x in xrange(self.xSize)] for x in xrange(self.ySize)] 


		for i in xrange(self.xSize):
			for j in xrange(self.ySize):
				if lines[i][j] == 'x':
					self.setState(i, j, True)
		
		

	def toString(self):
		content = ''
		for i in xrange(self.xSize):
			for j in xrange(self.ySize):
				if self.isAlive(i,j) == True:
					content += 'x'
				else:
					content += ' '
			content += '\n'

		return content[:-1]



	def getXSize(self):
		return self.xSize

	def getYSize(self):
		return self.ySize


	def getBoard(self):
		return self.board