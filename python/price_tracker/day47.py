import requests
from bs4 import BeautifulSoup
# import lxml
import smtplib

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept-Language":"en-US,en;q=0.5"
}

response =requests.get(url=URL,headers=headers)
web = response.text
soup = BeautifulSoup(web,"html.parser")
price_dollars = soup.find(name = "span",class_ = "aok-offscreen").get_text()

price = price_dollars.split("$")[1]
print(price)
if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="example.com",password = "password")
        connection.sendmail(from_addr="my_email",to_addrs="abc@gmail.com",msg = "Subject:Price Drop\n\n"
                            f"The product has price drop : {soup.title.get_text()}")
