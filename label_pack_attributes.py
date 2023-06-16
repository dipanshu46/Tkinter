from tkinter import *

root = Tk()
root.geometry("444x233")
# To add a title on your gui
root.title("My GUI with Harry")

# Label attributes
# text - adds the text  - string text
# bd - background   - string colour
# fg - foreground   - string colour
# font - sets the font  - string with space seperated values: fontstyle fontsize italic bold / tuple (fontstyle, fontsize)
# padx - x padding  - int x padding
# pady - y padding  - int y padding
# relief - border styling - FLAT, SUNKEN, RAISED, GROOVE, RIDGE

label1 = Label(text="This is a text label", bg="red", fg="white", padx=30, pady=50, font="Arial 15", borderwidth=6, relief=RIDGE)

# Pack Attrbutes
# anhcor - sets the positional direction of the content according to the side - string text - n,e,w,s,ne,nw,se,sw
# side - sets the position of the item - top, bottom, left, right
# fill - stretches the content to fill the mentioned direction fully -  X, Y
# padx - x padding - int x padding
# pady - Y padding - int y padding

label1.pack(anchor="nw", side=TOP, fill=X, padx=40, pady=40)

root.mainloop()