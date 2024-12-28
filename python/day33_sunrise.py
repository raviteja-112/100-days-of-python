import requests

#response = requests.get(url="https://api.sunrise-sunset.org/json?lat=14.467354&lng=78.824135&date=today&tzid=Asia/Kolkata" )
#better approach

MY_LAT = 14.467354 
MY_LONG = 78.824135 
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "tzid": "Asia/Kolkata",
    "formatted" : 0 
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters )

response.raise_for_status

data = response.json()

sunrise = data["results"]["sunrise"]
sunrise = sunrise.spilt("T")[1].spilt(":")[0] ##this gives hours

sunset = data["results"]["sunset"]
sunset = sunset.spilt("T")[1].spilt(":")[0] ##this gives hours
