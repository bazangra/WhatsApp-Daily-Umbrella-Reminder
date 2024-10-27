import requests
from twilio.rest import Client

account_sid = 'ACbbb8fba945900aa7f2a1f4116d1b4ab3'
auth_token = '3a82e7c3b683c8f2d3bd6f80ad1cc50c'
api_key = "ba745ec27bb5d154e7ca2bb08e2bc42c"
MY_LAT = 51.952110
MY_LONG = -3.028390

weather_para = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_para)

response.raise_for_status()
data = response.json()

will_rain = False
list2 = data["list"]
for each in list2:
    if int(each["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='It"s is going to rain today. Remember to bring an ☂️',
        to='whatsapp:+447711259832'
    )
    print(message.status)