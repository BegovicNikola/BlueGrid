import requests
import json

headers = {

    "X-Recharge-Access-Token": "abc123",

    "Accept":"application/json",

    "Content-Type":"application/json"

}

url = "https://api.rechargeapps.com/customers"

data ={
        "email": "watkinsglennco@gmail.com",

        "first_name": "Glenn",

        "last_name": "Watkins",

        "billing_first_name": "Glen",

        "billing_last_name": "Watkins",

        "billing_address1": "2588 Wayside Lane",

        "billing_zip": "94803",

        "billing_city": "El Sobrante",

        "billing_province": "California",

        "billing_country": "United States",

        "billing_phone":"5102236799"
}

result = requests.post(url, data=json.dumps(data), headers=headers)
print (result.text)
print (result)


