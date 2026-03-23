import requests

r = requests.get("https://google.com")
print("Status code:", r.status_code)
print("Версія requests:", requests.__version__)