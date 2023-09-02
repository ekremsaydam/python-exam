import socket
import sys
try:
    client_socket = socket.socket(family=socket.AF_INET,
                                  type=socket.SOCK_DGRAM,
                                  proto=0)
except socket.error as err:
    print(f"socket creation failed with error {str(err)}")
    sys.exit()

print("Socket successfully created")
message = "Hey server"
client_socket.sendto(message.encode('utf-8'), ('127.0.0.1', 1234))
data, server_addr = client_socket.recvfrom(4096)
print(f"received from server {server_addr[0]}:{server_addr[1]}: {data.decode('utf-8')}")
client_socket.close()
