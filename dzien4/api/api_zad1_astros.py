# REST API (Representational State Transfer Application Programming Interface
# ) to styl architektoniczny dla budowania usług sieciowych,
# wykorzystujący standardowe żądania HTTP (GET, POST, PUT, DELETE)
# do wymiany danych (najczęściej w formatach JSON/XML) między aplikacjami (klient-serwer),
# umożliwiający prostą, skalowalną i zunifikowaną komunikację między systemami, działając jak "kelner" dostarczający dane.
import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx - warnngi przekierowania
# 4xx - bład po stronie klienta, 404 Page Not Found, 400 Bad Request
# 5xx - błedy po stronie serwera
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP

print(response.text)
print(type(response.text)) # str

response_data = response.json()
print(type(response_data)) # <class 'dict'>

for i in response_data:
    print(i)
# people
# number
# message

print(response_data['people'])