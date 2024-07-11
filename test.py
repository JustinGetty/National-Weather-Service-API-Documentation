import requests

def testOutput():
    response = requests.get("https://api.weather.gov/openapi.json")
    print(response)
    weather_data = response.json()
    #print(weather_data)
    for path, function in weather_data.items():
        print(f"Path: {path}\nFunction: {function}")

def description():
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

if __name__ == "__main__":
    description()