import tkinter as tk
import tkinter.messagebox as messagebox  # Import for error messages

root = tk.Tk()
root.geometry("500x300")


def validate_input():
  username = usernameentry.get()  # Get value from username entry
  password = passwordentry.get()  # Get value from password entry
  if username == "" or password == "":
    messagebox.showerror("Error", "Please fill in all fields.")
    return False
  return True


def getvals():
  if validate_input():
    print("Accepted")


# Heading
label = tk.Label(root, text="Career App Login", font="arial 15 bold")
label.grid(row=0, column=3)

# Field name
username = tk.Label(root, text="Username")
username.grid(row=1, column=2)
password = tk.Label(root, text="Password")
password.grid(row=2, column=2)

# Variable for storing data
usernamevalue = tk.StringVar()
passwordvalue = tk.StringVar()

checkvalue = tk.IntVar()

# Creating entry field
usernameentry = tk.Entry(root, textvariable=usernamevalue)
passwordentry = tk.Entry(root, textvariable=passwordvalue)

# Packing entry fields
usernameentry.grid(row=1, column=3)
passwordentry.grid(row=2, column=3)

# Creating checkbox
checkbtn = tk.Checkbutton(text="Remember me?", variable=checkvalue)
checkbtn.grid(row=3, column=3)

# Submit button
tk.Button(text="Submit", command=getvals).grid(row=4, column=3)

root.mainloop()
