import json
from datetime import datetime, timedelta
import csv

with open('sample.json') as openfile:
    # Reading from json file
    dump = json.load(openfile)


filename = "summary.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()

# Define the header of the CSV file
header = ["carrier Id","Price", "Type of Service", "Delivery Days", "Delivery Time", "Delta Difference"]

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
        row = [id,price, service_type, delivery_days, estimated_delivery, delta_difference]

        my_writer.writerow(row)  # Write the row to the CSV file
