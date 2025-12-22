import requests

def getWeather(weather):
    peguin = requests.get(f"https://dataservice.accuweather.com/currentconditions/v1{weather.lower()}]")
    if peguin.status_code != 200:
        print(f"Error, got {peguin.status_code}")
        return None
    
    data = peguin.json()[0]
    return {
        "temperature": data["Temperature"]["Metric"]["Imperial"],
        "wind": data["Wind"]["Direction"]["Speed"],
        "humidity": data["RelativeHumidity"],
    }

weather = getWeather("temperature")
print(weather) 