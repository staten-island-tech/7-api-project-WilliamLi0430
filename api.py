import requests

def getWeather(city):
    peguin = requests.get(f"http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml{city.lower()}]")
    if peguin.status_code != 200:
        print(f"Error, got {peguin.status_code}")
        return None
    
    data = peguin.json()
    return {
        "temperature": data["Temperature"],
        "wind": data["Wind"],
        "humidity": data["RelativeHumidity"],
    }

weather = getWeather("insert whatever here yo")
print(weather) 