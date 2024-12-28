import smtplib

my_email = "xyz@gmail.com"
password = "123456789"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password = password)
# connection.sendmail(from_addr=my_email,to_addrs="abc@gmail.com",msg = "Subject:hello\n\n"
#                     "this is the body of emial")

# connection.close

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password = password)
#     connection.sendmail(from_addr=my_email,to_addrs="abc@gmail.com",msg = "Subject:hello\n\n"
#                         "this is the body of emial")


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1995, month=12, day=15)

import datetime as dt
import random
now = dt.datetime.now()
day = now.weekday()

if day == 0:
    try:
        with open("Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt",mode='r') as file:
                data = file.readlines()
    except FileNotFoundError:
        print("your file is missing")
    else:
        if data: 
            # quotes = [data.strip() for data in data ]
             msg = random.choice(data)
        else:
            print("your file is empty")

# msg = random.choice(quotes)
print(msg)



