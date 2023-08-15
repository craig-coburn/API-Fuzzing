# Code to test API data requests


import requests     # HTTP client library
import json         # Parse REST API JSON data 

# API Endpoints
endpoints = ["posts", "comments", "albums", "photos", "todos", "users"]

# REST API
api_url = "https://jsonplaceholder.typicode.com/"
response = requests.get(f"{api_url}{endpoints[5]}")

# See the status code server returned
if response.status_code == 200: 
    print("API Request Successful")
else:
    print("API Request Denied. Check endpoint")

# Show what is in the API
print(response.content.decode("utf-8"))

# Parse JSON API data
api_data = response.json()

# List of fields in API data
for data in api_data:
    print(data.keys())



