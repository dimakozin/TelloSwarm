import os
import json

interfaces = os.listdir('/sys/class/net')
interfaces.remove('lo')

data = {}

for interface in interfaces:
    data[interface] = ['192.168.10.1']

with open('interfaces.json', 'w') as file:
    file.writelines(json.dumps(data))
