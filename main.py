import os
import sys

from src.Board import *

b = readBoardFromFile()
b.renderBoard()
b.move("d2", "d4")
b.renderBoard()

