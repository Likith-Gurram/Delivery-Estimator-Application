
import requests

url = "https://apis-sandbox.fedex.com/rate/v1/rates/quotes"

payload ={
  "accountNumber": {
    "value": "740561073"
  },
  "requestedShipment": {
    "shipper": {
      "address": {
        "postalCode": 65247,
        "countryCode": "US"
      }
    },
    "recipient": {
      "address": {
        "postalCode": 75063,
        "countryCode": "US"
      }
    },
    "pickupType": "DROPOFF_AT_FEDEX_LOCATION",
    "rateRequestType": [
      "ACCOUNT",
      "LIST"
    ],
    "requestedPackageLineItems": [
      {
        "weight": {
          "units": "LB",
          "value": 10
        }
      }
    ]
  }
}
headers = {
    'Content-Type': "application/json",
    'X-locale': "en_US",
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJDWFMiXSwiUGF5bG9hZCI6eyJjbGllbnRJZGVudGl0eSI6eyJjbGllbnRLZXkiOiJsNzQxZGI0YzE5MDliNjRlM2JiMWRmM2RlMzNlOWJlNmY3In0sImF1dGhlbnRpY2F0aW9uUmVhbG0iOiJDTUFDIiwiYWRkaXRpb25hbElkZW50aXR5Ijp7InRpbWVTdGFtcCI6IjI3LUFwci0yMDIzIDE2OjIzOjU5IEVTVCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJhcGltb2RlIjoiU2FuZGJveCIsImN4c0lzcyI6Imh0dHBzOi8vY3hzYXV0aHNlcnZlci1zdGFnaW5nLmFwcC5wYWFzLmZlZGV4LmNvbS90b2tlbi9vYXV0aDIifSwicGVyc29uYVR5cGUiOiJEaXJlY3RJbnRlZ3JhdG9yX0IyQiJ9LCJleHAiOjE2ODI2MzQyMzksImp0aSI6IjNkYWQzYjE1LTM4NTYtNGMwZS1iMjY2LWZkNzkyZWEyNjQyZCJ9.iCaeQbfFuFHuEK3Eewo1NZ5_TGVGusMkCjgw26uoDSIwhnF5hBeFkiphDMCQsyVTUg2nhxARAOZnYmhdO3N0CK0C7re1vX5H3Lxpiwt0wo2pAnGBOBOwWUVK-ViSnPqz6i9R_nPe5oaTWQioUTfK2EOw6Td-jP-WGFZfr6yYQ1rB0U3DkU-EvAwe93W_ifOPL-2Lzz8jtEBPWRiPIMkVcI3WfCzaoEBoGIp-qF-JplEv_VLI8EUWIrOdSn7wwqMPInox8QBDQ0i901FqJh9Ih8iJ4K3PUUi9anMud5EDd7XuXsw3it77YAo4CaS_LwMulSuouscx4l03f0lYcTzw5LLmrNXMbRJzGuEwkDYnjivBXcNIR2O2OXoM0PVChtohVMdUJ4IHyuYZ2EsQAvJ9mCL-U2JIZm4oEJ6ermQDRQszwo6KrjV6HgBQ3T4h-KRvzhprZ9j1oeRypGRoDjf9wySJsJZ95w9TEIdrQdQHYucFnVk4vSEUCNpVrACyhRLSuz3qV7seMIzqcyS2IITJZ_YuvcXsj-cP4F9tFkW0iARVNTR-YVYxu3Kuhcg6bPoGOawa8dQ3ZueZMtMkXk3gUPjFTzK-esR3qvvNRiHL0ZVavOFbhC_f2u5mrckbYlWelid58LhnJgePcE2lFWkFQxPKLRCx2N6b5ssKqLu_K-o"
    }

response = requests.request(method = "POST",url = url, data=payload ,headers=headers)

print(response.text)