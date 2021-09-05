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

#Test - Query Weather API using City Name and Country Code
@pytest.mark.zipcode
def test_query_by_zipcode_country_code():
    # Query weather API using Zip Code and Country Code
    zip_code = input("Enter the Zip Code to check weather")
    print('Zip Code entered: {zc}'.format(zc=zip_code))

    # Enter the Country Code
    country_code = input("Enter the Country Code to check weather")
    print('Country Code entered: {cc}'.format(cc=country_code))

    # Query using the Zip Code and Country Code
    uri = base_uri + '?q='+ zip_code.lower() + ","+ country_code.lower() + "&appid=" + api_key
    print(f'Query Weather API using Zip Code {zip_code} and Country Code {country_code}: {uri}')

    # Search by Zip Code and Country Code
    response = get_response(uri)
    weather_data = response.json()

    # Validate using name attribute - City Name
    city_name = input(f'Enter a City to match with Zip Code {zip_code}')
    print(f"City Name : {weather_data['name']}")
    assert (weather_data["name"]).lower() == city_name.lower(),\
        f"Zip Code {zip_code} mismatch in City Name {weather_data['name']}"
