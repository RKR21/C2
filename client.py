import socket
import os

def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server
    server_address = ('localhost', 10000)
    print(f'connecting to {server_address}')
    sock.connect(server_address)

    # Send working directory to server
    wd = os.getcwd()
    sock.sendall(wd.encode())

    while True:
        # Receive data
        data = sock.recv(1024)
        print(f'received {data.decode()}')

        # Clean up the connection
        sock.close()


if __name__ == "__main__":
    main()