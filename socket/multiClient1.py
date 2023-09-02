import socket
import sys

client_socket = socket.socket()

host = '127.0.0.1'
port = 1233

try:
    client_socket.connect((host, port))
except socket.error as e:
    print(str(e))
    sys.exit()

print(f'Connected to server {host}:{port}')
data = client_socket.recv(1024).decode('utf-8')
print(f'Received from server: {data}')

while True:
    message = input('Enter message: ')
    if message.upper() == 'END':
        break
    client_socket.send(message.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(f'Received from server: {data}')

client_socket.close()
