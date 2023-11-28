import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import time
import sheeppy
from tkinter import *
import json
import requests
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")


def detailsview():
    def start_progress():
        progress['maximum'] = 100  # Set the maximum value of the progress bar
        for i in range(100):
            progress['value'] = i  # Update the progress bar value
            root.update()  # Refresh the window to show the updated progress bar
            time.sleep(0.01)  # Add a small delay to visualize the progress
        progress['value'] = 0  # Reset the progress bar value after completion
        root.destroy()


    root = tk.Tk()
    root.title("Package Details")
    menu_bar = tk.Menu(root)

    window_width = 500
    window_height = 400

    # Center the window on the screen
    center_window(root, window_width, window_height)

    # Set a modern color scheme
    bg_color = "#6495ED"  # Light gray background
    fg_color = "#333333"  # Dark text color
    accent_color = "#2962FF"  # Blue accent color

    root.configure(bg=bg_color)

    # Update label and entry styles
    label_font = ("Arial", 12)
    entry_font = ("Arial", 12)

    Label(root, text="From Postal Code", font=label_font, bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
    Label(root, text="To Postal Code", font=label_font, bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10,
                                                                                       pady=10)
    Label(root, text="*", bg=bg_color).grid(row=1, column=2)
    Label(root, text="To Street", font=label_font, bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=10)
    Label(root, text="*", bg=bg_color).grid(row=2, column=2)
    Label(root, text="To City Province", font=label_font, bg=bg_color, fg=fg_color).grid(row=3, column=0, padx=10,
                                                                                         pady=10)
    Label(root, text="*", bg=bg_color).grid(row=3, column=2)
    Label(root, text="To State Province", font=label_font, bg=bg_color, fg=fg_color).grid(row=4, column=0, padx=10,
                                                                                          pady=10)
    Label(root, text="*", bg=bg_color).grid(row=4, column=2)
    Label(root, text="Weight in pound", font=label_font, bg=bg_color, fg=fg_color).grid(row=5, column=0, padx=10,
                                                                                        pady=10)
    Label(root, text="Values with * are mandatory", font=label_font, bg=bg_color, fg=fg_color).grid(row=6, column=1,
                                                                                                    padx=10, pady=10)

    fromPs = Entry(root, font=entry_font)
    fromPs.grid(row=0, column=1, padx=10, pady=10)

    toPs = Entry(root, font=entry_font)
    toPs.grid(row=1, column=1, padx=10, pady=10)

    toCity = Entry(root, font=entry_font)
    toCity.grid(row=3, column=1, padx=10, pady=10)

    toStreet = Entry(root, font=entry_font)
    toStreet.grid(row=2, column=1, padx=10, pady=10)

    toState = ttk.Combobox(
        root,
        state="readonly",
        font=entry_font,
        values=[
            "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
            "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
            "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
        ],
    )
    toState.grid(row=4, column=1, padx=10, pady=10)

    wtE = Entry(root, font=entry_font)
    wtE.grid(row=5, column=1, padx=10, pady=10)

    progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
    progress.grid(row=9, column=1)

    button_style = ttk.Style()
    button_style.configure(
        "TButton",
        font=label_font,
        padding=6,
        relief="flat",
        background=accent_color,
        foreground="black",
    )

    def show_about():
            messagebox.showinfo(""," The application works using Ship engine API. \n \n"
                                "Helps the user to check different shipement rates across the USA with one click\n\n"
                                "Provides all the real time data")

    def show_contact_us():
        messagebox.showinfo("", "Project manager -- Likith Reddy Gurram\n"
                                    "GUI -- Venkata Sai Phaneendra\n"
                                    "Backend development -- Karthikeya Pappudippu\n"
                                    "Research and testing -- Sumanth Gunnaganti")

    def exit_application():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            root.destroy()

    # Create a menu bar
    menu_bar = tk.Menu(root)

    # Create a "File" menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=exit_application)

    # Create a "Help" menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=show_about)
    help_menu.add_command(label="Contact Us", command=show_contact_us)

    # Add the menus to the menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Help", menu=help_menu)



    def verify():
        url = "https://api.shipengine.com/v1/addresses/validate"

        payload = json.dumps([
            {
                "address_line1": toStreet.get(),
                "city_locality": toCity.get(),
                "state_province": toState.get(),
                "postal_code": toPs.get(),
                "country_code": "US"
            }])
        headers = {
            'Host': 'api.shipengine.com',
            'API-Key': 'TEST_YVrjR5qjiK1R94jQqsTjLj0P759U03vZJtFoRjtk3e4',
            'Content-Type': 'application/json'
        }

        cWt = int(wtE.get())
        if cWt>=70:
            messagebox.showinfo("", "Enter less than 70 pounds")
        else:

            print(wtE.get())
            print(type(wtE.get()))
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            res = json.loads(response.text)
            if res[0]["status"] == "verified":
                messagebox.showinfo(
                    "",
                    f"We matched it to this address\n\nStreet: {res[0]['matched_address']['address_line1']}\n"
                    f"City: {res[0]['matched_address']['city_locality']}\n"
                    f"State: {res[0]['matched_address']['state_province']}\n"
                    f"Postal code: {res[0]['matched_address']['postal_code']}"
                )
                input_variable = [
                    [fromPs.get()], [res[0]['matched_address']['postal_code']],
                    [res[0]['matched_address']['address_line1']], [res[0]['matched_address']['city_locality']],
                    [res[0]['matched_address']['state_province']], wtE.get()
                ]
                # Example.csv gets created in the current working directory
                with open('userInputData.csv', 'w', newline='') as csvfile:
                    my_writer = csv.writer(csvfile, delimiter=' ')
                    my_writer.writerows(input_variable)
                start_progress()
                sheeppy.process()
            else:
                messagebox.showinfo("", "Enter the correct Address")

    ttk.Button(root, text="Submit", style="TButton", command=verify).grid(row=7, columnspan=2, padx=10, pady=10)
    root.config(menu=menu_bar)
    root.mainloop()




