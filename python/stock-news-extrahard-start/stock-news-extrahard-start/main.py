
#inefficinet and not optimized for reading
#used unecessary functions

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = "QCS7WBIS5KF2ZA63"
STOCK_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API
}

NEWS_API = "c54d4c57e59348679c6ea3fdb67fad6b"
NEWS_parameters = {
    "q" : COMPANY_NAME,
    "apiKey":NEWS_API
}

account_sid = "your sid here"
auth_token = "your auth token"

def get_news():
    news_response = requests.get(url= "https://newsapi.org/v2/everything?",params=NEWS_parameters)
    news_response.raise_for_status
    news_data = news_response.json()
    # news_data = {news_data["articles"][f"{i}"] for i in range(3) }
    # news_data = [news_data["articles"][f"{i}"]["title"] for i in range(3)]
    headlines = [article["title"] for article in news_data["articles"][:3]]
    description = [article["description"] for article in news_data["articles"][:3]]

    return headlines,description

def sending_message(headlines,description,result):
    for i in range(len(headlines)):
            if result > 5 :
                 emoji = "🔺"
            else:
                 emoji = "🔻"
            client = Client(account_sid=account_sid,auth_token=auth_token)
            message = client.messages \
                .create(
                     body=f"{COMPANY_NAME}{emoji}{result}%""\n"
                     "Headline:"f"{headlines[i]}""\n"
                     "Breif:"f"{description[i]}",
                     from_='+15017122661',
                     to='+15558675310',
                 )






## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url="https://www.alphavantage.co/query?",params=STOCK_parameters)
stock_response.raise_for_status

stock_data = stock_response.json()
stock_data = stock_data["Time Series (Daily)"]
data_list = list(stock_data.items()) #could be used list compreshion for only values
yesterday = float(data_list[0][1]["4. close"])
day_before_yesterday = float(data_list[1][1]["4. close"])
result = ((yesterday - day_before_yesterday) / yesterday) * 100 #could be used abs funciton to reduce code
if result >= 5 or result <= -5:
    sending_message(get_news(result))



    


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

