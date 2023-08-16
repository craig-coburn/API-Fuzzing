# Code to test API fuzzing


import requests
import random       # Generate random inters, floats and strings
import string       # String manipulation


base_url = "https://jsonplaceholder.typicode.com/"

# List of endpoints to fuzz
endpoints = ["/posts", "/comments", "/albums", "/photos", "/todos", "/users"]

# Generate random string
def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def fuzz_request(endpoint, payload):
    url = base_url + endpoint
    response = requests.post(url, json=payload)
    return response

fuzz_vectors = [
    # Fuzz vectors for integers
    {"data": "normal_input", "value": 42, "status": "active"},
    {"data": "zero_input", "value": 0, "status": "inactive"},
    {"data": "negative_input", "value": -100, "status": "active"},
    {"data": "big_number_input", "value": 9999999999, "status": "active"},
    
    # Fuzz vectors for characters
    {"data": "normal_input", "value": "Hello, World!", "status": "active"},
    {"data": "escaped_quotes", "value": "It's a test", "status": "inactive"},
    {"data": "sql_injection", "value": "1' OR '1'='1", "status": "active"},
    
    # Fuzz vectors for binary
    {"data": "random_binary", "value": bytes([random.randint(0, 255) for _ in range(10)]), "status": "active"},
    # Add more fuzz vectors for binary inputs
]

for endpoint in endpoints:
    test_case = 1
    print(f"Fuzzing endpoint: {endpoint}")
    for vector in fuzz_vectors: 
        response = fuzz_request(endpoint,vector)

        # Uncomment to see response
        print(f"Test case: {test_case}")
        print(f"Payload: {vector}\nResponse: {response.status_code} {response.content}")

        # Analyze response for potential vulnerabilities
        if response.status_code == 200:
            print("Vulnerability found!\n")
            print(f"Error case: {payload}")
            # Check the error that was produced
            print(f"Error: {response.content.decode('utf-8')}")
        else: 
            print(f"No vulnerability found in {endpoint}\n")
        test_case += 1


