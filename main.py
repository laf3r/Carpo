#!/usr/bin/python3

import socket
from tqdm import tqdm
from termcolor import colored
from sys import argv

print('-' * 40)
print('[Simple port scanner by laf3r (v 1.2)]')
print('-' * 40)

ports = []
host = str(argv[1])
print('target ip: ', host)
print('Scanning ports-1-65535\n')
for port in tqdm(range(1, 65535 + 1)):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        ports.append(port)
    
    except:
        pass

print('Scan finished')
print(' ' * 20)
for i in ports:
    print(str('Port ') + str('[') + str(colored(i, 'white')) + str('] - ') + str(colored('Open', 'green')))
