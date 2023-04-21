import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(5)

hex_string = "57656c636f6d6520746f2074686520736572766572"
byte_string = bytes.fromhex(hex_string)

clientsocket, address = s.accept()
print(f'Connected by {address}')

while True:
    msg = clientsocket.recv(1024)
    if "close" in msg.decode("utf-8"):
        break
    clientsocket.send(bytes("Welcome to the server", "utf-8"))

clientsocket.close()
