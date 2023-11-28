from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import registerUser
import  detailsPage

def overview():
    root = Tk()

    def login():
        name = e1.get()
        pwd = e2.get()
        if name == "" or pwd == "":
            messagebox.showwarning("", "Enter the username and password to proceed")
        else:
            connection = mysql.connector.connect(
                host='localhost',
                database='unames_list',
                user='admin',
                password='password'
            )

            sql_select_Query = "SELECT * FROM usernames WHERE username = %s AND password = %s"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query, [(name), (pwd)])
            # get all records
            records = cursor.fetchall()
            if records:
                for i in records:
                    messagebox.showinfo("", "Login Successful")
                    root.destroy()

                    detailsPage.detailsview()
            else:
                messagebox.showerror("", "Login Failed\nTry again")

    def reg():
        root.destroy()
        from registerUser import registerview
        registerUser.registerview()

    # Set a modern color scheme
    bg_color = "#16B2DF"  # Light gray background
    fg_color = "#333333"  # Dark text color
    accent_color = "#2962FF"  # Blue accent color

    root.title("Delivery estimator")
    root.geometry("350x540")
    root.configure(bg=bg_color)
    root.eval('tk::PlaceWindow . center')

    # Update label and entry styles
    label_font = ("Arial", 12)
    entry_font = ("Arial", 12)

    Label(root, text="Username", font=label_font, bg=bg_color, fg=fg_color).grid(
        row=0, column=0, padx=10, pady=10
    )
    Label(root, text="Password", font=label_font, bg=bg_color, fg=fg_color).grid(
        row=1, column=0, padx=10, pady=10
    )

    logo = ImageTk.PhotoImage(Image.open('delivery.png'))

    e1 = Entry(root, font=entry_font)
    e1.grid(row=0, column=1, padx=10, pady=10)

    e2 = Entry(root, font=entry_font)
    e2.grid(row=1, column=1, padx=10, pady=10)
    e2.config(show="*")

    # Use a modern button style
    button_style = ttk.Style()
    button_style.configure(
        "TButton",
        font=label_font,
        padding=6,
        relief="flat",
        background=accent_color,
        foreground="black",
    )

    ttk.Button(root, text="Login", style="TButton", command=login).grid(
        row=2, column=1, padx=10, pady=10
    )
    ttk.Button(root, text="Register", style="TButton", command=reg).grid(
        row=3, column=1, padx=10, pady=10
    )
    ttk.Button(root, text="Quit", style="TButton", command=root.quit).grid(
        row=4, column=1, padx=10, pady=10
    )

    Label(root, image=logo, bg=bg_color).grid(row=5, column=1, padx=10, pady=10)

    root.mainloop()


overview()
