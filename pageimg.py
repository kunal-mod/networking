import time
import socket
from PIL import Image
import io
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.166.76.39', 8500)

s.connect(server_address)

command = bytes.fromhex('00 04 fd f9')
s.send(command)
data = s.recv(1024)
print(data.decode("utf-8"))

command = bytes.fromhex('00 09 05 ff 03 03 03 03 f3')
s.send(command)
data = s.recv(1024)
print(data.decode("utf-8"))

command = bytes.fromhex('00 07 a0 1a ff 00 42')
s.send(command)
data = s.recv(1024)

image_data = b''
chunk_size = 1460
while True:
    chunk = s.recv(chunk_size)
    x = len(chunk)
    print(len(chunk))
    # if (x < 100):
    #     break
    image_data += chunk
    if (x < 110 and x > 100):
        print(chunk.hex())
        break

s.close()

with open('pageimg.bin', 'wb') as f:
    f.write(image_data)

with open('pageimg.bin', 'rb') as f:
    pixel_data = f.read()
width = 1600
height = 1200
image = Image.frombytes('L', (width, height), pixel_data)
image.save('pageimg3.png')
image.show()
