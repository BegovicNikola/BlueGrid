import requests
import json

headers = {
    "X-Recharge-Access-Token": "abc123",
    "Accept":"application/json",
    "Content-Type":"application/json"
} 
url = "https://api.rechargeapps.com/customers/3411137/addresses"
data = {
    "address1": "2588 Wayside Lane",
    "address2": "",
    "city": "El Sobrante",
    "province": "California",
    "first_name": "Glenn",
    "last_name": "Watkins",
    "zip": "94803",
    "company": "ReCharged",
    "phone": "5102236799",
    "country": "United States",
    "original_shipping_lines": [
            {
                "price": "10.00",
                "code": "Standard Shipping",
                "title": "Standard Shipping"
            }
        ]
  }

result = requests.post(url, data=json.dumps(data), headers=headers)
print (result.text)
print (result)
