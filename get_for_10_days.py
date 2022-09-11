import arrow
import requests


start = arrow.get("2021-05-15")
auth_key = input("Enter your own API key: ")
response = requests.get(
  "https://api.stormglass.io/v2/weather/point",
  params={
    # Villers-sur-Mer : 49.32195479823806, -0.011785196637717673
    "lat": 49.322,
    "lng": -0.012,
    "start": start.to("UTC").timestamp(),  # Convert to UTC timestamp
    'end': start.shift(days=1).to("UTC").timestamp(),
  },
  headers={
    "Authorization": auth_key
  }
)

# Do something with response data.
json_data = response.json()
data = open("data.json", "a")
data.writelines("\n")
to_write = "Data for 10 days from the " + start.format('YYYY-MM-DD HH:mm:ss ZZ')
data.writelines(to_write)
data.writelines("\n"*2)
data.writelines(json_data)
data.writelines("\n"*2)
