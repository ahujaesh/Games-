import tkinter as tk
import os
import sys

def fruit():
    os.system('python SnakeGame.py')
def ttt():
    os.system('python Tic_Tac_toe.py')
def ch():
    os.system('python chess.py')
def boom():
    os.system('python Minesweeper.py')
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Open Fruit catcher!",
                   command=fruit)
button2 = tk.Button(frame,
                   text="Open Tic Tac Toe!",
                   command=ttt)
button3 = tk.Button(frame,
                   text="Open Chess!",
                   command=ch)
button4 = tk.Button(frame,
                   text="Open Minesweeper!",
                   command=boom)
slogan.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
root.mainloop()

