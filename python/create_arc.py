from tkinter import *
tk=Tk()
tk.title("Game")
tk.resizable=(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_arc(10,10,200,200,extent=180,style=ARC)
