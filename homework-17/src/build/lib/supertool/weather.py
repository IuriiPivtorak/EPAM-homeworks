"""
Weather report module

"""

import requests
from nominatim import Nominatim


def weather(location, token_id):
    """
    Downloads current weather info for location.

    :param location: location to search weather for.
    :type location: str.
    :param token_id: user's token for website.
    :type token_id: str.
    :returns: None. Prints weather data.
    """
    url = 'http://api.openweathermap.org/data/2.5/weather'
    querystring = {
        'q': location,
        'appid': token_id
    }
    response = requests.request('GET', url, params=querystring)
    data = response.json()
    if data == {'cod': '404', 'message': 'city not found'}:
        raise NameError('Input location name correctly!')
    elif data == {'cod': 401,
                  'message': 'Invalid API key. '
                             'Please see http://openweathermap.org/faq#error401'
                             ' for more info.'}:
        raise NameError('You have inputted invalid token id!')
    else:
        print('weather in {}: {}'.format(
            location, data['weather'][0]['description']))
        for i in data['main'].items():
            print('{}: {}'.format(i[0], i[1]))


def weather_forecast(location, token_id):
    """
    Downloads forecast for 3 hours for location.

    :param location: location to search forecast for.
    :type location: str.
    :param token_id: user's token for website.
    :type token_id: str.
    :returns: None. Prints weather data.
    """
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    querystring = {
        'q': location,
        'appid': token_id
    }

    response = requests.request('GET', url, params=querystring)
    data = response.json()
    if data == {'cod': '404', 'message': 'city not found'}:
        raise NameError('Input location name correctly!')
    elif data == {'cod': 401,
                  'message': 'Invalid API key. '
                             'Please see http://openweathermap.org/faq#error401'
                             ' for more info.'}:
        raise NameError('You have inputted invalid token id!')
    else:
        hours = 3
        j = 0
        while j < len(data['list']):
            print('weather forecast for {} hours in {}: {}'.format(hours, location,
                                                                   data['list'][j]['weather'][0]['description']))
            print(*data['list'][j]['main'].items())
            j += 1
            hours += 3


def nominatim_weather(location, token_id):
    """
    Downloads current weather and 3 hour forecast for location.

    :param location: location to search forecast for.
    :type location: str.
    :param token_id: user's token for website.
    :type token_id: str.
    :returns: None. Prints weather data.
    """
    if type(location) == str:
        nom = Nominatim()
        coordinates = nom.query(location)
        if coordinates:
            lat = coordinates[0]['lat']
            lon = coordinates[0]['lon']

            url = 'http://api.openweathermap.org/data/2.5/weather'
            token = token_id
            querystring = {
                'lat': lat,
                'lon': lon,
                'appid': token
            }
            response = requests.request('GET', url, params=querystring)
            data = response.json()
            if data == {'cod': 401, 'message': 'Invalid API key. '
                                               'Please see http://openweathermap.org/faq#error401 '
                                               'for more info.'}:
                raise NameError('You have inputted invalid token id!')
            else:
                print('weather in {}: {}'.format(
                    location, data['weather'][0]['description']))
                for i in data['main'].items():
                    print('{}: {}'.format(i[0], i[1]))

                url_2 = 'http://api.openweathermap.org/data/2.5/forecast'
                response_2 = requests.request('GET', url_2, params=querystring)
                data_2 = response_2.json()
                days = 5
                j = 39
                while j < len(data_2['list']):
                    print('weather forecast for {} days in {}: {}'.format(days, location,
                                                                           data_2['list'][j]['weather'][0][
                                                                               'description']))
                    for i in data_2['list'][j]['main'].items():
                        print('{}: {}'.format(i[0], i[1]))
                    j += 1
        else:
            raise NameError('no such location found!')
    else:
        raise TypeError('"location" should be of type str')
