import requests

def get_ip_address():
    """Return the public IP address of our computer."""
    url = 'https://api.ipify.org/'
    response = requests.get(url)
    return response.text


def get_geolocation(ip_address):
    """Return geolocation (latititud and longitud) of the IP address."""
    url = f'https://ipinfo.io/{ip_address}'
    response = requests.get(url)
    return response.json()['loc'].split(',')


def get_weather(lat, lon):
    """Return weather temperature in celsius for a given set of coordinates."""
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
    params = {'lat': lat, 'lon': lon}
    response = requests.get(url, params=params)
    return response.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']


def weather_at_server():
    ip_address = get_ip_address()
    lat, lon = get_geolocation(ip_address)
    temp_celsius = get_weather(lat, lon)
    
    return f"""
        Hello, <br>
        At the location ({lat}, {lon}) of this App Server IP address ({ip_address}), the temperature is {temp_celsius} °C.
    """

def weather_at_client(ip_address):
    lat, lon = get_geolocation(ip_address)
    temp_celsius = get_weather(lat, lon)
    
    return f"""
        Hello, <br>
        At your IP address {ip_address}, located at ({lat}, {lon}), the temperature is {temp_celsius} °C
    """


if __name__ == '__main__':
    print(weather_at_server().replace('<br>',''))