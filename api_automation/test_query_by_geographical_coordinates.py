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
    print(response.status_code)
    # Capture Response Parameters
    assert response.status_code == 200, "Weather Data not found " \
                                        f'Actual Response Code = {response.status_code},' \
                                        f'Response Text = {response.text}'
    assert response.url.__contains__('weather'), "URL not directing to OpenWeatherMAP API"
    return response

@pytest.mark.geography
def test_query_by_geographical_coordinates():
    #Input Latitude
    latitude = input("Enter Latitude")
    print(f'Latitude entered: {latitude}')

    #Input Longitude
    longitude = input("Enter Longitude")
    print(f'Longitude entered: {longitude}')

    # Query using the longitude and latitude
    uri = base_uri + "?lat=" + str(latitude) + "&lon="+ str(longitude)+"&appid=" + api_key
    print(f'Query weather API using Latitude {latitude} and Longitude {longitude}: {uri}')

    # Search by Latitude and Longitude
    weather_data = get_response(uri)
    weather_data = weather_data.json()

    #Match API response data for latitude and longitude passed in get request
    assert str(weather_data['coord']['lat']) == str(latitude),f'latitude {latitude} mismatched in API response'
    assert str(weather_data['coord']['lon']) == str(longitude), f'longitude {longitude} mismatched in API response'
    print(f"Latitude {latitude} matched with API Data {weather_data['coord']['lat']}")
    print(f"Longitude {longitude} matched with API Data {weather_data['coord']['lon']}")




