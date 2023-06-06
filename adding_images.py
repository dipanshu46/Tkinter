from tkinter import *

# Creating a window
app = Tk()
app.geometry("700x700")

# For adding images

# creating image object
photo1 = PhotoImage(file="../../../Personal/Dipanshu_Passport_size-removebg-preview.png")
# adding image object to the gui using label
photo1_label = Label(image=photo1)
photo1_label.pack()

# NOTE: tkinter PhotoImage accepts only png images, to use jpg images we need to install pillow module using pip and import Image and ImageTk from PIL
from PIL import Image, ImageTk

# To open Jpg images...
# Opening image
image = Image.open("../../../Personal/Dipanshu.jpeg")
photo2 = ImageTk.PhotoImage(image)
# adding image object to the gui using label
photo2_label = Label(image=photo2)
photo2_label.pack()

# Starting the window
app.mainloop()