from tkinter import *

tk = Tk()
tk.title("Happy Bill Gates")
canvas = Canvas(tk, width=300, height=300)
canvas.pack()
f = PhotoImage(file='./res/f.gif')
s = PhotoImage(file='./res/s.gif')
canvas.create_image(0, 0, anchor=NW, image=f)

def dont_punch(event):
    canvas.create_image(0, 0, anchor=NW, image=f)
    tk.title("Happy Bill Gates :)")

def punch(event):
    canvas.create_image(0, 0, anchor=NW, image=s)
    tk.title("Sad Bill Gates :(")

canvas.bind_all('<Button-1>', punch)
canvas.bind_all('<Button-3>', dont_punch)




    
