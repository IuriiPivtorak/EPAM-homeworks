import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import requests
from nominatim import Nominatim


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
                hours = 3
                j = 0
                while j < len(data_2['list']):
                    print('weather forecast for {} hours in {}: {}'.format(hours, location,
                                                                           data_2['list'][j]['weather'][0][
                                                                               'description']))
                    print(*data_2['list'][j]['main'].items())
                    j += 1
                    hours += 3
        else:
            raise NameError('no such location found!')
    else:
        raise TypeError('"location" should be of type str')


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


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Input location for weather report'
        self.left = 400
        self.top = 400
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Make forecast', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxvalue = self.textbox.text()
        sys.stdout = open('results.txt', 'w')
        nominatim_weather(textboxvalue, 'b4a9d8e16b916107e741f1e84440c660')
        sys.stdout = sys.__stdout__
        with open('results.txt') as file:
            lines = file.readlines()
            result = ''
            for line in lines:
                result += str(line)
            QMessageBox.question(self, 'Weather forecast', result, QMessageBox.Ok,
                                 QMessageBox.Ok)
            self.textbox.setText('')
        os.remove('results.txt')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



#app = QApplication(sys.argv)
#text, ok = QInputDialog.getText(None, 'name', 'enter your name:')
#print(text)
#sys.exit()
