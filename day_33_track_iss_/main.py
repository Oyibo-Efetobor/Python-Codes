import requests
from datetime import *
import smtplib

email = ''
email_password = ''

time_now = datetime.now()

my_lat = 8.140670
my_long = 5.102050



def check_iss_position():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()

    iss_data = iss_response.json()

    longitude = float(iss_data['iss_position']['longitude'])
    latitude = float(iss_data['iss_position']['latitude'])

    my_position = [my_long, my_lat]
    iss_position = [longitude, latitude]

        
    if (my_position[0] - 5) <= iss_position[0] <= (my_position[0] + 5) and \
       (my_position[1] - 5) <= iss_position[1] <= (my_position[1] + 5):
        return True
    else:
        return False


def check_iss_visibility():
    sun_parameters = {
        'lat': my_lat,
        'lng': my_long,
        'formatted':0
    }

    sun_response = requests.get('https://api.sunrise-sunset.org/json', params=sun_parameters)
    sun_response.raise_for_status()

    sun_data = sun_response.json()

    sunrise = int(sun_data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(sun_data['results']['sunset'].split("T")[1].split(":")[0])
    current_time = time_now.hour
    
    if sunrise <= current_time <= sunset:
        return True
    else:
        return False

def send_iss_email():
    # Create an SMTP connection
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=email, password=email_password)
        # Send the email
        connection.sendmail(
            from_addr=email,
            to_addrs='',
            msg="Check The ISS is above your area "
        )
        
if check_iss_position() and check_iss_visibility == "True":
    send_iss_email()