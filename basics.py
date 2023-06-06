from tkinter import *

# Creating app
app = Tk()

# Setting height and width of the app on opening.

# Width x Height
app.geometry('900x800')

# Minimum size allowed to the app window
# Width, Height
app.minsize(300,200)

# Maximum size allowed to the app window
# Width, Height
app.maxsize(1000,800)

# Adding text to GUI
# We first need to create a label that contains text.
name = Label(text="My name Dipanshu Singh and this is my GUI")
# Then we need to pack it into our gui using pack()
name.pack()

# Starting the app
app.mainloop()