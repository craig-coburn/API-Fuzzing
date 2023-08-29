# Code to test API data requests

import requests     # HTTP client library
import json         # Parse REST API JSON data    
    
    
    
def get_data(base_url):
    response = requests.get(base_url)
    print('Getting data from API: ', base_url)
    print('Response Code: ', response.status_code)
    try:
        api_data = response.json()
        formatted_json = json.dumps(api_data, indent=2)  # Format JSON with indentation
        print(formatted_json)
        return api_data
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON response from API")
        return None



def extract_strings_with_word(api_data, keyword):
    matching_strings = []

    for item in api_data:
            for key, value in item.items():
                if isinstance(value, str) and keyword.lower() in value.lower():
                    matching_strings.append(value)

    return matching_strings



def main():
    api_url = "https://jsonplaceholder.typicode.com/" # Base URL
    api_endpoints = ["posts", "comments", "albums", "photos", "todos", "users"]
    
    # Make a get request to the API endpoint
    api_data = get_data(f'{api_url}{api_endpoints[0]}')
    
    keyword = "ERROR"
    strings_with_keyword = extract_strings_with_word(api_data, keyword)
    if strings_with_keyword:
        print(f"Strings containing the keyword '{keyword}':\n")
        for string in strings_with_keyword:
            clean_string = string.replace('\n', '')
            print(clean_string)
    else:
        print(f"No strings found containing the keyword '{keyword}'.")
        
        
    
if __name__ == "__main__":
    main()
