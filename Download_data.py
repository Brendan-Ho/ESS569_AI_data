import requests

# Replace with actual API endpoint and API key
api_url = "https://opendata.lifebit.ai/api/v1/datasets"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
params = {
    "search": "assigned species: Staphylococcus aureus"
}

# Make request
response = requests.get(api_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print("Data:", data)
else:
    print("Failed to retrieve data:", response.status_code, response.text)
