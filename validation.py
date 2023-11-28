import requests
import json

url = "https://api.shipengine.com/v1/addresses/validate"

payload = json.dumps([
  {
    "address_line1": "56 Crescent pl ",
    "city_locality": "Bridgeport",
    "state_province": "CT",
    "postal_code": "06608",
    "country_code": "US"
  }
])
headers = {
  'Host': 'api.shipengine.com',
  'API-Key': 'TEST_YVrjR5qjiK1R94jQqsTjLj0P759U03vZJtFoRjtk3e4',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)