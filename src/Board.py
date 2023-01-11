from colorama import Fore, Back, Style

class Board:
	def __init__(self, board = 0, turnNumber = 1, player1="Player1", player2="Player2", moves = []):
		self.board = board
		self.turnNumber = turnNumber
		self.player1 = player1
		self.player2 = player2
		self.moves = moves

	def __str__(self):
		s = "{0},{1},{2}\n".format(self.turnNumber, self.player1, self.player2)
		for y in range(8):
			for x in range(8):
				# Board numbering is from bottom left, but array indexing is from top left
				s = s + self.board[7 - y][x]
			s = s + "\n"
		
		s = s + self.moves
		return s

	def move(self, a, b):
		p = CTI(a)
		q = CTI(b)

		temp = self.getIndex(q)

		self.setIndex(q, self.getIndex(p))
		self.setIndex(p, ".")

	def setIndex(self, ind, inp):
		y = ind[1]
		x = ind[0]
		s = self.board[y][x]

		self.board[y] = self.board[y][:x] + inp + self.board[y][x + 1:]

	def getIndex(self, ind):
		# Assumes ind = [x, y]
		return self.board[ind[1]][ind[0]]

	def renderBoard(self, selected = ""):
		if selected == "":
			ySel = -1
			xSel = -1
		else:
			p = CTI(selected)
			ySel = 7 - p[1]
			xSel = p[0]

		for y in range(8):
			row = ""
			for x in range(8):
				# Board numbering is from bottom left, but array indexing is from top left
				temp = self.board[7 - y][x]
				if temp == ".":
					temp = " "

				isWhite = temp.islower()
				temp = temp.upper()

				if (x + y) % 2 == 0:
					temp = Back.WHITE + temp
				else:
					temp = Back.BLACK + temp

				if self.board[7 - y][x] != " ":
					if y == ySel and x == xSel:
						temp = Style.BRIGHT + temp

					if isWhite: # Player is black
						temp = Fore.RED + temp
					else:
						temp = Fore.GREEN + temp

				temp = temp + Style.RESET_ALL

				row = row + temp
			print("\t\t" + str(7 - y + 1) + "  " + row)

		print()
		print("\t\t   abcdefgh")

# Coordinate to Index
def CTI(coord):
	if coord[0].isalpha():
		x = ord(coord[0]) - 97
	else:
		x = int(coord[0]) - 1

	y = int(coord[1]) - 1

	return [x, y]

def readBoardFromFile(name = "startingPosition"):
	# Removes any extension
	name = name.split(".")[0]
	f = open("src/Boards/{0}.txt".format(name), "r")
	s = f.read()
	f.close()

	ssplit = s.split("\n")
	firstRow = ssplit[0].split(",")
	turnNumber = int(firstRow[0])
	p1 = firstRow[1]
	p2 = firstRow[2]

	board = ssplit[1:9]
	print(board)
	moves = ssplit[9]

	return Board(board, turnNumber, p1, p2, moves)