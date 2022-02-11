# Udemy Python Bootcamp
#tkinker on Canvas
from struct import pack
import tkinter
from tkinter import *
from typing import Any

win = Tk()

c = Canvas(win, height=1250, width=1300, bg='blue') # Note - the Canvas needs to be Capital 'C'
coord=0,0,1250,1300
# Creating Arc in Canvas
arc = c.create_arc(coord,start=0,extent=150, fill='red')  # start is the angle and extent is the degree of turn

# Creating Line in Canvas
line = c.create_line(10,10,200,200, fill='white')

# Creating Oval in Canvas
oval=c.create_oval(0,0,100,100,fill='green') # x0,y0, x1,y1, options

# Creating Polygen in Canvas - some issue, need to research more
polygen=c.create_polygon(900,30,12,12,24,24,36,36,48,48,60,60, fill='yellow')

# Attaching image in Canvas
filename = PhotoImage(file="SimpleSpiralPatterns.png")
image=c.create_image(630,30, anchor=NE, image=filename)



c.pack()
win.mainloop()
