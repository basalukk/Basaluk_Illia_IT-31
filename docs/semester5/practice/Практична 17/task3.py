import requests
import sys

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.75,
    "longitude": 25.34,
    "current": "temperature_2m,wind_speed_10m"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    current = data["current"]
    units = data["current_units"]

except (requests.RequestException, KeyError, ValueError) as error:
    print(f"Помилка отримання погоди: {error}", file=sys.stderr)
    sys.exit(1)

print("Illia Basalukk, IT-31")
print("Місто: Луцьк")
print(f"Температура: {current['temperature_2m']} {units['temperature_2m']}")
print(f"Швидкість вітру: {current['wind_speed_10m']} {units['wind_speed_10m']}")
print(f"Час вимірювання: {current['time']}")
