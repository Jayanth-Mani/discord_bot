import requests
from temperature_change import k_to_f
from dotenv import load_dotenv
import os

'''
res = requests.get('https://prettyprinted.com')

print(res.text)

if res:
    print("Response OK")
else:
    print("Response Failed")
'''

load_dotenv("ultimate.env") # replace ".env" with whatever you named your file
api_key = os.environ.get("weather_API_KEY")

url = "http://api.openweathermap.org/data/2.5/"

def weather_report(city):
    final_url = url + "weather?appid=" + api_key + "&q=" + city.lower()
    json_data = requests.get(final_url).json()
    print(json_data)
    description = json_data["weather"][0]["description"]
    temperature = str(round(k_to_f(json_data["main"]["temp"]), 2)) + "°F"
    feels_like = str(round(k_to_f(json_data['main']['feels_like']), 2)) + "°F"
    return str(description), str(temperature), str(feels_like)

def weather_forecast(city):
    final_url = f"{url}forecast?q={city.lower()}&appid={api_key}"
    json_data = requests.get(final_url).json()
    results = {}
    day = 1
    for it in range(40):
        time = str(json_data["list"][it]["dt_txt"][11:])
        if time == "12:00:00":
            results.update({"day " + str(day): "Low: " + str(round(k_to_f(json_data["list"][it]["main"]["temp_min"]), 2)) + "°F " + "\nHigh: " + str(round(k_to_f(json_data["list"][it]["main"]["temp_max"]), 2)) + "°F " + "\nHumidity: " + str(json_data["list"][it]["main"]["humidity"]) + "%"})
            day += 1
            print(results)
    return results

'''cities = ["boston", "chicago", "san francisco",]
weather = []
temperature = []
feels_like = []
for city in cities:
    final_url = url + "appid=" + api_key + "&q=" + city.lower()
    json_data = requests.get(final_url).json()
    weather.append(json_data["weather"][0]["description"])
    temperature.append(str(round(k_to_f(json_data["main"]["temp"]), 2)) + "°F")
    feels_like.append(str(round(k_to_f(json_data['main']['feels_like']), 2)) + "°F")
    #formatted_data = city +":" + "\nCurrent weather: " + json_data["weather"][0]["description"] + "\nThe temperature is: " + str(k_to_f(json_data["main"]["temp"])) + "°F" + "\nFeels like: " + str(k_to_f(json_data['main']['feels_like'])) + "°F"
    #print(formatted_data)

print(weather)
print(temperature)
print(feels_like)

weather_data = pd.DataFrame(
    {
        'Weather' : weather,
        'Temperature' : temperature,
        'Feels Like': feels_like,
    },
    index = cities
)

print(weather_data)
weather_data.to_csv('weather.csv')
'''