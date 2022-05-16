# -----------------------------------------------------------
# @author dimakozin <dimakozin@gmail.com>
# @date 30.09.2021
# @version 1.0.0
# Код управления стаей дронов Tello + Tello EDU
# Обязательно необходимо прописать, по какому интерфейсу идет работа с дроном
# Дроны Tello нельзя соединить в одну Wi-Fi сеть - на каждый дрон свой Wi-Fi адаптер
# Наименование интерфейса прописывается в объекте Drones
#
#
# (C) 2021 Dmitry Kozin, Moscow, Russia
# -----------------------------------------------------------

import time
from TelloDrone import TelloDrone

class TelloSwarm:
    """ Класс-обертка по отправке команд на стаю дронов Tello + Tello EDU """
    def __init__(self, delay=.3):
        self.drones = []
        self.delay = delay

    def set_delay(self, delay):
        """
            Установка задержки между отправкой команд
            :param delay: задержка (в секундах)
        """
        self.delay = delay

    def send_command(self, command):
        """
            Отправка командов стае дронов
            :param command: отправляемая команда
        """
        selected_drones = []

        for drone in self.drones:
            if drone.is_selected:
                selected_drones.append(drone)

        if not selected_drones:
            selected_drones = self.drones

        for drone in selected_drones:
            drone.send_command(command)
            time.sleep(self.delay)

    def add_to_swarm(self, drone):
        """
            Добавляет объект класса TelloDrone в стаю
            :param drone: объект класса TelloDrone
        """
        if not isinstance(drone, TelloDrone):
            raise RuntimeError("Нельзя добавлять в стаю дронов не дроны Tello")
        self.drones.append(drone)

    def get_all_drones(self):
        """
            :returns: все дроны в стае
        """
        return self.drones
