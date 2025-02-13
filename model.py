import requests
import json

def ignore():
    response = requests.get("https://api.weather.gov/openapi.json")
    print(response)
    weather_data = response.json()
    #print(weather_data)
    paths = weather_data["paths"]
    #iterates through the paths, assigns function to the sub path i.e get or post
    for path, function in paths.items():
        #function, details looks at the details of the get or post function. If its a dict, then print the description of it
        for function, details in function.items():
            if isinstance(details, dict):
                description = details.get("description", "No description available")
                print(f"Path: {path}")
                print(f"Description: {description}\n")

def getJson(endpoint):
    clean_response = ""
    response = requests.get(endpoint)
    #print(response)
    weather_data = response.json()
    #print(weather_data)
    print(f"Weather Data: {weather_data}")
    return weather_data



def getPaths(endpoint=""):
    response = requests.get(f"https://api.weather.gov/openapi.json{endpoint}")
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code} from {endpoint}")
        return []

    weather_data = response.json()
    if "paths" not in weather_data:
        print(f"Error: 'paths' not found in the response for {endpoint}")
        return []

    return list(weather_data["paths"].keys())

def getEndpointResponse(endpoint):
    parsed = (requests.get(endpoint)).json()
    #parsed = json.loads(response)
    #print(json.dumps(parsed, indent = 4))
    return json.dumps(parsed, indent = 4)

if __name__ == "__main__":
    #getJson()
    print("success")