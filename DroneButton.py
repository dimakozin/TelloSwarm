from PyQt6 import QtWidgets, QtCore

class DroneButton:
    """ Класс-обертка кнопки дрона """
    def __init__(self, drone, x, y, height, width, index, centralwidget):
        self.drone = drone
        self.index = index
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.button = QtWidgets.QPushButton(centralwidget)
        self.button.setGeometry(QtCore.QRect(x, 230, 71, 51))
        self.button.setObjectName("droneConsoleButton_" + str(index))
        self.button.setText("Дрон " + str(index))
        self.button.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        self.drone.is_selected = not self.drone.is_selected

        if self.drone.is_selected:
            style = "background-color: red"
        else:
            style = ""

        self.button.setStyleSheet(style)
