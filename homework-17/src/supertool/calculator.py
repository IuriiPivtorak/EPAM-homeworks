"""
Calculator interface module

"""

import sys
from PyQt5 import QtGui, QtWidgets
import supertool.calc
import functools


class MainApplication(QtWidgets.QMainWindow):
    """
    Class for calculator with interface

    """
    def __init__(self):
        super(MainApplication, self).__init__()

        # setting UI to open in main window
        self.ui = supertool.calc.Ui_MainWindow()
        self.ui.setupUi(self)

        # attribute to store inputted operations
        self.operation = None

        # attributes to store inputted values
        self.num_1 = None
        self.num_2 = None

        # attribute that checks which value is supposed to be worked with
        self.flag_attr_1 = True

        for i in range(9):
            col = i % 3
            row = i // 3
            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName(f'button_{i}')
            self.ui.gridLayout.addWidget(button, row, col, 1, 1)
            button.setText(str(i+1))

            button.clicked.connect(functools.partial(self.button_pressed, i + 1))

        # reset button
        reset = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        reset.setSizePolicy(sizePolicy)
        reset.setFont(font)
        reset.setObjectName('button_{}'.format('C'))
        reset.setText('C')
        self.ui.gridLayout.addWidget(reset, 0, 4, 1, 1)
        reset.clicked.connect(self.reset)

        # zero button
        zero = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        zero.setSizePolicy(sizePolicy)
        zero.setFont(font)
        zero.setObjectName('button_{}'.format('0'))
        zero.setText('0')
        self.ui.gridLayout.addWidget(zero, 3, 1, 1, 1)
        zero.clicked.connect(self.button_pressed)

        # multiplication button
        mult = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        mult.setSizePolicy(sizePolicy)
        mult.setFont(font)
        mult.setObjectName('button_{}'.format('*'))
        mult.setText('*')
        self.ui.gridLayout.addWidget(mult, 1, 4, 1, 1)
        mult.clicked.connect(self.multiplication)

        # divide button
        divide = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        divide.setSizePolicy(sizePolicy)
        divide.setFont(font)
        divide.setObjectName('button_{}'.format('/'))
        divide.setText('/')
        self.ui.gridLayout.addWidget(divide, 2, 4, 1, 1)
        divide.clicked.connect(self.division)

        # power button
        power = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        power.setSizePolicy(sizePolicy)
        power.setFont(font)
        power.setObjectName('button_{}'.format('^'))
        power.setText('^')
        self.ui.gridLayout.addWidget(power, 0, 5, 1, 1)
        power.clicked.connect(self.power)

        # plus button
        plus = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        plus.setSizePolicy(sizePolicy)
        plus.setFont(font)
        plus.setObjectName('button_{}'.format('+'))
        plus.setText('+')
        self.ui.gridLayout.addWidget(plus, 1, 5, 1, 1)
        plus.clicked.connect(self.plus)

        # substraction button
        minus = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        minus.setSizePolicy(sizePolicy)
        minus.setFont(font)
        minus.setObjectName('button_{}'.format('-'))
        minus.setText('-')
        self.ui.gridLayout.addWidget(minus, 2, 5, 1, 1)
        minus.clicked.connect(self.minus)

        # equality button
        equal = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        equal.setSizePolicy(sizePolicy)
        equal.setFont(font)
        equal.setObjectName('button_{}'.format('='))
        equal.setText('=')
        self.ui.gridLayout.addWidget(equal, 3, 5, 1, 1)
        equal.clicked.connect(self.equal)

    #############################
    # Calculator methods
    #############################

    def button_pressed(self, number):
        """
        Sets what should appear in UI and what changes in attributes
        when buttons 0-9 are clicked by user.

        Until self.flag_attr_1 is set to False, corrects self.num_1,
        else - corrects self.num_2.

        :param number: value from 0 to 9.
        :type number: int.
        :returns: None -- displays in UI pressed number.
        """
        if self.flag_attr_1 is True:
            if self.num_1 is None:
                self.num_1 = number
                self.ui.lcd.display(self.num_1)
            else:
                self.num_1 = int(str(self.num_1) + str(number))
                self.ui.lcd.display(self.num_1)
        elif self.flag_attr_1 is False:
            if self.num_2 is None:
                self.num_2 = number
                self.ui.lcd.display(self.num_2)
            else:
                self.num_2 = int(str(self.num_2) + str(number))
                self.ui.lcd.display(self.num_2)

    def reset(self):
        """
        Sets behavior of reset button.

        :returns: None -- attributes are set to their initial state, '0' is displayed in UI.
        """
        self.operation = None
        self.num_1 = None
        self.num_2 = None
        self.flag_attr_1 = True
        self.ui.lcd.display(0)

    def multiplication(self):
        """
        Sets behavior of multiplication button.

        :returns: None -- changes self.operation and self.flag_attr_1
        """
        self.operation = 1
        self.flag_attr_1 = False

    def division(self):
        """
        Sets behavior of division button.

        :returns: None -- changes self.operation and self.flag_attr_1
        """
        self.operation = 2
        self.flag_attr_1 = False

    def power(self):
        """
        Sets behavior of power button.

        :returns: None -- changes self.operation and self.flag_attr_1
        """
        self.operation = 3
        self.flag_attr_1 = False

    def plus(self):
        """
        Sets behavior of addition button.

        :returns: None -- changes self.operation and self.flag_attr_1
        """
        self.operation = 4
        self.flag_attr_1 = False

    def minus(self):
        """
        Sets behavior of substraction button.

        :returns: None -- changes self.operation and self.flag_attr_1
        """
        self.operation = 5
        self.flag_attr_1 = False

    def equal(self):
        """
        Sets behavior of equality button.
        Checks self.operation and performs operation on value according to it.

        :returns: None -- displays in UI the result of operations and sets result as self.num_1.
        """
        if self.operation == 1:
            self.ui.lcd.display(self.num_1 * self.num_2)
            self.num_1 = self.num_1 * self.num_2
            self.num_2 = None
            self.operation = None
        elif self.operation == 2:
            if self.num_2 != 0:
                self.ui.lcd.display(self.num_1 / self.num_2)
                self.num_1 = self.num_1 / self.num_2
                self.num_2 = None
                self.operation = None
            # if user tries to divide by zero
            else:
                self.ui.lcd.display('---')
                self.num_1 = None
                self.num_2 = None
                self.operation = None
                self.flag_attr_1 = True
        elif self.operation == 3:
            self.ui.lcd.display(self.num_1 ** self.num_2)
            self.num_1 = self.num_1 ** self.num_2
            self.num_2 = None
            self.operation = None
        elif self.operation == 4:
            self.ui.lcd.display(self.num_1 + self.num_2)
            self.num_1 = self.num_1 + self.num_2
            self.num_2 = None
            self.operation = None
        elif self.operation == 5:
            self.ui.lcd.display(self.num_1 - self.num_2)
            self.num_1 = self.num_1 - self.num_2
            self.num_2 = None
            self.operation = None
        elif self.operation is None:
            self.ui.lcd.display(self.num_1)
        elif self.operation is None and self.num_1 is None and self.num_2 is None:
            self.ui.lcd.display('')
