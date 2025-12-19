import requests

def getWeather(weather):
    instead = requests.get(f"https://dataservice.accuweather.com/{weather.lower()}]")
    if instead.status_code != 200:
        print("Error")
        return None
    
    data = instead.json()[0]
    return {
        "temperature": data["Temperature"]["Metric"]["Imperial"],
        "wind": data["Wind"]["Direction"]["Speed"],
        "humidity": data["RelativeHumidity"],
    }

weather = getWeather("temperature")
print(weather) 