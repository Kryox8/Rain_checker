import requests
import json
import os
from twilio.rest import Client

acount_sid = os.environ['SMS_API_SID']
auth_token = os.environ['SMS_AUTH_TOKEN']
peronal_phone_number = os.environ['PERSONAL_PHONE_NUM']

client = Client(acount_sid,auth_token)
#-----TWILIO INFO ABOVE------------------------------

api_key = os.environ.get('WEATHER_API_KEY')

cords = {'latitude' : 20.613345541991823 , 'longitude' :  -100.40839255181642}
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={cords['latitude']}&lon={cords['longitude']}&appid={api_key}'

response = requests.get(url=url)
json_data = response.json()



relevant_entries = json_data['list'][:6]


"""
for entry in relevant_entries:
    if 500<= entry['weather'][0]['id'] <=599:
        client.messages.create(

            to=peronal_phone_number,
            from_= '+12769001378',
            body='Bring an umberlla its probably gonna rain 🌧️!'
        )

        print('message sent')
        
"""

client.messages.create(

            to=peronal_phone_number,
            from_= '+12769001378',
            body='Bring an umberlla its probably gonna rain 🌧️!'
        )

       
print('message sent')