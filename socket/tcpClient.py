import socket
import sys

# Create a TCP/IP socket
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f"socket creation failed with error {str(err)}")
    sys.exit()

client_socket.connect(('127.0.0.1', 1234))
payload = 'Hey server'
try:
    while True:
        # client_socket.sendall(bytes(payload, 'utf-8'))
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"received from server {data.decode('utf-8')}")
        payload = input("Enter a new payload: ")
        if payload.upper() == 'END':
            break
except socket.error as err:
    print(f"send failed with error {str(err)}")
    sys.exit()

client_socket.close()
