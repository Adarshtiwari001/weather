import requests

def get_weather_forecast(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for any request errors

        data = response.json()
        if data["cod"] == "200":
            city = data["city"]["name"]
            country = data["city"]["country"]
            print(f"Weather forecast for {city}, {country}:")

            for forecast in data["list"]:
                date_time = forecast["dt_txt"]
                weather_description = forecast["weather"][0]["description"]
                temperature = forecast["main"]["temp"]
                humidity = forecast["main"]["humidity"]
                wind_speed = forecast["wind"]["speed"]

                print(f"Date/Time: {date_time}, Weather: {weather_description}, "
                      f"Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")

        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "ef1f2a01e7ded25ecbd177b8be02e3c3"
    
    while True:
        city = input("Enter city name (or 'quit' to exit): ")
        if city.lower() == 'quit':
            break
        
        get_weather_forecast(api_key, city)
