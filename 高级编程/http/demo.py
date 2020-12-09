import requests

r = requests.get('http://106.12.220.252:8765/hot_words')
print(r.json())


print(r.json()["data"])

data = r.json()["data"]

for w in data:
    print(w)