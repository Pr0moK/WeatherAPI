import string
import requests

def get_weather(city):
    if city is None:
        city = "London"
    params = {
        "API_KEY": "YOUR_API_KEY",
        "API_URL": "https://api.weatherstack.com/current?access_key="
    }

    response = requests.get(params['API_URL']+params['API_KEY']+f"&query={city}")
    if response.status_code == 200:
        data = response.json()
        country=data['location']['country']
        time=data['current']['observation_time']
        temperature=data['current']['temperature']
        return {'country': country, 'time': time, 'temperature': temperature}
    else:
        print("Error")

def CheckCityName(city):
    for i in city:
        if i not in string.ascii_letters:
            return False
    return True
