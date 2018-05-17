import hashlib
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def comparison(*args):
    """
    Hashes files and prints number of same files
    with their names.
    :param args: names of files.
    :type args: str.
    :returns: list of lists -- number of same files with their names.
    """
    my_list = {}
    try:
        for arg in args:
            with open(arg, 'rb') as file:
                hasher = hashlib.md5()
                buf = file.read()
                hasher.update(buf)
                data = hasher.hexdigest()
                if data in my_list.keys():
                    my_list[data].append(str(arg))
                else:
                    my_list[data] = [arg]
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist!')
    result = []
    for i in my_list.values():
        x = len(i)
        result.append([x, [j for j in i]])
    for res in sorted(result, reverse=True):
        print('{} file(s): {}'.format(res[0], res[1]))
    return result

    with open('aaa.txt', 'w') as file:
        print('who', file=file)

    with open('bbb.txt', 'w') as file:
        print('who', file=file)

    with open('ccc.txt', 'w') as file:
        print('it is different file.', file=file)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Input file names with "space" to compare:'
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
        self.button = QPushButton('Make comparison', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxvalue = self.textbox.text()
        files = [str(s) for s in textboxvalue.split()]
        sys.stdout = open('results.txt', 'w')
        comparison(*files)
        sys.stdout = sys.__stdout__
        with open('results.txt') as file_2:
            lines = file_2.readlines()
            result = ''
            for line in lines:
                result += str(line)
            QMessageBox.question(self, 'Files comparison', result, QMessageBox.Ok,
                                 QMessageBox.Ok)
            self.textbox.setText('')
        os.remove('results.txt')


if __name__ == '__main__':

    with open('aaa.txt', 'w') as file:
        print('who', file=file)
    with open('bbb.txt', 'w') as file:
        print('who', file=file)
    with open('ccc.txt', 'w') as file:
        print('it is different file.', file=file)

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())