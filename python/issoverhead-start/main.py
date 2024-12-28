import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 14.467354 # Your latitude
MY_LONG = 78.824135  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def position():
    if MY_LAT < iss_latitude+5 and MY_LAT > iss_latitude-5 and MY_LONG < iss_longitude+5 and MY_LONG > iss_longitude-5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

def dark():
    if time_now > sunset and time_now > sunrise:
        return True
    else:
        return False
    

while(1):
    time.sleep(10)
    if dark() and position():
        # with smtpd.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user = "my email",
        #                      password = "my password")
        #     connection.sendmail(from_addr = "my email",
        #                         to_addrs = "my email",msg =
        #                         "Suject:Iss station\n\n"
        #                         "now you can see ISS Station from your home")
        print("you can see iss!")
    else:
        print("you cannot see iss now! ")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



