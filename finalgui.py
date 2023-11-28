import tkinter as tk
from tkinter import ttk
import json

import detailsPage
import finaltest


def display_rates(rates):
    def summary():

        from finaltest import summarize
        finaltest.summarize()

    def detback():
        from detailsPage import detailsview
        detailsPage.detailsview()

    root = tk.Tk()
    root.title("Shipping Rates")

    tab_control = ttk.Notebook(root)
    fedex_tab = ttk.Frame(tab_control)
    ups_tab = ttk.Frame(tab_control)
    usps_tab = ttk.Frame(tab_control)
    summary_tab = ttk.Frame(tab_control)

    tab_control.add(fedex_tab, text="FedEx")
    tab_control.add(ups_tab, text="UPS")
    tab_control.add(usps_tab, text="USPS")
    tabs = [fedex_tab, ups_tab, usps_tab]

    for tab in tabs:
        tree = ttk.Treeview(tab)
        tree["columns"] = ("package_type", "service_type", "shipping_amount", "delivery_days", "estimated_delivery")
        tree.heading("#0", text="Carrier")
        tree.column("#0", anchor="w", width=150)
        tree.heading("package_type", text="Package Type")
        tree.column("package_type", anchor="center", width=120)
        tree.heading("service_type", text="Service Type")
        tree.column("service_type", anchor="center", width=150)
        tree.heading("shipping_amount", text="Shipping Amount (USD)")
        tree.column("shipping_amount", anchor="center", width=150)
        tree.heading("delivery_days", text="Delivery Days")
        tree.column("delivery_days", anchor="center", width=120)
        tree.heading("estimated_delivery", text ="Estimated Delivery Date ")
        tree.column("estimated_delivery", anchor="center", width=180)
        tree.pack(padx=10, pady=10)

    best_price = float("inf")
    fastest_delivery = float("inf")

    for rate in rates:
        package_type = rate["package_type"]
        service_type = rate["service_type"]
        shipping_amount = rate["shipping_amount"]["amount"]
        delivery_days = rate["delivery_days"]
        estimated_delivery = rate["estimated_delivery_date"]
        carrier_code = rate["carrier_code"]
        if carrier_code == "fedex":
            tab = fedex_tab
        elif carrier_code == "ups":
            tab = ups_tab
        elif carrier_code == "usps":
            tab = usps_tab

        else:
           continue

        tree = tab.winfo_children()[0]
        tree.insert("", tk.END, text=service_type, values=(package_type, service_type, shipping_amount, delivery_days, estimated_delivery))

   # tree = summary_tab.winfo_children()[0]
    tab_control.pack(padx=10, pady=10)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy)
    exit_button.pack(side="right", padx=5)


    back_button = ttk.Button(button_frame, text="Back", command=detback)
    back_button.pack(side="left", padx=5)

    summary_button = ttk.Button(button_frame, text="Summary View", command = summary)
    summary_button.pack(side="left", pady=7)
    root.mainloop()

def  drill():
    with open('sample.json') as openfile:
        dump = json.load(openfile)
    display_rates(dump)
