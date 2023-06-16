'''
Q: Create 4 buttons, horizontally stacked and each performing some different printing.
'''

from tkinter import *
import os

def greet(name):
    os.system('clear')
    print(name,"is pressed.")

root = Tk()
root.geometry("655x333")

frame = Frame(root, bg='grey', relief=RIDGE)
frame.pack(side=BOTTOM, fill=X)

b1 = Button(frame, fg='red', text="Button1", command= lambda: greet("Button 1"))
b1.pack(padx=23)

b2 = Button(frame, fg='red', text="Button2", command=lambda: greet("Button 2"))
b2.pack(padx=23)

b3 = Button(frame, fg='red', text="Button3", command=lambda: greet("Button 3"))
b3.pack(padx=23)

b4 = Button(frame, fg='red', text="Button4", command=lambda: greet("Button 4"))
b4.pack(padx=23)

root.mainloop()