import numpy as np

board = np.chararray((5,5),unicode = True)

print("Ultra tic tac toe!")
print("Some rules/things you can do: \n -all the rules of tic-tac-toe but - \n -you can take over other people's squares \n -you can go anyware \n \n and much much more to explore! \n \n \n ")

board[1][0] = "_"
board[1][1] = "_"
board[1][2] = "_"
board[1][3] = "_"
board[1][4] = "_"

board[3][0] = "_"
board[3][1] = "_"
board[3][2] = "_"
board[3][3] = "_"
board[3][4] = "_"

board[0][3] = "|"
board[1][3] = "|"
board[2][3] = "|"
board[3][3] = "|"
board[4][3] = "|"

board[0][1] = "|"
board[1][1] = "|"
board[2][1] = "|"
board[3][1] = "|"
board[4][1] = "|"

board[0][0] = "B"
board[2][0] = "B"
board[4][0] = "B"

board[0][2] = "B"
board[0][4] = "B"

board[2][2] = "B"
board[2][4] = "B"

board[4][2] = "B"
board[4][4] = "B"


print(board)

loop = 0
while loop == 0:
  xinput = input("You are player X. Where would you like to go? (y - cooordanates)")
  yinput = input("You are player X. Where would you like to go? (x - cooordanates)")
  board[int(xinput)][int(yinput)] = "X"
  print(board)
  if board[0][0] == "X" :
    if board[2][2] == "X":
      if board[4][4] == "X":
        loop = 1
        print("X won!")
        break
  if board[0][0] == "X" :
    if board[2][0] == "X":
      if board[4][0] == "X":
        loop = 1
        print("X won!")
        break
  if board[1][2] == "X" :
    if board[2][2] == "X":
      if board[3][2] == "X":
        loop = 1
        print("X won!")
        break
  if board[4][0] == "X" :
    if board[4][2] == "X":
      if board[4][4] == "X":
        loop = 1
        print("X won!")
        break
  if board[2][0] == "X" :
    if board[2][2] == "X":
      if board[2][4] == "X":
        loop = 1
        print("X won!")
        break
  if board[0][4] == "X" :
    if board[2][2] == "X":
      if board[4][0] == "X":
        loop = 1
        print("X won!")
        break
  if board[0][0] == "X" :
    if board[2][0] == "X":
      if board[4][0] == "X":
        loop = 1
        print("X won!")
        break
  if board[0][4] == "X" :
    if board[2][4] == "X":
      if board[4][4] == "X":
        loop = 1
        print("X won!")
        break  


  xinput = input("You are player Y. Where would you like to go? (y - cooordanates)")
  yinput = input("You are player Y. Where would you like to go? (x - cooordanates)")
  board[int(xinput)][int(yinput)] = "Y"
  print(board)
  if board[0][0] == "Y" :
    if board[2][2] == "Y":
      if board[4][4] == "Y":
        loop = 1
        print("Y won!")
        break
  if board[0][0] == "Y" :
    if board[2][0] == "Y":
      if board[4][0] == "Y":
        loop = 1
        print("Y won!")
        break
  if board[1][2] == "Y" :
    if board[2][2] == "Y":
      if board[3][2] == "Y":
        loop = 1
        print("Y won!")
        break
  if board[4][0] == "Y" :
    if board[4][2] == "Y":
      if board[4][4] == "Y":
        loop = 1
        print("Y won!")
        break
  if board[2][0] == "Y" :
    if board[2][2] == "Y":
      if board[2][4] == "Y":
        loop = 1
        print("Y won!")
        break
  if board[0][4] == "Y" :
    if board[2][2] == "Y":
      if board[4][0] == "Y":
        loop = 1
        print("Y won!")
        break
  if board[0][0] == "Y" :
    if board[2][0] == "Y":
      if board[4][0] == "Y":
        loop = 1
        print("Y won!")
        break
  if board[0][4] == "Y" :
    if board[2][4] == "Y":
      if board[4][4] == "Y":
        loop = 1
        print("Y won!")
        break  
