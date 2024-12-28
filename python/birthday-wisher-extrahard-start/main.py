##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "your email"
MY_PASSWORD = "your password"


now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month,today_day)

data = pandas.read_csv("birthday-wisher-extrahard-start/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


def random_letter(name):
    number = random.randint(1,3)
    with open(f"birthday-wisher-extrahard-start/letter_templates/letter_{number}.txt") as file:
        text = file.read()
    personal_msg = text.replace("[NAME]",f"{name}")
    return personal_msg

def check_birthdays():
        if today_tuple in birthdays_dict:
            name = birthdays_dict[(today_month,today_day)]["name"]
            content = random_letter(name)
            email = birthdays_dict[(today_month,today_day)]["email"]
        sending_mails(content,email)

def sending_mails(content,email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password = MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,msg = "Subject:Birthday Wishes\n\n"
                            f"{content}")
    print(content,email)



check_birthdays()




        



