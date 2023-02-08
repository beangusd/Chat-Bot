import socket
host = "shhh"
port = 12423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen()
conn, addr = s.accept()

print(conn)
print(addr)

