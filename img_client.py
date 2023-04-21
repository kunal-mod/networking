import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import socket

HOST = 'localhost'  # server IP address
PORT = 1234  # server port number

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((HOST, PORT))

# Receive the image data
image_data = b''
chunk_size = 5120
while True:
    chunk = s.recv(chunk_size)
    if not chunk:
        break
    image_data += chunk

# Close the connection
s.close()

# Save the image data to a file
with open('received_image.jpg', 'wb') as f:
    f.write(image_data)

# Display the image
img = mpimg.imread('received_image.jpg')
plt.imshow(img)
plt.show()
