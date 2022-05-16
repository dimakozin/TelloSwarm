# -----------------------------------------------------------
# @author dimakozin <dimakozin@gmail.com>
# @date 04.10.2021
# @version 1.0.0
# GUI для управления стаей дронов Tello + Tello EDU
#
#
# (C) 2021 Dmitry Kozin, Moscow, Russia
# -----------------------------------------------------------


import sys
import json
from PyQt6 import QtGui, QtWidgets

import SwarmUI

from TelloSwarm import TelloSwarm
from TelloDrone import TelloDrone


def main():
    with open("interfaces.json") as file:
        interfaces = json.load(file)

    swarm = TelloSwarm()
    for interface in interfaces.keys():
        for IP in interfaces[interface]:
            swarm.add_to_swarm(TelloDrone(interface=interface, IP=IP))

    app = QtWidgets.QApplication(sys.argv)
    window = SwarmApp(swarm=swarm)
    window.show()
    app.exec()


class SwarmApp(QtWidgets.QMainWindow, SwarmUI.Ui_MainWindow):
    def __init__(self, swarm):
        super().__init__()
        self.swarm = swarm
        self.drone_buttons = []
        self.setupUi(self, self.swarm)

        self.upButton.clicked.connect(self.upButtonClicked)
        self.downButton.clicked.connect(self.downButtonClicked)
        self.forwardButton.clicked.connect(self.forwardButtonClicked)
        self.backwardButton.clicked.connect(self.backwardButtonClicked)
        self.leftButton.clicked.connect(self.leftButtonClicked)
        self.rightButton.clicked.connect(self.rightButtonClicked)
        self.cwButton.clicked.connect(self.cwButtonClicked)
        self.ccwButton.clicked.connect(self.ccwButtonClicked)
        self.takeoffButton.clicked.connect(self.takeoffButtonClicked)
        self.landButton.clicked.connect(self.landButtonClicked)
        self.commandButton.clicked.connect(self.commandButtonClicked)
        self.stopButton.clicked.connect(self.stopButtonClicked)
        self.sendCommandToAllButton.clicked.connect(self.queryToAllButtonClicked)
        self.delayEdit.textChanged.connect(self.onDelayChange)

    def upButtonClicked(self):
        """  Событие при клике на кнопку Вверх """
        self.swarm.send_command("up " + self.UpDownEdit.text())

    def downButtonClicked(self):
        """  Событие при клике на кнопку Вниз """
        self.swarm.send_command("down " + self.UpDownEdit.text())

    def forwardButtonClicked(self):
        """  Событие при клике на кнопку Вперед """
        self.swarm.send_command("forward " + self.XLineEdit.text())

    def backwardButtonClicked(self):
        """  Событие при клике на кнопку Назад """
        self.swarm.send_command("backward " + self.XLineEdit.text())

    def leftButtonClicked(self):
        """  Событие при клике на кнопку Влево """
        self.swarm.send_command("left " + self.XLineEdit.text())

    def rightButtonClicked(self):
        """  Событие при клике на кнопку Вправо """
        self.swarm.send_command("right " + self.XLineEdit.text())

    def cwButtonClicked(self):
        """  Событие при клике на кнопку Поворот по часовой стрелке """
        self.swarm.send_command("cw " + self.AngleEdit.text())

    def ccwButtonClicked(self):
        """  Событие при клике на кнопку Против часовой стрелки """
        self.swarm.send_command("ccw " + self.AngleEdit.text())

    def takeoffButtonClicked(self):
        """  Событие при клике на кнопку Взлет """
        self.swarm.send_command("takeoff")

    def landButtonClicked(self):
        """  Событие при клике на кнопку Посадка """
        self.swarm.send_command("land")

    def commandButtonClicked(self):
        """  Событие при клике на кнопку Командный режим """
        self.swarm.send_command("command")

    def stopButtonClicked(self):
        """
        Событие при клике на кнопку Зависание в воздухе
        ВНИМАНИЕ: данная команда не поддерживается дронами Tello SDK 1.0
        """
        self.swarm.send_command("stop")

    def queryToAllButtonClicked(self):
        """  Событие при клике на кнопку "Отправить" (на все дроны) """
        self.swarm.send_command(self.queryToAllEdit.text())

    def onDelayChange(self):
        """  Событие при изменении времени задержки """
        try:
            delay = float(self.delayEdit.text())
            if delay == 0.0:
                return
            self.swarm.set_delay(delay)
        except ValueError:
            pass


if __name__ == '__main__':
    main()
