
import requests
import json
import csv
import finalgui

def process():
    file = open("userInputData.csv", "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    print(data[5][0])
    weight = data[5][0]
    for i in range(len(data)):
        print(data[i][0])

    url = "https://api.shipengine.com/v1/rates/estimate"

    payload = json.dumps({
      "carrier_ids": [
        "se-4639556",
        "se-4639557",
        "se-4639575"
      ],
      "from_country_code": "US",
      "from_postal_code": f"{data[0][0]}",
      "to_country_code": "US",
      "to_postal_code": f"{data[1][0]}",
      "to_city_locality": f"{data[3][0]}",
      "to_state_province": f"{data[4][0]}",
      "weight": {
        "value": int(weight),
        "unit": "pound"
      },
      "dimensions": {
        "unit": "inch",
        "length": 5,
        "width": 5,
        "height": 5
      },
      "confirmation": "none",
      "address_residential_indicator": "no"
    })
    headers = {
      'Host': 'api.shipengine.com',
      'API-Key': "yC2kbZKGhwrV5cPL1Bmi/p7q576N3ELNzX6kfo7zewE",
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jsondata = response.json()
    print(response.text)

    with open("sample.json", "w") as outfile:
      json.dump(jsondata,outfile)
    dump1 = json.loads(response.text)

    from finalgui import drill
    finalgui.drill()

    # for i in range (28):
    #   print("carreir id :",dump1[i]["carrier_id"])
    #   print("Price: ",dump1[i]["shipping_amount"]["amount"])
    #   print("Type of package : ",dump1[i]["package_type"])
    #   print("Service type : ",dump1[i]["service_type"])
    #   print("Estimated Delivery", dump1[i]["estimated_delivery_date"])
    #   print("Delivery Days : ", dump1[i]["delivery_days"])
    #   print("---------------------")

