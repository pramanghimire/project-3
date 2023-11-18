import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc}")
    else:
        print("City not found.")

# Test the function
get_weather("London")
