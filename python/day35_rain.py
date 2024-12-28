import requests
import os
from twilio.rest import Client

api_key = "218c15391ef97980ff2449d1dadc89e5"
# api_key = os.environ.get("API_KEY")
account_sid = "your sid here"
auth_token = "your auth token"

MY_LAT = 14.467354
MY_LONG = 78.824135
parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : api_key,
    "cnt" : 4
}
response = requests.get("http://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status
weather_data = response.json()

will_rain = False
ids = [int(entry['weather'][0]['id']) for entry in weather_data['list']]


for id in ids:
    if id <700:
        will_rain = True
if will_rain:
    client = Client(account_sid=account_sid,auth_token=auth_token)
    message = message = client.messages \
                .create(
                     body="It is raining outside,bring your umbrella",
                     from_='+15017122661',
                     to='+15558675310'
                 )

    print(message.status)




