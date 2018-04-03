import requests
import json

headers = {
    "X-Recharge-Access-Token": "abc123",
    "Accept":"application/json",
    "Content-Type":"application/json"
}
url = "https://api.rechargeapps.com/subscriptions"
data = {
    "address_id":9745455,
    "next_charge_scheduled_at":"2017-04-01T00:00:00",      
    "product_title":"Sumatra Coffee",
    "price":13,
    "quantity":7,
    "shopify_variant_id":3844924611,
    "order_interval_unit":"day",
    "order_interval_frequency":"30",
    "number_charges_until_expiration": 2,
    "charge_interval_frequency":"30",
    "order_day_of_month":None,
    "order_day_of_week":None,
    "properties": [
                        {
                          "name": "grind",
                          "value": "drip"
                        },
                        {
                          "name": "size",
                          "value": "medium"
                        }
                      ]
      }

result = requests.post(url, data=json.dumps(data), headers=headers)
print (result.text)
print (result)


