import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
import pandas as pd

email = ''
email_password = ''

letter_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

todays_date = dt.date.today()
todays_date_tuple = (todays_date.month, todays_date.day)  # e.g., (10, 10)
birthday_data = pd.read_csv('birthdays.csv')

recipient_list = []


def send_mail(recipients, message):
    # Create an SMTP connection
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=email, password=email_password)
        # Send the email
        connection.sendmail(
            from_addr=email,
            to_addrs=recipients,
            msg=message  # Send the message content
        )


birthdays_dict = {
    (row['month'], row['day']): [row['email'], row['name']]
    for index, row in birthday_data.iterrows()
}


def get_name():
    for i in birthdays_dict:
        if i == todays_date_tuple:
            recipient_list.append(birthdays_dict[i][0])
            the_name = birthdays_dict[i][1]
    return the_name


# Create or clear the final_letter.txt
with open('final_letter.txt', 'w') as final_file:
    pass


def replace_letter(name):
    with open('letter_templates/' + random.choice(letter_list), 'r') as file:
        with open('final_letter.txt', 'a') as final_file:  # Open in append mode
            for line in file:
                if '[NAME]' in line:
                    line = line.replace('[NAME]', name)  # Replace the placeholder with the name
                final_file.write(line)  # Write the modified line to the final letter


# Get the name and replace placeholders in the letter
replace_letter(get_name())

# Read the content of final_letter.txt after writing to it
with open('final_letter.txt', 'r') as final_file:
    final_content = final_file.read()

# Create the email message with subject
subject = "HAPPY BIRTHDAY"
message = f"Subject: {subject}\n\n{final_content}"

# Send the email using the content read from final_letter.txt
send_mail(recipient_list, message)
print('\n\n')
print("Email sent to:", recipient_list)
print('\n\n')