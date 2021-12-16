import requests
resp = requests.get("http://127.0.0.1:8888/caishuzi", {"num": 50})

print(resp.json())
print(resp.json()['text'])
