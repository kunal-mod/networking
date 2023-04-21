"""# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
# # import cv2
# img = cv2.imread("img1.bmp")
# cv2.imshow("win", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# with open('img1.bmp', 'rb') as f:
#     image_data = f.read()

# print(image_data[:10])
# print(len(image_data))
# chunk_size = 1024
# num_chunks = (len(image_data) + chunk_size - 1) // chunk_size
# print(num_chunks)

# img = mpimg.imread('received_image.jpg')
# plt.imshow(img)
# plt.show()

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8500))

hex_string = "0005f007f2"
byte_string = bytes.fromhex(hex_string)
s.send(byte_string)
time.sleep(1)

hex_string = "000601000106"
byte_string = bytes.fromhex(hex_string)
s.send(byte_string)
time.sleep(1)
hex_string = "0007a01aff0042"
byte_string = bytes.fromhex(hex_string)
s.send(byte_string)
time.sleep(1)
msg = s.recv(1024)
s.close()
print('Connection closed.')
"""
"""
import socket
import struct

# Define the IP address and port number of the camera
ip_address = "localhost"
port = 8500

# Create a TCP/IP socket and connect to the camera
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, port))

# # Set the camera to single frame mode
# mode_cmd = bytes.fromhex('A0020100000003000100')
# client_socket.send(mode_cmd)

# # Set the exposure time to 500 ms
# exposure_cmd = bytes.fromhex('A003030000000500000001F4')
# client_socket.send(exposure_cmd)

# # Start capturing images
# start_cmd = bytes.fromhex('A0020200000003000101')
# client_socket.send(start_cmd)

# Receive the image data from the camera
data_cmd = bytes.fromhex('A0010400000003')
client_socket.send(data_cmd)
data_len_bytes = client_socket.recv(4)
data_len = struct.unpack('>I', data_len_bytes)[0]
data = client_socket.recv(data_len)

# Save the image data to a file
with open('image.bin', 'wb') as f:
    f.write(data)

# Close the connection
client_socket.close()
"""


# Define the IP address and port number to capture traffic on
# ip_address = "localhost"
# port = 8500

# # Define a packet filter to capture traffic on the specified IP address and port
# packet_filter = "host {} and port {}".format(ip_address, port)

# # Define a callback function to process each captured packet


# def process_packet(packet):
#     # Check if the packet has a TCP layer
#     if packet.haslayer(TCP):
#         # Check if the packet is a TCP SYN, ACK, or data packet
#         if packet[TCP].flags & (TCP.SYN | TCP.ACK) == TCP.SYN or packet[TCP].flags & (TCP.SYN | TCP.ACK) == TCP.ACK or len(packet[TCP].payload) > 0:
#             # Print the contents of the packet
#             print(packet.show())


# # Start capturing traffic using the specified packet filter and callback function
# sniff(filter=packet_filter, prn=process_packet)


# create a socket object
from PIL import Image
import io
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the simulation server's IP address and port number
server_address = ('127.0.0.1', 85)

# connect to the server
s.connect(server_address)

# send the image capture command to the server
command = bytes.fromhex('000601000106')
s.send(command)

# receive the image data from the server
data = b''
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    data += chunk

# decode the image data into an image
image = Image.open(io.BytesIO(data))
image.show()

# close the socket connection
s.close()
