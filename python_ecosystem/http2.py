import requests

url = "https://api.abuseipdb.com/api/v2/blacklist"

headers = {
    "Key": "YOUR_API_KEY_HERE",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)

for entry in data.get("data", [])[:5]:
    print(f"IP: {entry['ipAddress']} - Reports: {entry['numReports']}")
