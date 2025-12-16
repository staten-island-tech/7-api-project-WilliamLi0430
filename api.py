import requests

def getWeather(weather):
    instead = requests.get(f"https://www.wunderground.com/forecast/us/ny/new-york-city")
    if instead.stautus_code != 200:
        print("Error")
        return None
    
    data = instead.json()
    return {
        "temperature": data["temperature"],
        