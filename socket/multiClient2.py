import socket
import sys
import threading


def receive():
    print('reveice started')
    while True:
        try:
            data = client_socket.recv(1024)
        except socket.error as error:
            print(f'An error occurred : {error}')
            break

        if not data:
            break

        print(data.decode('utf-8'))

    client_socket.close()


def send():
    print('send started')
    while True:
        message = f'{input("Mesajınız :")}'
        if message.upper() == 'END':
            break
        client_socket.send(message.encode('utf-8'))

    # client_socket.close()
    # print('Connection closed')
    # client_socket.shutdown(socket.SHUT_RDWR)
    # print('Connection shutdown')
    # sys.exit()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(f'An error occurred while connecting: {e}')
        sys.exit()

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()
