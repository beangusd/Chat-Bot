import socket
host = "192.168.1.4"
port = 12423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen()
conn, addr = s.accept()

print(conn)
print(addr)

