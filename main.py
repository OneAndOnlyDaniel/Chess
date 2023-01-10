import os
import sys

from src.Board import *

b = readBoardFromFile()
b.renderBoard()

#b.move("a3", "b6")