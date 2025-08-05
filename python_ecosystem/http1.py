import requests
ip = input("Enter IP to lookup: ")
res = requests.get(f"http://ip-api.com/json/{ip}")
data = res.json()
print(data)
print(f"{ip} is in {data['city']}, {data['country']}")

