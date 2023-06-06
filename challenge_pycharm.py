# Q: WAP to create a window of 733x435 containing a Welcome to PyCharm! text in it.

from tkinter import *

app = Tk()

app.geometry("733x435")
app.minsize(733,435)
app.maxsize(733,435)

PyCharm = Label(text="Welcome to PyCharm!")
PyCharm.pack()

app.mainloop()