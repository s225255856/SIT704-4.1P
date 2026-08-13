import socket

server = '192.168.1.112'
port = 110
username = 'ustest'
password = 'test'
buffer = "A"*108
while len(buffer) <= 4000:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        response = s.recv(1024).decode()
        s.sendall(f'USER {username}\r\n'.encode())
        response = s.recv(1024).decode()
        s.sendall(f'PASS {password}\r\n'.encode())
        response = s.recv(1024).decode()
        s.close()
        print("\n Done!")

    except socket.error as e:
        print(f"Socket error {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")