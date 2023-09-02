import socket
import sys

# Create a UDP socket
try:
    server_socket = socket.socket(family=socket.AF_INET,
                                  type=socket.SOCK_DGRAM,
                                  proto=0)
except socket.error as err:
    print(f"socket creation failed with error {str(err)}")
    sys.exit()

print("Socket successfully created")

server_socket.bind(('127.0.0.1', 1234))
print("Listening UDP on port 1234")

while True:
    data, client_addr = server_socket.recvfrom(4096)
    print(f"received from client - {client_addr[0]}:{client_addr[1]} \
- {data.decode('utf-8')}")
    message = "Hello I Am UDP Server"
    server_socket.sendto(message.encode('utf-8'), client_addr)
