import socket
import sys

# Create a TCP/IP socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f"socket creation failed with error {str(err)}")
    sys.exit()

print("Socket successfully created")

target_host = input("Enter a host to connect to: ")
target_port = input("Enter the target port: ")

try:
    sock.connect((target_host, int(target_port)))
    print(f"socket connected to {target_host} on port {target_port}")

    # https://www.rfc-editor.org/rfc/rfc2616
    request = f"""GET / HTTP/1.1
Host: {target_host}

"""
    sock.sendall(request.encode('utf-8'))
    response = sock.recv(4096)
    print(response.decode('utf-8'))

    sock.shutdown(2)
except socket.error as err:
    print(f"connection failed with error {str(err)}")
    sys.exit()
