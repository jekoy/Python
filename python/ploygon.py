import time
from tkinter import *
tk=Tk()
tk.title("Game")
canvas=Canvas(tk,width=400,height=200)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
for i in range(0,60):
    canvas.move(1,5,0)
    tk.update()
    time.sleep(1)
