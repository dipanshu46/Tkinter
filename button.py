from tkinter import *

def hello():
    print("Hello tkinter buttons")

def name():
    print("Name is Dipanshu Singh")

def bye():
    print("Closing app")
    exit()

root = Tk()
root.geometry("655x333")

frame = Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame.pack(side=LEFT, anchor=NW)

# Creating buttons 
b1 = Button(frame, fg='red', text="Print now", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg='red', text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg='red', text="End now", command=bye)
b3.pack(side=LEFT, padx=23)

root.mainloop()