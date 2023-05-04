import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.166.76.39', 8500)
s.connect(server_address)


def printHex(data):
    print(' '.join('{:02x}'.format(x) for x in data))


# to initiate connection
command = bytes.fromhex('00 04 fd f9')
s.send(command)
data = s.recv(1024)                         # response: 00 04 00 00
printHex(data)

# to query IN_1 with nominal val LOW
command = bytes.fromhex('00 08 41 60 00 00 01 28')
s.send(command)
data = s.recv(1024)
printHex(data)

command = bytes.fromhex('00 05 f0 15 e0')
s.send(command)
data = s.recv(1024)                         # response 00 08 00 00 00 00 00 08
printHex(data)


# to query IN_1 with nominal val High
command = bytes.fromhex('00 08 41 60 00 01 01 29')
s.send(command)
data = s.recv(1024)
printHex(data)

command = bytes.fromhex('00 05 f0 15 e0')
s.send(command)
data = s.recv(1024)                         # response 00 08 00 00 00 00 00 08
printHex(data)

"""
# to set OUT_4 LOW and OUT_3 HIGH for OK signal
command = bytes.fromhex('00 08 41 10 03 00 01 5b')
s.send(command)
data = s.recv(1024)
printHex(data)

command = bytes.fromhex('00 05 f0 15 e0')
s.send(command)
data = s.recv(1024)                         # response 00 08 00 00 00 00 00 08
printHex(data)

command = bytes.fromhex('00 08 41 10 02 01 01 5b')
s.send(command)
data = s.recv(1024)
printHex(data)

command = bytes.fromhex('00 05 f0 15 e0')
s.send(command)
data = s.recv(1024)                         # response 00 08 00 00 00 00 00 08
printHex(data)

"""
s.close()
