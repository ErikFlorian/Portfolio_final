import socket

s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(2)

print("čekám na 2 klienty...")
c1, _ = s.accept()
c2, _ = s.accept()

print("spojeno")

while True:
    data = c1.recv(4096)
    if not data:
        break
    c2.sendall(data)
