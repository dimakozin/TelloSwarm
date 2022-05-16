# -----------------------------------------------------------
# @author dimakozin <dimakozin@gmail.com>
# @date 01.10.2021
# @version 0.0.1
# Модуль управления дронами Tello (Tello EDU)
#
#
# (C) 2021 Dmitry Kozin, Moscow, Russia
# -----------------------------------------------------------

import socket
if not hasattr(socket,'SO_BINDTODEVICE'):
    socket.SO_BINDTODEVICE = 25

import threading
from datetime import datetime


class TelloDrone:
    """ Класс-обертка для более простого управления дроном """

    def __init__(self, interface, IP="192.168.10.1", udp_port=8889, command_timeout=.3, transmitter_logger=print,
                 receiver_logger=print):
        """
            Конструктор дрона. Создает подключение, проверяет, что дрон подключен и готов к работе

            :param interface: интерфейс, по которому будет отправлен запрос на дрон
            :param IP: IP-адрес дрона. Для Tello - в его сети, по умолчанию адресс 192.168.10.1;
            Tello EDU может быть настроен в другой сети (см. комманда ap <Wi-Fi сеть> <пароль от сети>)
            :param udp_port: порт, по которому отправляются запросы на дрон (по умолчанию 8889)
            :param command_timeout: задержка между отправкой комманд
        """
        self.IP = IP
        self.port = udp_port
        self.interface = interface

        self.is_selected = False

        self.command_timeout = command_timeout
        self.transmitter_logger = transmitter_logger
        self.receiver_logger = receiver_logger

        self.response = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # общаемся по IP, через UDP
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, bytes(interface, 'UTF-8'))

        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True

        self.receive_thread.start()
        self.abort_flag = False

    def send_command(self, command):
        """
            Отправка команды на дрон

            :param command: команда для дрона
            :return: ответ на команду от дрона

        """
        self.abort_flag = False
        timer = threading.Timer(self.command_timeout, self.set_abort_flag)

        self.socket.sendto(command.encode('utf-8'), (self.IP, self.port))

        now = datetime.now()
        self.transmitter_logger("[%s] Command: %s" % (now.strftime("%H:%M:%S"), command))

        timer.start()

    def _receive_thread(self):
        """Слушатель ответов от дрона
        Запускает поток-слушатель ответов.

        :return: ответ от дрона

        """
        while True:
            try:
                self.response, ip = self.socket.recvfrom(256)

                now = datetime.now()
                self.receiver_logger("[%s] Response: %s" % (now.strftime("%H:%M:%S"), self.response))
            except Exception:
                break

    def set_abort_flag(self):
        """Устанавливает флаг выполнения команды в значение False
            Выполняется в случае, если не получен ответ от дрона
        """

        self.abort_flag = True

    def set_transmitter_logger(self, transmitter_logger):
        """Назначает логгирование при отправке сообщений дрону
            :params transmitter_logger: функция логгирования сообщения
        """
        self.transmitter_logger = transmitter_logger

    def set_receiver_logger(self, receiver_logger):
        """Назначает логгирование при получении сообщений дрону
            :params receiver_logger: функция логгирования сообщения
        """
        self.receiver_logger = receiver_logger
