'''
Q: Create an application to take username and password from user and save it in your program itself (temporary storage) when submit button is clikced and make sure the entry gets cleaned for new user entry. Also display the added user's when clicked on another button called users. 
'''

from tkinter import *

user_info = {}

def getVals():
    # get() method gets the value of the variable.
    key = userValue.get()
    val = passValue.get()

    user_info.update({key:val})
    print("\nUser succesfully added")

    # set() method sets the value of the variable.
    userValue.set('')
    passValue.set('')

def dispUsers():
    for key in user_info:
        print(f"\nUsername: {key}\nPassword: {user_info[key]}")

# Creating our app
root = Tk()
root.geometry("633x555")

# Creating Labels for username and Password and using grid to place them
user = Label(root, text='Username')
password = Label(root, text='Password')
# grid() works on row, column principle and does the same thing as for packing.
user.grid(row=0, column=0)
password.grid(row=1, column=0)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

# Creating variables for our username entry and password entry by the user
userValue = StringVar()
passValue = StringVar()

# Using Entry() to take input from user for username and password
userEntry = Entry(root, textvariable=userValue)
passEntry = Entry(root, textvariable=passValue)
userEntry.grid(row=0,column=1)
passEntry.grid(row=1, column=1)

Button(text="Submit", command=getVals).grid(row=2, column=0)
Button(text="Users", command=dispUsers).grid(row=4, column=0)

# Starting our app
root.mainloop()