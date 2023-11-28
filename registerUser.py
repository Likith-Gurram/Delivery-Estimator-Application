from tkinter import *
from tkinter import messagebox
import mysql.connector
def registerview():
    root = Tk()
    def backMain():
        root.destroy()
        import newlogingui

    def createDbData():
        uname = e1.get()
        password = e2.get()

        if (uname == "" and password == ""):
            messagebox.showinfo("", "Blank Not allowed")
        else:
            dataBase = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Account@09",
                database="unames_list"
            )

            # preparing a cursor object
            cursorObject = dataBase.cursor()

            sql = "INSERT INTO USERNAMES (USERNAME, PASSWORD)\
            VALUES (%s, %s)"
            val = (uname, password)

            cursorObject.execute(sql, val)
            dataBase.commit()

            # disconnecting from server
            dataBase.close()
            messagebox.showinfo("", "User Added")

    root.title("Register")
    Label(root, text="UserName").grid(row=0, column=0, padx=10, pady=10)
    Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
    bg_color = "#16B2DF"  # Light gray background
    fg_color = "#333333"  # Dark text color
    accent_color = "#2962FF"  # Blue accent color

    global e1, e2
    e1 = Entry(root)
    e1.grid(row=0, column=1)

    e2 = Entry(root, show="*")
    e2.grid(row=1, column=1)
    e2.config(show="*")

    Button(root, text="Create", command=createDbData).grid(row=2, column=1, padx=10, pady=10)
    Button(root, text="Back to main menu", command=backMain).grid(row=3, column=1, padx=10, pady=10)
    root.mainloop()
