import csv
import smtplib
import datetime as dt
import pandas
import random


##################### Extra Hard Starting Project ######################
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

#birthday data
data = pandas.read_csv("birthdays.csv")

#date
now = dt.datetime.now()
now_month = now.month
now_day = now.strftime(("%d"))

#email creds (Vul hier je eigen email & wachtwoord in)
my_email = ""
password = ""


#is there a birthday? if so;
if data._get_value(0, "month") == now_month and data._get_value(0, "day"):
    random_letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(random_letter) as letter_file:
        text = letter_file.read()
        change_name = text.replace("[NAME]", data._get_value(0, "name"))
        connection = smtplib.SMTP("outlook.office365.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=random.choice(data["email"]),
            msg=f"Subject:Happy Birthday! \n\n{change_name}")
        connection.close()













