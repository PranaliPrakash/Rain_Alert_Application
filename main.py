import requests
import os
from twilio.rest import Client

Api_Key = "cb704fc954cbaa778597d5a901c76a78"  # openweather
account_sid = "AC9030b0017cbc0658779ea9cd44c45860"  # twilio
auth_token = "5ecc5209c6e27163a3cb96947dfe4bb1"  # twilio
trial_no = "+16067160420"  # twilio
parameters = {"lat": -6.175110, "lon": 106.865, "appid": Api_Key}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)  # openweather_API
response.raise_for_status()
data = response.json()

id_list = []
for i in range(0, 12):
    id = data["hourly"][i]["weather"][0]["id"]
    id_list.append(id)

count = 0
for id_no in id_list:
    if id_no < 700:
        count += 1
if count > 1:
    client = Client(account_sid, auth_token)  # twilio
    message = client.messages \
        .create(
        body="It might be raining. Bring your umbrella.",
        from_=trial_no,
        to='+919359848038'
    )
    print(message.status)
else:
    print("no rain")


