import requests

url = "https://apis-sandbox.fedex.com/oauth/token"

payload ={
					"grant_type": "client_credentials",
					"client_id": "l741db4c1909b64e3bb1df3de33e9be6f7",
					"client_secret": "58775572edef49b4950f3dbca46c74cf"
        }
# 'input' refers to JSON Payload
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print (response.text)
