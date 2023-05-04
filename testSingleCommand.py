
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.166.76.39', 8500)

s.connect(server_address)


def printHex(data):
    print(' '.join('{:02x}'.format(x) for x in data))


def querySuccess():
    command = bytes.fromhex('00 05 f0 15 e0')
    s.send(command)
    # response 00 08 00 00 00 00 00 08
    data = s.recv(1024)
    printHex(data)


command = bytes.fromhex('00 04 fd f9')
s.send(command)
data = s.recv(1024)
print(data.decode("utf-8"))
printHex(data)

# set page
command = bytes.fromhex('00 09 05 ff 01 01 01 01 f3')
s.send(command)
data = s.recv(1024)
printHex(data)
querySuccess()
