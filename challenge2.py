from tkinter import *

root = Tk()

root.geometry("500x400")
root.minsize(500,400)
root.maxsize(500,400)

ready = Label(text="READY", bg="green", fg="white", font="Arial 15 bold", padx=30, pady=30, borderwidth=5, relief=GROOVE)
ready.pack(side=BOTTOM, padx=20, pady=20, fill=X)

root.mainloop()