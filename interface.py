import tkinter as tk
import os
import sys

def fruit():
    os.system('python SnakeGame.py')
def ttt():
    print("h")
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
                   text="Open Fruit catcher!",
                   command=ttt)
slogan.pack(side=tk.LEFT)

root.mainloop()
