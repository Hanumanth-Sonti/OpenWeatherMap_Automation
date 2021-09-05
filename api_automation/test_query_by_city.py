import requests
import pytest

# API Key of OpenWeatherMap
api_key = "24d8ecf8629a97ff64a8c046bc830ee3"

# Base URI of the Openweather map API
base_uri = 'https://api.openweathermap.org/data/2.5/weather'

# function to run the get API Call
def get_response(uri):
    # Get Request of input value
    response = requests.get(uri)

    # Capture Response Parameters
    print(f'Response Code = {response.status_code},Response Text = {response.text}')
    if (not response.url.__contains__('weather')):
        print(f"URL not directing to OpenWeatherMap API {response.url.__contains__('weather')}")
    return response

def validate_city(response,city_name):
    #Validate using name attribute - City Name
    if response.json()['cod']=='404':
        print(f'City with name {city_name} not found')
        assert response.json()['cod'] == 200, f'Invalid City {city_name}'
    else:
        assert (response.json()["name"]).lower() == city_name.lower(), \
            f"City Name {city_name} mismatch in weather data weather_data['name']"
        print(f"Name attribute {response.json()['name']} and {city_name} matched")

def print_weather_data(weather_data,city_name):
    try:
        # Capture Weather Data
        current_temp = (weather_data['main']['temp'] - 273.15)
        min_temp = weather_data['main']['temp_min']
        max_temp = weather_data['main']['temp_max']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        windspeed = weather_data['wind']['speed']
        weather_description = weather_data['weather'][0]['description']
        weather_main = weather_data['weather'][0]['main']
        clouds = weather_data['clouds']['all']

        # Print Weather statistics
        print('---Weather Statistics for City Name--{}'.format(city_name))
        print(f'Weather Description: {weather_description}')
        print(f'Current Temperature: {current_temp}')
        print(f'Humidity: {humidity}')
        print(f'Pressure: {pressure}')
        print(f'Wind Speed: {windspeed}')
        print(f'Min Temperature: {min_temp}')
        print(f'Max Temperature: {max_temp}')

        # Calculate Temperature in Celsis and Fahrenheit
        fahrenheit = float(current_temp)
        celsius = (fahrenheit - 32) * 5 / 9
        fahrenheit = (celsius * 9 / 5) + 32
        print(' Fahrenheit:{f}  Celsius: {c}'.format(f=fahrenheit, c=celsius))
    except KeyError:
        print(f'Key error to print weather statistics for city {city_name}')
        # print the cod value
        print(f"Error Cod: weather_data['cod']")

#Check Weather Acivity
def check_WeatherActivity(weather_data):
    #Get Weather description and Main
    weather_description = weather_data['weather'][0]['description']
    weather_main = weather_data['weather'][0]['main']
    # Check Weather is clear for outdoor activities
    if ((weather_description).lower() == ('clear sky') and
            (weather_main).lower() == 'clear'):
        print('Weather is good for outdoor activities due to clear sky or clear')
    else:
        print(f'Weather not good for outdoor activities due to {weather_description}')

#Test - Query Weather API using City Name
@pytest.mark.city
def test_query_by_city_name():
    # Enter the City Name
    city_name = input("Enter the City Name to check weather")
    print('City Name entered: {}'.format(city_name))

    # Query using the city name
    uri = base_uri + '?q=' + city_name.lower() + "&appid=" + api_key
    print(f'Query Weather API using City Name: {uri}')

    # Search by City Name
    response = get_response(uri)

    #Validate City is found
    validate_city(response,city_name)

    # print weather data of the city
    weather_data = response.json()
    print_weather_data(weather_data, city_name)

    #Check Weather Activity for Outdoor Activities
    check_WeatherActivity(weather_data)

#Test - Query Weather API using City Name and Country Code
@pytest.mark.city
def test_query_by_city_country_code():
    # Query weather API using City name and Country Code
    # Enter the City Name
    city_name = input("Enter the City Name to check weather")
    print('City Name entered: {city}'.format(city=city_name))

    # Enter the Country Code
    country_code = input("Enter the Country Code to check weather")
    print('Country Code entered: {cc}'.format(cc=country_code))

    # Query using the city name and state_code
    uri = base_uri + '?q='+ city_name.lower() + ","+ country_code.lower() + "&appid=" + api_key
    print(f'Query Weather API using City Name and Country Code: {uri}')

    # Search by City Name and Country Code
    response = get_response(uri)

    # Validate City is found
    validate_city(response, city_name)

    # print weather data of the city
    weather_data = response.json()
    print_weather_data(weather_data, city_name)

    # Check Weather Activity for Outdoor Activities
    check_WeatherActivity(weather_data)

