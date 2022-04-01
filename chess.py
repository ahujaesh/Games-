import numpy as np
import emoji

board = np.chararray((8,9),unicode = True)
tiles = np.chararray((8,9),unicode = True)
#print(emoji.emojize(':banana:'))
  
print("Welcome to 2 player chess!")
def charecters():
  board[1][0] = "👑"
  board[1][1] = "👑"
  board[1][2] = "👑"
  board[1][3] = "👑"
  board[1][4] = "👑"
  board[1][5] = "👑"
  board[1][6] = "👑"
  board[1][7] = "👑"

  board[6][0] = "🍌"
  board[6][1] = "🍌"
  board[6][2] = "🍌"
  board[6][3] = "🍌"
  board[6][4] = "🍌"
  board[6][5] = "🍌"
  board[6][6] = "🍌"
  board[6][7] = "🍌"

  board[7][0] = "🍍"
  board[7][7] = "🍍"
  board[7][1] = "🥝"
  board[7][6] = "🥝"
  board[7][3] = "🍩"
  board[7][4] = "🍰"
  board[7][2] = "🍓"
  board[7][5] = "🍓"

  board[0][3] = "🤴"
  board[0][4] = "👸"
  board[0][0] = "🏰"
  board[0][7] = "🏰"
  board[0][1] = "🐴"
  board[0][6] = "🐴"
  board[0][5] = "🧙"
  board[0][2] = "🧙"



def line2():
  board[2][0] = "⬜"
  board[2][1] = "⬛"
  board[2][2] = "⬜"
  board[2][3] = "⬛"
  board[2][4] = "⬜"
  board[2][5] = "⬛"
  board[2][6] = "⬜"
  board[2][7] = "⬛"

def line3():
  board[3][0] = "⬛"
  board[3][1] = "⬜"
  board[3][2] = "⬛"
  board[3][3] = "⬜"
  board[3][4] = "⬛"
  board[3][5] = "⬜"
  board[3][6] = "⬛"
  board[3][7] = "⬜"

def line4():
  board[4][0] = "⬜"
  board[4][1] = "⬛"
  board[4][2] = "⬜"
  board[4][3] = "⬛"
  board[4][4] = "⬜"
  board[4][5] = "⬛"
  board[4][6] = "⬜"
  board[4][7] = "⬛"

def line5():
  board[5][0] = "⬛"
  board[5][1] = "⬜"
  board[5][2] = "⬛"
  board[5][3] = "⬜"
  board[5][4] = "⬛"
  board[5][5] = "⬜"
  board[5][6] = "⬛"
  board[5][7] = "⬜"

def tiles0():
  tiles[0][0] = "⬜"
  tiles[0][1] = "⬛"
  tiles[0][2] = "⬜"
  tiles[0][3] = "⬛"
  tiles[0][4] = "⬜"
  tiles[0][5] = "⬛"
  tiles[0][6] = "⬜"
  tiles[0][7] = "⬛"

def tiles1():
  tiles[1][0] = "⬛"
  tiles[1][1] = "⬜"
  tiles[1][2] = "⬛"
  tiles[1][3] = "⬜"
  tiles[1][4] = "⬛"
  tiles[1][5] = "⬜"
  tiles[1][6] = "⬛"
  tiles[1][7] = "⬜"

def tiles2():
  tiles[2][0] = "⬜"
  tiles[2][1] = "⬛"
  tiles[2][2] = "⬜"
  tiles[2][3] = "⬛"
  tiles[2][4] = "⬜"
  tiles[2][5] = "⬛"
  tiles[2][6] = "⬜"
  tiles[2][7] = "⬛"

def tiles3():
  tiles[3][0] = "⬛"
  tiles[3][1] = "⬜"
  tiles[3][2] = "⬛"
  tiles[3][3] = "⬜"
  tiles[3][4] = "⬛"
  tiles[3][5] = "⬜"
  tiles[3][6] = "⬛"
  tiles[3][7] = "⬜"

def tiles4():
  tiles[4][0] = "⬜"
  tiles[4][1] = "⬛"
  tiles[4][2] = "⬜"
  tiles[4][3] = "⬛"
  tiles[4][4] = "⬜"
  tiles[4][5] = "⬛"
  tiles[4][6] = "⬜"
  tiles[4][7] = "⬛"

def tiles5():
  tiles[5][0] = "⬛"
  tiles[5][1] = "⬜"
  tiles[5][2] = "⬛"
  tiles[5][3] = "⬜"
  tiles[5][4] = "⬛"
  tiles[5][5] = "⬜"
  tiles[5][6] = "⬛"
  tiles[5][7] = "⬜"


def tiles6():
  tiles[6][0] = "⬜"
  tiles[6][1] = "⬛"
  tiles[6][2] = "⬜"
  tiles[6][3] = "⬛"
  tiles[6][4] = "⬜"
  tiles[6][5] = "⬛"
  tiles[6][6] = "⬜"
  tiles[6][7] = "⬛"

def tiles7():
  tiles[7][0] = "⬛"
  tiles[7][1] = "⬜"
  tiles[7][2] = "⬛"
  tiles[7][3] = "⬜"
  tiles[7][4] = "⬛"
  tiles[7][5] = "⬜"
  tiles[7][6] = "⬛"
  tiles[7][7] = "⬜"

def x():
  print("    0    1    2    3    4    5    6    7")

def numbers():
  board[0][8] = "0"
  board[1][8] = "1"
  board[2][8] = "2"
  board[3][8] = "3"
  board[4][8] = "4"
  board[5][8] = "5"
  board[6][8] = "6"
  board[7][8] = "7"


charecters()
line2()
line3()
line4()
line5()
tiles0()
tiles1()
tiles2()
tiles3()
tiles4()
tiles5()
tiles6()
tiles7()
numbers()
x()
print(board)


ending  = 0
brak = 1
tile = "h"

while ending == 0:
  print("you are the king's army")
  whatToMovex = int(input("Which peice would you like to move (x couardanate (left to right))"))
  whatToMovey = int(input("Which peice would you like to move (y couardanate (up and down))"))
  whereToMovex = int(input("Where would you like to move it (x couardanate)"))
  whereToMovey = int(input("Where would you like to move it (y couardanate)"))
  selectedpeice = board[whatToMovex][whatToMovey]
  if board[whereToMovex][whereToMovey] == u'🍩':
    print("The king's army won!")
    brak = 2
  board[whereToMovex][whereToMovey] = selectedpeice
  tile = tiles[whatToMovex][whatToMovey]
  board[whatToMovex][whatToMovey] = tile
  x()
  print(board)
  if brak == 2:
    break


  print("you are the fruit army")
  whatToMovex = int(input("Which peice would you like to move (x couardanate (left to right))"))
  whatToMovey = int(input("Which peice would you like to move (y couardanate (up and down))"))
  print("")
  whereToMovex = int(input("Where would you like to move it (x couardanate)"))
  whereToMovey = int(input("Where would you like to move it (y couardanate)"))
  print("")
  selectedpeice = board[whatToMovex][whatToMovey]
  if board[whereToMovex][whereToMovey] == u'👸':
    print("Fruit team won!")
    ending = 1
  board[whereToMovex][whereToMovey] = selectedpeice
  tile = tiles[whatToMovex][whatToMovey]
  board[whatToMovex][whatToMovey] = tile
  x()
  print(board)

  

  
