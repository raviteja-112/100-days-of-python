import requests
import datetime as dt
from requests.auth import HTTPBasicAuth


headers =  {
    # 'Content-Type': 'application/json',
    'x-app-id': "1bcae3ff",
    'x-app-key': "2b06482a3314e4754924a35185394a3c"
  }

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

post_config = {
    "query" : f"{input('Tell me which exercises you did:')}",
    "gender" : "male",
    "weight_kg":80,
    "heihgt_cm":165,
    "age":20
}

sheety_url = "https://api.sheety.co/phill/myWebsite/emails"

basic = HTTPBasicAuth('username', 'password')

response = requests.post(url=URL,json=post_config,headers=headers,auth=basic)
response.status_code
print(response.json())

today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response_sheet = requests.post(url = sheety_url,json=sheet_inputs)

# bearer_headers = {
# "Authorization": f"Bearer {YOUR TOKEN}"
# }
# sheet_response = requests.post(
#     sheet_endpoint, 
#     json=sheet_inputs, 
#     headers=bearer_headers
# )
# print(os.environ.get('KEY_THAT_MIGHT_EXIST'))