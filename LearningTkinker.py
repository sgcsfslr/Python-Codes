# Udemy Python Bootcamp
#tkinker
from struct import pack
import tkinter
from tkinter import *


def pr():
    print('Button Action command of pr')


win = Tk()
win.geometry("400x400")
b = Button(win , text = 'button', command=pr, padx=10, pady=10, activeforeground='red') # The command will trigger the function "pr" , padx and pady create the size of the button
#b.pack()  # This will set the button above button 2
#b.grid(row=2, column=1) # This will set the button to appear at row 2, column 1
b.place(x=100,y=200) # This will set the button in a very specific location
b2 = Button(win , text = 'button 2')
#b2.pack() # This will set the button below button 1
#b2.grid(row=1, column=1) # This will set the button to appear at row 1, column 1
b2.place(x=200,y=300) # This will set the button in a very specific location




win.mainloop()

