import socket
import time

HOST = 'localhost'  # server IP address
PORT = 1234  # server port number

# Read the image data
with open('img1.bmp', 'rb') as f:
    image_data = f.read()

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen(1)

print(f'Server is listening on {HOST}:{PORT}...')

# Wait for a client to connect
conn, addr = s.accept()
print(f'Connected by {addr}')

# Send the image data in chunks of 1024 bytes
chunk_size = 5120
# Round up to the nearest chunk size
num_chunks = (len(image_data) + chunk_size - 1) // chunk_size
for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = start_idx + chunk_size
    conn.sendall(image_data[start_idx:end_idx])
    time.sleep(0.001)

# Close the connection
conn.close()
s.close()
print('Connection closed.')
