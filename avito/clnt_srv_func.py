import socket
import matrix
def connect():
    SERVER = "127.0.0.1"
    PORT = 8000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    client.sendall(bytes("This is from Client",'UTF-8'))
    while True:
        in_data = client.recv(1024)
        print("From Server :" ,in_data.decode())
        out_data = input()
        client.sendall(bytes(out_data,'UTF-8'))
        if out_data=='bye':
           break
    client.close()
    return in_data.decode()
"""
matrix.scrap(in_data.decode())
print(matrix, len(matrix))
print(read_matrix(matrix, len(matrix)))
"""
