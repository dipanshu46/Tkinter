# Frames are just like div's in web development. They are used to break our screen into smaller segments.
from tkinter import *

root = Tk()

root.geometry("655x333")

# Creating a frame
f2 = Frame(root, bg="grey", borderwidth=1, relief=GROOVE)
f2.pack(side=TOP, fill="x")

f3 = Frame(root, bg="grey", borderwidth=1, relief=GROOVE)
f3.pack(side=TOP, fill="x")

f1 = Frame(root, bg="grey", borderwidth=1, relief=GROOVE)
f1.pack(side=LEFT, fill="y")

l1 = Label(f1, text="EXPLORER", bg="grey", fg="white", font="Arial 10")
l1.pack(pady=20)

l2 = Label(f2, text="frame.py - Tkinter - Visual Studio Code", bg="grey", fg="white", font="Ubuntu 11 bold")
l2.pack(pady=10)

l3 = Label(f3, text="File  Edit  Selection  View  Go  Run  Terminal  Help", bg="grey", fg="white", font="Ubuntu 11")
l3.pack(padx=5, anchor=W)

root.mainloop()