from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import detailsPage
from tkinter import ttk

def verify():
  uname = e1.get()
  password = e2.get()

  if (uname == "" and password == ""):
    messagebox.showinfo("", "Blank Not allowed")
  elif (uname == "Admin" and password == "123"):
    messagebox.showinfo("", "Login Success")
    root.destroy()
    detailsPage.overview()
  else:
    messagebox.showinfo("", "Incorrent Username and Password")

root = Tk()
root.title("Login")
root.geometry("400x250") # set the initial size of the window

# center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (400/2)) # center horizontally
y = int((screen_height/2) - (250/2)) # center vertically
root.geometry(f"400x250+{x}+{y}")

# create a style for the ttk widgets
style = ttk.Style()
style.theme_use('default')

adminimage = ImageTk.PhotoImage(Image.open('delivery.png'))

Label(root, text="UserName").grid(row=0, column=0, padx=10, pady=10)
Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)

e1 = ttk.Entry(root)
e1.grid(row=0, column=1)

e2 = ttk.Entry(root, show="*")
e2.grid(row=1, column=1)
e2.config(show="*")

# create a ttk button
ttk.Button(root, text="Login", command=verify).grid(row=2, column=1, pady=10)

root.mainloop()
