import smtplib
import datetime as dt
from random import choice

SENDER = "example1@gmail.com"
PASSWORD = "Example.password1"
RECEIVER = "example2@gmail.com"

now = dt.datetime.now()
today = now.weekday()

if today == 0:  # Check for Monday
    try:
        with open("quotes.txt", mode="r") as file:
            quote_list = file.readlines()
            quote = choice(quote_list)
    except FileNotFoundError:
        pass
    else:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(SENDER, PASSWORD)
            message = f"Subject: Monday Motivation\nFrom: {SENDER}\nTo: {RECEIVER}\n\n{quote}"
            connection.sendmail(SENDER, RECEIVER, message)
