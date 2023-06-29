from tkinter import *

def submit():
    print("\nSubmitting form...")
    
    with open("records.txt", 'a') as f:
        f.write(f"{name_val.get(),phone_val.get(),gender_val.get(),emergency_val.get(),payment_mode_val.get(),food_service_val.get()}\n")
    
    name_val.set('')
    phone_val.set('')
    gender_val.set('')
    emergency_val.set('')
    payment_mode_val.set('')
    food_service_val.set(0)

    print("\nTravel details submitted!")

root = Tk()
root.geometry("633x555")

# Heading
Label(root, text="Welcome To Tipotripy!", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

# Creating labels for details of user
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
payment_mode = Label(root, text="Payment Mode")
food_service = Label(root, text="Want to pre-book your meal?")

# Placing the labels using grid
name.grid(row=1 ,column=2)
phone.grid(row=2 ,column=2)
gender.grid(row=3 ,column=2)
emergency.grid(row=4 ,column=2)
payment_mode.grid(row=5 ,column=2)
food_service.grid(row=6, column=2)

# Creating variables for user deatils
name_val = StringVar()
phone_val = StringVar()
gender_val = StringVar()
emergency_val = StringVar()
payment_mode_val = StringVar()
food_service_val = IntVar()

# Creating Entries for variables
name_entry = Entry(root, textvariable=name_val)
phone_entry = Entry(root, textvariable=phone_val)
gender_entry = Entry(root, textvariable=gender_val)
emergency_entry = Entry(root, textvariable=emergency_val)
payment_mode_entry = Entry(root, textvariable=payment_mode_val)

# Placing the entries using grid
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payment_mode_entry.grid(row=5, column=3)

# Checkbox
food_service_check = Checkbutton(text="Yes", variable=food_service_val)
food_service_check.grid(row=6, column=3)

# Button
Button(text="Submit", command=submit).grid(row=7, column=3)

root.mainloop()