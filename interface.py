import tkinter as tk
import os
import sys

def fruit():
    os.system('python SnakeGame.py')
def ttt():
    os.system('python Tic_Tac_Toe.py')
def ch():
    os.system('python chess')
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
slogan2 = tk.Button(frame,
                   text="Open Tic Tac Toe!",
                   command=ttt)
slogan3 = tk.Button(frame,
                   text="Open Chess!",
                   command=ch)
slogan.pack(side=tk.LEFT)

root.mainloop()
