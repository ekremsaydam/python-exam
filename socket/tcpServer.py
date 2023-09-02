import socket
import sys

try:
    server_socket = socket.socket(
        socket.AF_INET,            # set protocol family to 'Internet' (INET)
        socket.SOCK_STREAM,        # set protocol type to 'TCP' (SOCK_STREAM)
        proto=0                    # set the default protocol (for TCP it's IP)
    )
except socket.error as err:
    print(f"socket creation failed with error {str(err)}")
    sys.exit()

print("Socket successfully created")

# Use '127.0.0.1' to bind to localhost
# Use '0.0.0.0' or '' to bind to ALL network interfaces simultaneously
# Use an actual IP of an interface to bind to a specific address.
# socket.gethostname()
server_socket.bind(('127.0.0.1', 1234))

backlog = 5  # the max number of queued connections
server_socket.listen(backlog)

while True:
    print("Waiting for a connection...")

    # Accept client connection
    client_socket, client_addr = server_socket.accept()

    print(f"Got a connection from {client_addr}")
    while True:
        data = client_socket.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break

        print(
            f"received from client - {client_addr[0]}:{client_addr[1]} \
- data: {data.decode('utf-8')}")
        try:
            client_socket.sendall(bytes('Hey client', 'utf-8'))
        except socket.error as err:
            print(f"send failed with error {str(err)}")
            sys.exit()

    client_socket.close()
    print("Client disconnected...")
server_socket.close()
