import socket
import time


IPs = [
    '192.168.10.1'
    #    '192.168.31.235',
    #    '192.168.31.187',
    #    '192.168.31.123',
    #    '192.168.31.247',
]
UDP_PORT = 8889

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("==================================")
print("*        DRONE COMMAND MODE      *")
print("==================================")

def send_command(command, delay=0):
    """
        Отправка команды на все дроны

        :param command: Команда, посылаемая на дроны
        :param delay: Задержка между отправкой команд
    """
    for IP in IPs:
        sock.sendto(bytes(command, "UTF-8"), (IP, UDP_PORT))
        time.sleep(delay)
        sock.sendto(bytes(command, "UTF-8"), (IP, UDP_PORT))
        print("Drone %s: %s" % (IP, command))



while True:
    print("Write command:")
    command = input()
    send_command(command)

