from colored_print import ColoredPrint

log = ColoredPrint()
import random
import time
import numpy as np

log.info("Welcome to Minesweeper!")
log.success("it is currently " + (time.ctime()))
log.info("In this game, you are trying to search the board for mines.")
log.info("You can chose how many mines there are.")
log.info("After that, you can type in the X and Y coordinates to start.")
log.info("After you enter it in, the system will tell you if you hit a mine or not.")
log.info("If you didn't hit a mine, it wil give you a number on the 10 X 10 grid.")
log.info("This number represents if there are mines nearby.")
log.info("If it is 0, then there is no mines close by.")
log.info("If it is 1 or more, the number represents the ammount of mines near you. Watch out!")
log.info("To win, place flags on all the mines.")
print("")
log.pink("Ready?")
print("")
log.pink("Set!")
print("")
log.pink("Go!")
 
rows, columms = (10,10)
board = np.chararray((10,10),unicode = True)
board[:] = '-'
board2 = np.chararray((10,10),unicode = True)
board2[:] = '-'

print("")
print("How many mines do you want there to be?")
mines = int(input())
minesList = []






#picking random spaces to be mines
def location4():
  location3 = []

  location1 = random.randint(0,9)

  location2 = random.randint(0,9)

  location3.append(location1)
  location3.append(location2)
  return location3


while mines > 0:
  storage = location4()
  if storage in minesList:
    pass
  else:
   mines = mines - 1
   minesList.append(storage)


loop = 0

def minetest():
  for i in range (len(minesList)):
    x = minesList[i][0] 
    y = minesList[i][1]
    board [x][y] = "💣"
    userrowtest = x + 1
    userrowtest2 = x - 1
    usercoltest = y + 1
    usercoltest2 = y - 1
    if userrowtest > -1 and userrowtest < 10:
      if board[userrowtest][y] != '💣':
        if board[userrowtest][y] != '-':
          board[userrowtest][y] = str(int(board[userrowtest][y])+1)
        else:
         board[userrowtest][y] = '1'
    if userrowtest2 > -1 and userrowtest2 < 10:
      if board[userrowtest2][y] != '💣':
        if board[userrowtest2][y] != '-':
          board[userrowtest2][y] = str(int(board[userrowtest2][y])+1)
        else:
         board[userrowtest2][y] = '1'
    if usercoltest > -1 and usercoltest < 10:
      if board[x][usercoltest] != '💣':
        if board[x][usercoltest] != '-':
          board[x][usercoltest] = str(int(board[x][usercoltest])+1)
        else:
         board[x][usercoltest] = '1'
    if usercoltest2 > -1 and usercoltest2 < 10:
      if board[x][usercoltest2] != '💣':
        if board[x][usercoltest2] != '-':
          board[x][usercoltest2] = str(int(board[x][usercoltest2])+1)
        else:
         board[x][usercoltest2] = '1'

    #diagonals

    if userrowtest2 > -1 and userrowtest2 < 10:
      if usercoltest2 > -1 and usercoltest2 < 10:
        if board[userrowtest2][usercoltest2] != '💣':
          if board[userrowtest2][usercoltest2] != '-':
            board[userrowtest2][usercoltest2] = str(int(board[userrowtest2][usercoltest2])+1)
          else:
            board[userrowtest2][usercoltest2] = '1'
    if userrowtest > -1 and userrowtest < 10:
      if usercoltest > -1 and usercoltest < 10:
        if board[userrowtest][usercoltest] != '💣':
          if board[userrowtest][usercoltest] != '-':
            board[userrowtest][usercoltest] = str(int(board[userrowtest][usercoltest])+1)
          else:
            board[userrowtest][usercoltest] = '1'
    if userrowtest2 > -1 and userrowtest2 < 10:
      if usercoltest > -1 and usercoltest < 10:
        if board[userrowtest2][usercoltest] != '💣':
          if board[userrowtest2][usercoltest] != '-':
            board[userrowtest2][usercoltest] = str(int(board[userrowtest2][usercoltest])+1)
          else:
           board[userrowtest2][usercoltest] = '1'
    if userrowtest > -1 and userrowtest < 10:
      if usercoltest2 > -1 and usercoltest2 < 10:
        if board[userrowtest][usercoltest2] != '💣':
          if board[userrowtest][usercoltest2] != '-':
            board[userrowtest][usercoltest2] = str(int(board[userrowtest][usercoltest2])+1)
          else:
           board[userrowtest][usercoltest2] = '1'




minetest()

usercolumn = 1
flagcount = len(minesList) + 3
minecount = len(minesList)
while True:
  print ("Would you like to place a flag? (1 = yes 2 = no)")
  YN = int(input())

  if(YN == 1):
    flagcount = flagcount - 1
    if (flagcount > 0):
     print("What row would you like to go to?")
     while True:
        try:
          a = int(input()) - 1
          break
        except:
         print("This number is invalid. Please enter new coordinates.")

     print("What column would you like to go to?")
     while True:
        try:
          b = int(input()) - 1
          break
        except:
          print("This number is invalid. Please enter new coordinates.")
     if board[a][b] == '💣':
       minecount = minecount - 1
     if (minecount < 1):
       log.success("You win!🏆")
       print(board)
     board[a][b] = '⚐'
     board2[a][b] = '⚐'
     print(board2)
    else:
      print("you have run out of flags :(")
  else:
   print("What row would you like to go to?")
   while True:
     try:
       userrow = int(input()) - 1
       break
     except:
       print("This number is invalid. Please enter new coordinates.")

   print("What column would you like to go to?")
   while True:
     try:
       usercolumn = int(input()) - 1
       break
     except:
        print("This number is invalid. Please enter new coordinates.")

   if (board[userrow][usercolumn] == '💣'):
     print("You hit a mine. :( This is where the mines were. ")
     print(board)
     time.sleep(60)
     break
   else:
    print("You didn't hit a mine.")
    board2[userrow][usercolumn] = 'O'
    if board[userrow][usercolumn] != '-':
      board2[userrow][usercolumn] = board[userrow][usercolumn]
      print(board2)
    else:
      print(board2)
