import tkinter as tk
import csv
from tkinter import ttk
import json
from datetime import datetime, timedelta
import finalgui

def summarize():
    with open('sample.json') as openfile:
        # Reading from json file
        dump = json.load(openfile)

    filename = "summary.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()

    # Define the header of the CSV file
    header = ["carrier Id", "Price", "Type of Service", "Delivery Days", "Delivery Time", "Time Elapsed"]

    with open('summary.csv', 'a', newline='') as csvfile:
        my_writer = csv.writer(csvfile)
        my_writer.writerow(header)  # Write the header row to the CSV file

        for i in range(28):
            id = dump[i]["carrier_id"]
            price = dump[i]["shipping_amount"]["amount"]
            service_type = dump[i]["service_type"]
            delivery_days = dump[i]["delivery_days"]
            estimated_delivery = dump[i]["estimated_delivery_date"]
            if estimated_delivery is None:
                continue

            timestamp_obj = datetime.fromisoformat(estimated_delivery[:-1])
            present_time = datetime.now()
            time_difference = timestamp_obj - present_time
            delta_difference = str(time_difference)

            # Create a row with the data for each iteration
            row = [id, price, service_type, delivery_days, estimated_delivery, delta_difference]

            my_writer.writerow(row)  # Write the row to the CSV file

    view()

def view():
    # Read the CSV file and store the data in a list of dictionaries
    data = []
    with open('summary.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Create dictionaries to store the fastest and cheapest options for each carrier
    fastest_options = {}
    cheapest_options = {}

    # Iterate over the data and find the fastest and cheapest options for each carrier
    for row in data:
        carrier_id = row['carrier Id']
        delivery_days = int(row['Delivery Days'])
        price = float(row['Price'])
        service_type = row['Type of Service']
        delta_difference_str = row['Time Elapsed']

        # Split the Time Elapsed into days, hours, and minutes
        if ' days, ' in delta_difference_str:
            days, time = delta_difference_str.split(' days, ')
        else:
            days = '0'
            time = delta_difference_str
        hours, minutes, _ = time.split(':')

        # Format the Time Elapsed string
        if days == '0':
            delta_difference = f"{hours} hours, {minutes} minutes"
        elif days == '1':
            delta_difference = f"{days} day, {hours} hours, {minutes} minutes"
        else:
            delta_difference = f"{days} days, {hours} hours, {minutes} minutes"

        # Check if the carrier is already in the dictionaries
        if carrier_id not in fastest_options:
            fastest_options[carrier_id] = {'Delivery Days': delivery_days, 'Type of Service': service_type, 'Price': price, 'Time Elapsed': f"{days} days, {hours} hours, {minutes} minutes"}
        elif delivery_days < fastest_options[carrier_id]['Delivery Days']:
            fastest_options[carrier_id] = {'Delivery Days': delivery_days, 'Type of Service': service_type, 'Price': price, 'Time Elapsed': f"{days} days, {hours} hours, {minutes} minutes"}

        if carrier_id not in cheapest_options:
            cheapest_options[carrier_id] = {'Price': price, 'Type of Service': service_type, 'Time Elapsed': f"{days} days, {hours} hours, {minutes} minutes"}
        elif price < cheapest_options[carrier_id]['Price']:
            cheapest_options[carrier_id] = {'Price': price, 'Type of Service': service_type, 'Time Elapsed': f"{days} days, {hours} hours, {minutes} minutes"}

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Fastest and Cheapest Options")
    window.geometry("800x600")

    # Create two frames for the layouts
    frame1 = ttk.Frame(window, width=400)
    frame1.pack(side="top", padx=10, pady=10, fill="both")
    frame2 = ttk.Frame(window, width=400)
    frame2.pack(side="top", padx=10, pady=10, fill = "both")

    # Create the treeview for displaying fastest options
    tree1 = ttk.Treeview(frame1, columns=("Price", "Delivery Days", "Type of Service", "Time Elapsed"), show="headings")
    tree1.heading("Price", text="Price",anchor='center')
    tree1.heading("Delivery Days", text="Delivery Days",anchor='center')
    tree1.heading("Type of Service", text="Type of Service",anchor='center')
    tree1.heading("Time Elapsed", text="Time Elapsed",anchor='center')
    tree1.pack(side="left", fill="both", expand="true",anchor='center')

    # Insert fastest options into the treeview
    for carrier_id, option in fastest_options.items():
        tree1.insert("", "end", values=(option["Price"], option["Delivery Days"], option["Type of Service"], option["Time Elapsed"]))

    # Create the treeview for displaying cheapest options
    tree2 = ttk.Treeview(frame2, columns=( "Price", "Type of Service", "Time Elapsed"), show="headings")
    tree2.heading("Price", text="Price", anchor='center')
    tree2.heading("Type of Service", text="Type of Service",anchor='center')
    tree2.heading("Time Elapsed", text="Time Elapsed",anchor='center')
    tree2.pack(side="left", fill="both", expand="true")

    # Insert cheapest options into the treeview
    for carrier_id, option in cheapest_options.items():
        tree2.insert("", "end", values=( option["Price"], option["Type of Service"], option["Time Elapsed"]))

    exit_button = ttk.Button(window, text="Exit", command=window.destroy)
    exit_button.pack(side="bottom", expand="true")
    # Start the Tkinter event loop
    window.mainloop()



