import socket
import sys
import threading


def receive(client_socket, client_address):
    print('receive started')
    while True:
        try:
            data = client_socket.recv(1024)
        except socket.error as error:
            print(f'An error occurred : {error}')
            break

        print(data.decode('utf-8'))

    server_socket.close()


def send():
    while True:
        message = input("Server message : ")
        for client in clients:
            client.sendall(message.encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 1234
    clients = set()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(f'An error occurred while binding: {e}')
        sys.exit()

    print('Waiting for a Connection...')
    server_socket.listen()
    print("Server is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established!")

        clients.add((client_socket))
        send_thread = threading.Thread(target=send)
        send_thread.start()

        receive_thread = threading.Thread(
            target=receive, args=(client_socket, client_address))
        receive_thread.start()

    # send_thread = threading.Thread(target=send)
    # send_thread.start()
