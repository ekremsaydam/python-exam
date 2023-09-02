import datetime
import socket
import sys
from _thread import start_new_thread


def client_thread(connection: socket.socket, clientAddress: tuple):
    connection.sendall('welcome to the server'.encode('utf-8'))
    while True:
        data = connection.recv(2048)
        if not data or data.decode('utf-8').upper() == 'END':
            break

        client_info = '{0} {1} - data : {2}'.format(
            f'[{clientAddress[0]}:{clientAddress[1]}]',
            datetime.datetime.now(),
            data.decode("utf-8"))

        print(client_info)
        reply = 'server says: ' + data.decode('utf-8')
        connection.sendall(reply.encode('utf-8'))

    connection.close()
    print(f"[{clientAddress[0]}:{clientAddress[1]}] - \
{datetime.datetime.now()} - Client disconnected...")


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 1233
    clients = set()
    ThreadCount = 0

    server_socket = socket.socket()

    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(f'An error occurred while binding: {e}')
        sys.exit()

    server_socket.listen(5)
    print("Waiting for a Connection...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.add((client_socket, client_address))

        print(f'[{client_address[0]}:{client_address[1]}] - \
    {datetime.datetime.now()} Connected to the server.')
        start_new_thread(client_thread, (client_socket, client_address))
        ThreadCount += 1
        print(f'Thread Number: {ThreadCount}')

    server_socket.close()
