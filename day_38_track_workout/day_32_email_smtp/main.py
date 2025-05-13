import smtplib
import datetime as dt  # can be used to get current date and time
import random
from email.mime.text import MIMEText  # Added import for handling non-ASCII characters
import pandas as pd

email = ''
email_password = ''

days = {0: 'Monday',
        1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
        4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

now = dt.datetime.now()
day_of_week = now.weekday()


def send_mail(message):
    # Create an SMTP connection
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=email, password=email_password)
        # Send the email
        connection.sendmail(
            from_addr=email,
            to_addrs='',
            msg=message.as_string()  # Send the properly formatted MIME message
        )


def message_func():
    with open('quotes.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    # Construct the message
    message_text = days[day_of_week] + " , " + random.choice(lines)
    # Use MIMEText to encode the message as UTF-8
    msg = MIMEText(message_text, 'plain', 'utf-8')
    msg['Subject'] = 'Your Weekly Quote'
    msg['From'] = email
    msg['To'] = ''
    return msg


# Call the send_mail function with the properly formatted message
send_mail(message=message_func())

