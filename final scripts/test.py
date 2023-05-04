import time
import socket
from PIL import Image

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


# to initiate connection
command = bytes.fromhex('00 04 fd f9')
s.send(command)
data = s.recv(1024)                         # response: 00 04 00 00
printHex(data)

command = bytes.fromhex('00 0b 07 00 04 00 03 0d 40 00 46')
s.send(command)
printHex(data)
querySuccess()

# time.sleep(1)

# # set page
command = bytes.fromhex('00 09 05 ff 02 02 02 02 f3')
s.send(command)
data = s.recv(1024)
printHex(data)
querySuccess()

# grab image
# command = bytes.fromhex('00 06 01 00 01 06')
# s.send(command)
# data = s.recv(1024)
# printHex(data)

# capture
command = bytes.fromhex('00 07 a0 1a ff 00 42')
s.send(command)
data = s.recv(1024)
printHex(data)

# assemble
image_data = b''
chunk_size = 1460
while True:
    chunk = s.recv(chunk_size)
    x = len(chunk)
    print(len(chunk))
    # if (x < 100):
    #     break
    image_data += chunk
    if (x == 104):
        break

s.close()

with open('pageimage.bin', 'wb') as f:
    f.write(image_data)

with open('pageimage.bin', 'rb') as f:
    pixel_data = f.read()
width = 1600
height = 1200
image = Image.frombytes('L', (width, height), pixel_data)
image.save('boschimg.bmp')
image.show()
