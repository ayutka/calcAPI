import requests


r_get = requests.get("http://0.0.0.0:8080/?formula=2 * 3")

print(r_get.json())