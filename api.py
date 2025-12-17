import requests

def getWeather(weather):
    instead = requests.get(f"https://developer.accuweather.com/core-weather/location-key-currentconditions")
    if instead.status_code != 200:
        print("Error")
        return None
    
    data = instead.json()
    return {
        "temperature": data["Temperature"],
        "wind": data["Wind"],
        "humidity": data["Humidity"],
        "visibility": data["Visibility"]
    }

weather = getWeather("temperature")
print(weather)