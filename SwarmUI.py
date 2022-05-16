from PyQt6 import QtCore, QtWidgets
from DroneButton import DroneButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, swarm):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(710, 288)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.upButton.setObjectName("upButton")
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(10, 90, 71, 71))
        self.downButton.setObjectName("downButton")
        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setGeometry(QtCore.QRect(90, 10, 81, 71))
        self.forwardButton.setObjectName("forwardButton")
        self.backwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.backwardButton.setGeometry(QtCore.QRect(90, 90, 81, 71))
        self.backwardButton.setObjectName("backwardButton")
        self.leftButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftButton.setGeometry(QtCore.QRect(180, 10, 81, 71))
        self.leftButton.setObjectName("leftButton")
        self.rightButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightButton.setGeometry(QtCore.QRect(180, 90, 81, 70))
        self.rightButton.setObjectName("rightButton")
        self.cwButton = QtWidgets.QPushButton(self.centralwidget)
        self.cwButton.setGeometry(QtCore.QRect(270, 10, 81, 71))
        self.cwButton.setObjectName("cwButton")
        self.ccwButton = QtWidgets.QPushButton(self.centralwidget)
        self.ccwButton.setGeometry(QtCore.QRect(270, 90, 81, 71))
        self.ccwButton.setObjectName("ccwButton")
        self.takeoffButton = QtWidgets.QPushButton(self.centralwidget)
        self.takeoffButton.setGeometry(QtCore.QRect(360, 150, 161, 70))
        self.takeoffButton.setObjectName("takeoffButton")
        self.landButton = QtWidgets.QPushButton(self.centralwidget)
        self.landButton.setGeometry(QtCore.QRect(530, 150, 171, 70))
        self.landButton.setObjectName("landButton")
        self.XLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.XLineEdit.setGeometry(QtCore.QRect(100, 196, 81, 20))
        self.XLineEdit.setObjectName("XLineEdit")
        self.XLabel = QtWidgets.QLabel(self.centralwidget)
        self.XLabel.setGeometry(QtCore.QRect(14, 200, 47, 13))
        self.XLabel.setObjectName("XLabel")
        self.AngleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AngleEdit.setGeometry(QtCore.QRect(260, 170, 91, 20))
        self.AngleEdit.setObjectName("AngleEdit")
        self.AngleLabel = QtWidgets.QLabel(self.centralwidget)
        self.AngleLabel.setGeometry(QtCore.QRect(190, 170, 51, 16))
        self.AngleLabel.setObjectName("AngleLabel")
        self.UpDownEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UpDownEdit.setGeometry(QtCore.QRect(100, 168, 81, 20))
        self.UpDownEdit.setObjectName("UpDownEdit")
        self.UpDownLabel = QtWidgets.QLabel(self.centralwidget)
        self.UpDownLabel.setGeometry(QtCore.QRect(13, 170, 81, 16))
        self.UpDownLabel.setObjectName("UpDownLabel")
        self.commandButton = QtWidgets.QPushButton(self.centralwidget)
        self.commandButton.setGeometry(QtCore.QRect(360, 60, 161, 81))
        self.commandButton.setObjectName("commandButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(530, 60, 171, 81))
        self.stopButton.setObjectName("stopButton")
        self.queryToAllLabel = QtWidgets.QLabel(self.centralwidget)
        self.queryToAllLabel.setGeometry(QtCore.QRect(360, 10, 111, 16))
        self.queryToAllLabel.setObjectName("queryToAllLabel")
        self.sendCommandToAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendCommandToAllButton.setGeometry(QtCore.QRect(620, 28, 75, 23))
        self.sendCommandToAllButton.setObjectName("sendCommandToAllButton")
        self.queryToAllEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryToAllEdit.setGeometry(QtCore.QRect(360, 30, 251, 20))
        self.queryToAllEdit.setObjectName("queryToAllEdit")
        self.delayLabel = QtWidgets.QLabel(self.centralwidget)
        self.delayLabel.setGeometry(QtCore.QRect(189, 197, 51, 16))
        self.delayLabel.setObjectName("delayLabel")
        self.delayEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.delayEdit.setGeometry(QtCore.QRect(260, 196, 91, 20))
        self.delayEdit.setObjectName("delayEdit")

        started_position = 10
        increment = 80
        index = 1

        for drone in swarm.get_all_drones():
            button = DroneButton(drone, started_position, 230, 71, 51, index, centralwidget=self.centralwidget)
            self.drone_buttons.append(button)

            started_position += increment
            index += 1

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tello Drones Swarm"))
        self.upButton.setText(_translate("MainWindow", "Вверх +X"))
        self.downButton.setText(_translate("MainWindow", "Вниз -X"))
        self.forwardButton.setText(_translate("MainWindow", "Вперед +X"))
        self.backwardButton.setText(_translate("MainWindow", "Назад +X"))
        self.leftButton.setText(_translate("MainWindow", "Влево +X"))
        self.rightButton.setText(_translate("MainWindow", "Вправо +X"))
        self.cwButton.setText(_translate("MainWindow", "CW Angle"))
        self.ccwButton.setText(_translate("MainWindow", "CCW Angle"))
        self.takeoffButton.setText(_translate("MainWindow", "Взлет"))
        self.landButton.setText(_translate("MainWindow", "Посадка"))
        self.XLineEdit.setText(_translate("MainWindow", "100"))
        self.XLabel.setText(_translate("MainWindow", "X"))
        self.AngleEdit.setText(_translate("MainWindow", "90"))
        self.AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.UpDownEdit.setText(_translate("MainWindow", "100"))
        self.UpDownLabel.setText(_translate("MainWindow", "X Вверх/Вниз"))
        self.commandButton.setText(_translate("MainWindow", "Командный режим"))
        self.stopButton.setText(_translate("MainWindow", "Зависание в воздухе"))
        self.queryToAllLabel.setText(_translate("MainWindow", "Запрос ко всем"))
        self.sendCommandToAllButton.setText(_translate("MainWindow", "Отправить"))
        self.queryToAllEdit.setText(_translate("MainWindow", "battery?"))
        self.delayLabel.setText(_translate("MainWindow", "Delay"))
        self.delayEdit.setText(_translate("MainWindow", "0.5"))
